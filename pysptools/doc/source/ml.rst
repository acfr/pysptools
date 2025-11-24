.. automodule:: pysptools.ml

Machine Learning (alpha)
************************

Warning: ml module is experimental and may be subject to backward-incompatible changes.

This module supports LightGBM and XGBoost:

* `LightGBM`_
* `XGBoost`_

.. seealso:: See the file :download:`test_ml_models.py<../../tests/test_ml_models.py>` for an example.


LightGBM
========

Function
--------
.. autofunction:: pysptools.ml.load_lgbm_model

------------------------------

Class
-----
.. autoclass:: pysptools.ml.HyperLGBMClassifier
    :members:


XGBoost
=======

Function
--------
.. autofunction:: pysptools.ml.load_xgb_model

------------------------------

Class
-----
.. autoclass:: pysptools.ml.HyperXGBClassifier
    :members:

