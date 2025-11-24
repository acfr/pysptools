Downloading and Installing PySptools
************************************

PySptools can run under Python 2.7 and 3.6. It has been tested for these versions but can probably run under others Python versions.

.. note:: The HSI cubes are, in general, large and the 64 bits version of Python is recommended.

The latest release is available at these download sites:

	* `pypi <https://pypi.python.org/pypi/pysptools>`_
	* `sourceforge <http://sourceforge.net/projects/pysptools/>`_ 

.. warning:: If you use the 'ml' (Machine Learning) module, you needs to apply manually two patches. See the section 'Applying patches' below.

Manual installation
===================

To install somewhere, download the sources, expand it in a directory and add 
the pysptools-0.xx.x directory path to PYTHONPATH system variable.

Distutils installation
======================

You can use Distutils. Expand the sources in a directory,
go to the pysptools-0.xx.x directory and at the command prompt type 'python setup.py install'.

PIP installation
================

The easy way. Install all the requirements, see the file requirements.txt. Type 'pip install pysptools' at the command prompt.

Anaconda installation
=====================

.. note:: An older pysptools version stay on anaconda. This version is to old, use PIP instead.

.. note:: Avoid installing CVXOPT if not needed. From a anaconda version (that I don't know) installing CVXOPT
          automaticaly install OpenBLAS. If you want to stay with MKL, don't install CVXOPT. 

It's a good idea to use anaconda for the complete setup. A fresh anaconda installation comes with numpy, scipy,
scikit-learn, matplotlib, jupyter and pandas. You need to install spectral, cvxopt, tabulate, plotnine, lightgbm
and  xgboost. They all exist as packages for anaconda. Run these CLI commands::

    conda install -y -c conda-forge tabulate
    conda install -y -c conda-forge spectral
    conda install -y -c conda-forge plotnine
    conda install -y -c conda-forge xgboost=0.72.1
    conda install -y -c conda-forge lightgbm=2.1.2
    conda install -y -c conda-forge cvxopt

Finally you can install pysptools using PIP::

    pip install pysptools

Applying patches
================

These patches are needed only if you use the 'ml' module. Otherwise, skip this step.

First, go to the 'patches' directory under 'pysptools' directory::

    cd [somepath]/pysptools/patches

Copy the first patch lightgbm_2.1.2_sklearn.patch to the lightgbm directory, here an example with anaconda::

    cp lightgbm_2.1.2_sklearn.patch [somepath]/anaconda3/lib/python3.6/site-packages/lightgbm

Move to the lightgbm directory and apply the patch::

    cd [somepath]/anaconda3/lib/python3.6/site-packages/lightgbm
    patch -b < lightgbm_2.1.2_sklearn.patch

Do the same for xgboost::

    cd [somepath]/pysptools/patches
    cp xgboost_0.72.1_sklearn.patch [somepath]/anaconda3/lib/python3.6/site-packages/xgboost
    cd [somepath]/anaconda3/lib/python3.6/site-packages/xgboost
    patch -b < xgboost_0.72.1_sklearn.patch


Removing the library
====================

To uninstall the library, you have to do it manually. Go to your python installation. In the
Lib/site-packages folder simply removes the associated pysptools folder and files.

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

The development environment
===========================

The library is developed on the linux platform with anaconda.

* For Python 2.7: anaconda2 v5.1.0
* For Python 3.6: anaconda3 v5.1.0

PySptools 0.14.1 was tested with OpenBLAS on anaconda 4.2.0.

Numerical Stability
===================

After running many tests we can observe that most of the algorithms in this library are numerically stable. But not all! Problems are with FCLS and SVC. I didn't investigate in deep but here I present some observations and how to work around the problem.

These problems are not critical and with a good Python configuration, thanks to Anaconda, we can pass over. With a MKL based Python distribution, if we run the Pine Creek example 2 many times, we observe a cyclic output from FCLS. And from one cycle to another (it exist 2 cycles for example 2), the rendering of the abundances maps is not the same. If we run the same example with a OpenBLAS based Python distribution the cycling disappear and the abundances maps stay the same at each run. I observed something similar with SVC but it's more complex to analyses.

The solution is to avoid MKL and use OpenBLAS when running FCLS. This can be done easily with the new Anaconda version 2.5 (older public Anaconda versions are OpenBLAS only). To setup your environment to OpenBLAS see the following documentation on the Anaconda site: 
`Anaconda 2.5 Release - now with MKL Optimizations <https://www.continuum.io/blog/developer-blog/anaconda-25-release-now-mkl-optimizations>`_. Except for FCLS, MKL can be used without any problem.

.. note:: The recipe below is true for older anaconda version only. You don't need it for recent versions. Installing CVXOPT install OpenBLAS by default.

Here a recipe that I used with Anaconda 4.2.0::

    # install nomkl plus numpy, scipy, numexpr and scikit-learn, all for OpenBLAS
    conda install nomkl
    # Note that cvxopt for OpenBLAS is not updated
    # If it is already there, remove it
    conda remove cvxopt
    # Go to the conda site for cvxopt: https://anaconda.org/anaconda/cvxopt
    # If, by example, you are Linux and Python 3.5, download linux-64/cvxopt-1.1.8-py35_0.tar.bz2
    # In the download directory, type
    conda install cvxopt-1.1.8-py35_0.tar.bz2
    # And finally, but I'm not sure it's usefull
    conda remove mkl mkl-service
    # You done

Release notes
=============

.. toctree::
   :maxdepth: 2

   release_notes

Issues
======

This issue is not fixed (but is on my list):

Hi,
I found a small bug in pysptools but didn't want to sign up for github to create a new issue. 

When using a mask in the extract method of any of the endmember extraction classes, the returned endmember indices are for the compressed array rather than the original array. I was exporting the indices to ENVI5 roi xml files and found the spectral profiles didn't match, but it took me awhile to find the bug.

Cheers,
Steve
