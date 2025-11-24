Welcome to PySptools v0.15.0
============================

Hyperspectral library for Python

Presentation
============

PySptools is the Python Spectral Tools project. It is hosted on
https://sourceforge.net/projects/pysptools

You can go to the online documentation at https://pysptools.sourceforge.io. The online documentation is updated regularly.

PySptools is a python module that implements spectral and hyperspectral algorithms. Specializations of the library are the endmembers extraction, unmixing process, supervised classification, target detection, noise reduction, convex hull removal, features extraction at spectrum level and a scikit-learn bridge. Version 0.15.0 introduce an experimental machine learning functionality based on XGBoost and LightGBM.

Functionalities
===============

The functions and classes are organized by topics:

    * abundance maps: FCLS, NNLS, UCLS
    * classification: AbundanceClassification, NormXCorr, SAM, SID
    * detection: ACE, CEM, GLRT, MatchedFilter, OSP
    * distance: chebychev, NormXCorr, SAM, SID
    * endmembers extraction: ATGP, FIPPI, NFINDR, PPI
    * machine learning: XGBoost, LightGBM
    * material count: HfcVd, HySime
    * noise: Savitzky Golay, MNF, whiten
    * sigproc: bilateral
    * scikit learn: HyperEstimatorCrossVal, HyperSVC, HyperGradientBoostingClassifier, HyperRandomForestClassifier, HyperKNeighborsClassifier, HyperLogisticRegression and others
    * spectro: convex hull quotient, features extraction (tetracorder style), USGS06 lib interface
    * util: load_ENVI_file, load_ENVI_spec_lib, corr, cov, plot_linear_stretch, display_linear_stretch, convert2D, convert3D, normalize, InputValidation, ROIs and others

The library do an extensive use of the numpy numeric library and can achieve good speed for some functions. The library is mature enough and is very usable even if the development is at a beta stage (and some at alpha).

Dependencies
============

    * Python 2.7 or 3.5, 3.6
    * numpy, required
    * scipy, required
    * scikit-learn, required, version >= 0.18
    * spectral, required, version >= 0.17
    * matplotlib, required, [note: pytsptools >= 0.14.2 now execute on matplotlib 2.0.x and stay back compatible]
    * CVXOPT, optional, version >= 1.1.7, [note: to run FCLS] 
    * jupyter, optional, version >= 1.0.0, [note: if you want to use the notebook display functionality]
    * tabulate, optional, [note: use by ml module]
    * pandas, optional, [note: use by ml module]
    * plotnine, optional, [note: use by ml module, a ggplot2]
    * lightgbm, optional, version 2.1.2 ONLY, [note: use by ml module]
    * xgboost, optional, version 0.72.1 ONLY, [note: use by ml module]

PySptools version 0.15.0 is developed on the linux platform with anaconda version 5.1.0 for both python 2.7 and 3.6.

Installation
============

The latest release is available at these download sites:

    * pypi: https://pypi.python.org/pypi/pysptools
    * sourceforge: http://sourceforge.net/projects/pysptools

For installation, I refer you to the web site https://pysptools.sourceforge.io/installation.html

Algorithms sources
==================

Matlab Hyperspectral Toolbox by Isaac Gerg, visit:
http://sourceforge.net/projects/matlabhyperspec/

The piecewise constant toolbox (PWCTools) by Max A. Little, visit:
http://www.maxlittle.net/software/

The Endmember Induction Algorithms toolbox (EIA), visit:
http://www.ehu.es/ccwintco/index.php/Endmember_Induction_Algorithms (broken?)

HySime by Bioucas-Dias and Nascimento, visit:
http://www.lx.it.pt/~bioucas/code.htm 

Scikit-learn

XGBoost and LightGBM

And papers


In hope that this program is usefull.

Christian Therien
ctherien@users.sourceforge.net
