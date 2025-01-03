# ruff: noqa: E241
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
import xarray as xr

from xclim.sdba.loess import (
    _constant_regression,  # noqa
    _gaussian_weighting,  # noqa
    _linear_regression,  # noqa
    _loess_nb,  # noqa
    _tricube_weighting,  # noqa
    loess_smoothing,  # noqa
)


@pytest.mark.slow
@pytest.mark.parametrize(
    "d,f,w,n,dx,exp",
    [
        (0, 0.2, _tricube_weighting, 1, False, [-0.0698081, -0.3623449]),
        (0, 0.31, _tricube_weighting, 2, True, [-0.0052623, -0.1453554]),
        (1, 0.2, _tricube_weighting, 3, True, [-0.0555941, -0.9219777]),
        (1, 0.2, _tricube_weighting, 4, False, [-0.0691396, -0.9155697]),
        (1, 0.4, _gaussian_weighting, 2, False, [0.00287228, -0.4469015]),
    ],
)
def test_loess_nb(d, f, w, n, dx, exp):
    regfun = {0: _constant_regression, 1: _linear_regression}[d]
    x = np.linspace(0, 1, num=100)
    y = np.sin(x * np.pi * 10)
    ys = _loess_nb(  # dx is non 0 if dx is True
        x, y, f=f, reg_func=regfun, weight_func=w, niter=n, dx=(x[1] - x[0]) * int(dx)
    )

    assert np.isclose(ys[50], exp[0])
    assert np.isclose(ys[-1], exp[1])


@pytest.mark.slow
@pytest.mark.parametrize("use_dask", [True, False])
def test_loess_smoothing(use_dask, open_dataset):
    tas = open_dataset(
        "cmip3/tas.sresb1.giss_model_e_r.run1.atm.da.nc",
        chunks={"lat": 1} if use_dask else None,
    ).tas.isel(lon=0, time=slice(0, 740))
    tas = tas.where(tas.time.dt.dayofyear != 360)  # Put NaNs

    tasmooth = loess_smoothing(tas, f=0.1).load()

    np.testing.assert_allclose(tasmooth.isel(lat=0, time=0), 263.19834)
    np.testing.assert_array_equal(tasmooth.isnull(), tas.isnull().T)

    # Same but with one missing time, so the x axis is not equally spaced
    tas2 = tas.where(tas.time != tas.time[-3], drop=True)
    tasmooth2 = loess_smoothing(tas2, f=0.1)

    np.testing.assert_allclose(
        tasmooth.isel(time=slice(None, 700)),
        tasmooth2.isel(time=slice(None, 700)),
        rtol=1e-3,
        atol=1e-2,
    )

    # Same but we force not to use the optimization
    tasmooth3 = loess_smoothing(tas, f=0.1, equal_spacing=False)
    np.testing.assert_allclose(tasmooth, tasmooth3, rtol=1e-3, atol=1e-3)


@pytest.mark.slow
@pytest.mark.parametrize("use_dask", [True, False])
def test_loess_smoothing_nan(use_dask):
    # create data with one axis full of nan
    # (random array taken from np.random.randn)
    # fmt: off
    data = np.array(
        [
            -0.993, -0.980, -0.452, -0.076,  0.447,
             0.389,  2.408,  0.966, -0.793,  0.090,
            -0.173,  1.713, -1.579,  0.454, -0.272,
            -0.005, -0.926, -2.022, -1.661, -0.493,
            -0.643,  0.891,  0.194,  0.086,  0.983,
            -1.048,  2.032,  1.174, -0.441, -0.204,
            -1.126,  0.933,  1.987,  0.638,  0.789,
             0.767,  0.676, -1.028,  1.422,  0.453,
        ]
    )
    # fmt: on
    data = data.reshape(2, 2, 10)  # pylint: disable=too-many-function-args
    data[0, 0] = [np.nan] * 10
    da = xr.DataArray(
        data,
        dims=["scenario", "model", "time"],
        coords={"time": pd.date_range("2000-01-01", periods=10, freq="YS")},
    ).chunk({"time": -1})

    out = loess_smoothing(da)

    assert out.dims == da.dims
    # check that the output is all nan on the axis with nan in the input
    assert np.isnan(out.values[0, 0]).all()
