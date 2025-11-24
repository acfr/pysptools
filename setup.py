from distutils.core import setup


setup_requires = ['numpy',
            'scipy',
            'scikit-learn >= 0.18',
            'spectral >= 0.17',
            'matplotlib >= 2.0',
            'cvxopt >= 0.18',
            'jupyter'
            'tabulate',
            'pandas',
            'plotnine',
            'lightgbm = 2.1.2',
            'xgboost = 0.72.1']


setup(name = "pysptools",
    version = "0.15.0",
    description = "A hyperspectral imaging tools box",
    author = "Christian Therien",
    author_email = "ctherien@users.sourceforge.net",
    url = "https://pysptools.sourceforge.io",
    license = "Apache License Version 2.0",
    keywords = "python, hyperspectral imaging, signal processing, library, endmembers, unmixing, pysptools, sam, sid, atgp, N-FINDR, NFINDR, spectroscopy, target detection, georessources, geoimaging, spectral, remote sensing",
    #setup_requires = setup_requires,
    packages=[  'pysptools',
                'pysptools/abundance_maps',
                'pysptools/classification',
                'pysptools/detection',
                'pysptools/distance',
                'pysptools/doc',
                'pysptools/doc/source',
                'pysptools/doc/source/bur',
                'pysptools/doc/source/chull',
                'pysptools/doc/source/hem',
                'pysptools/doc/source/pic',
                'pysptools/doc/source/smk',
                'pysptools/doc/source/_templates',
                'pysptools/eea',
                'pysptools/examples',
                'pysptools/material_count',
                'pysptools/noise',
                'pysptools/tests',
                'pysptools/sigproc',
                'pysptools/skl',
                'pysptools/spectro',
                'pysptools/util',
                'pysptools/ml',
                'pysptools/ml/nbex',
                'pysptools/patches'
                ],
    package_data={'pysptools': ['*.*'],
                  'pysptools/doc': ['*.*'],
                  'pysptools/doc': ['*'],
                  'pysptools/doc/source': ['*.*'],
                  'pysptools/doc/source/bur': ['*.*'],
                  'pysptools/doc/source/chull': ['*.*'],
                  'pysptools/doc/source/hem': ['*.*'],
                  'pysptools/doc/source/pic': ['*.*'],
                  'pysptools/doc/source/smk': ['*.*'],
                  'pysptools/doc/source/_templates': ['*.*'],
                  'pysptools/examples': ['*.html'],
                  'pysptools/ml/nbex': ['*.*'],
                  'pysptools/patches': ['*.patch']},
    long_description = """
PySptools is a python module that implements spectral and hyperspectral algorithms. Specializations of the library are the endmembers extraction, unmixing process, supervised classification, target detection, noise reduction, convex hull removal, features extraction at spectrum level and a scikit-learn bridge. Version 0.15.0 introduce an experimental machine learning functionality based on XGBoost and LightGBM.

The library is designed to be easy to use and almost all functionality has a plot function to save you time with the data analysis process. The actual sources of the algorithms are the Matlab Hyperspectral Toolbox of Isaac Gerg, the pwctools of M. A. Little, the Endmember Induction Algorithms toolbox (EIA), the HySime Matlab module by José Bioucas-Dias and José Nascimento and science papers.

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

Installation
============

For installation, I refer you to the web site https://pysptools.sourceforge.io/installation.html

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
""",
    classifiers=[
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Scientific/Engineering :: Image Recognition",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Visualization"
    ],
)
