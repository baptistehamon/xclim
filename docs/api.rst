===
API
===

Indicators
==========

.. toctree::
   :maxdepth: 1

   api_indicators

Indices
=======

See: :ref:`indices:Climate Indices`

Health Checks
=============

See: :ref:`checks:Health Checks`

Translation Tools
=================

See: :ref:`internationalization:Internationalization`

Ensembles Module
================

.. automodule:: xclim.ensembles
   :members: create_ensemble, ensemble_mean_std_max_min, ensemble_percentiles
   :noindex:

.. automodule:: xclim.ensembles._reduce
   :noindex:

.. Use of autofunction is so that paths do not include private modules.
.. autofunction:: xclim.ensembles.kkz_reduce_ensemble
   :noindex:

.. autofunction:: xclim.ensembles.kmeans_reduce_ensemble
   :noindex:

.. autofunction:: xclim.ensembles.plot_rsqprofile
   :noindex:

.. automodule:: xclim.ensembles._robustness
   :noindex:

.. autofunction:: xclim.ensembles.robustness_fractions
   :noindex:

.. autofunction:: xclim.ensembles.robustness_categories
   :noindex:

.. autofunction:: xclim.ensembles.robustness_coefficient
   :noindex:

.. automodule:: xclim.ensembles._partitioning
    :noindex:

.. autofunction:: xclim.ensembles.hawkins_sutton
    :noindex:

.. autofunction:: xclim.ensembles.lafferty_sriver
    :noindex:

Units Handling Submodule
========================

.. automodule:: xclim.core.units
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. _sdba-user-api:

SDBA Module
===========

.. warning::

    The SDBA submodule is in the process of being split from `xclim` in order to facilitate development and effective
    maintenance of the SDBA utilities. The `xclim.sdba` functionality will change in the future.
    For more information, please visit https://xsdba.readthedocs.io/en/latest/.

.. automodule:: xclim.sdba.adjustment
   :members:
   :exclude-members: BaseAdjustment
   :special-members:
   :show-inheritance:
   :noindex:

.. automodule:: xclim.sdba.processing
   :members:
   :noindex:

.. automodule:: xclim.sdba.detrending
   :members:
   :show-inheritance:
   :exclude-members: BaseDetrend
   :noindex:

.. automodule:: xclim.sdba.utils
   :members:
   :noindex:

.. autoclass:: xclim.sdba.base.Grouper
   :members:
   :class-doc-from: init
   :noindex:

.. automodule:: xclim.sdba.nbutils
   :members:
   :noindex:

.. automodule:: xclim.sdba.loess
   :members:
   :noindex:

.. automodule:: xclim.sdba.properties
   :members:
   :exclude-members: StatisticalProperty
   :noindex:

.. automodule:: xclim.sdba.measures
   :members:
   :exclude-members: StatisticalMeasure
   :noindex:

.. _spatial-analogues-api:

Spatial Analogues Module
========================

.. autoclass:: xclim.analog.spatial_analogs
   :noindex:

.. autofunction:: xclim.analog.friedman_rafsky
   :noindex:

.. autofunction:: xclim.analog.kldiv
   :noindex:

.. autofunction:: xclim.analog.kolmogorov_smirnov
   :noindex:

.. autofunction:: xclim.analog.nearest_neighbor
   :noindex:

.. autofunction:: xclim.analog.seuclidean
   :noindex:

.. autofunction:: xclim.analog.szekely_rizzo
   :noindex:

.. autofunction:: xclim.analog.zech_aslan
   :noindex:

Subset Module
=============

.. warning::
    The `xclim.subset` module was removed in `xclim==0.40`. Subsetting is now offered via `clisops.core.subset`.
    The subsetting functions offered by `clisops` are available at the following link: :doc:`CLISOPS core subsetting API <clisops:api>`

.. note::
    For more information about `clisops` refer to their documentation here:
    :doc:`CLISOPS documentation <clisops:readme>`

Other Utilities
===============

.. automodule:: xclim.core.calendar
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. automodule:: xclim.core.formatting
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. automodule:: xclim.core.options
   :members: set_options
   :noindex:

.. automodule:: xclim.core.utils
   :members:
   :undoc-members:
   :member-order: bysource
   :show-inheritance:
   :noindex:

Modules for xclim Developers
============================

Indicator Tools
---------------

.. automodule:: xclim.core.indicator
   :members:
   :member-order: bysource
   :show-inheritance:
   :noindex:

Bootstrapping Algorithms for Indicators Submodule
-------------------------------------------------

.. automodule:: xclim.core.bootstrapping
   :members:
   :show-inheritance:
   :noindex:

.. _`sdba-developer-api`:

SDBA Utilities
--------------

.. warning::

    The SDBA submodule is in the process of being split from `xclim` in order to facilitate development and effective
    maintenance of the SDBA utilities. The `xclim.sdba` functionality will change in the future.
    For more information, please visit https://xsdba.readthedocs.io/en/latest/.

.. automodule:: xclim.sdba.base
   :members:
   :show-inheritance:
   :exclude-members: Grouper
   :noindex:

.. autoclass:: xclim.sdba.detrending.BaseDetrend
   :members:
   :noindex:

.. autoclass:: xclim.sdba.adjustment.TrainAdjust
   :members:
   :noindex:

.. autoclass:: xclim.sdba.adjustment.Adjust
   :members:
   :noindex:

.. autofunction:: xclim.sdba.properties.StatisticalProperty
   :noindex:

.. autofunction:: xclim.sdba.measures.StatisticalMeasure
   :noindex:

.. _`spatial-analogues-developer-api`:

Spatial Analogues Helpers
-------------------------

.. autofunction:: xclim.analog.metric
   :noindex:

.. autofunction:: xclim.analog.standardize
   :noindex:

Testing Module
--------------

.. automodule:: xclim.testing.utils
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. automodule:: xclim.testing.helpers
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:
