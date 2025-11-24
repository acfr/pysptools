#
#------------------------------------------------------------------------------
# Copyright (c) 2013-2014, Christian Therien
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
#
# dnoise.py - This file is part of the PySptools package.
#

from __future__ import division

import numpy as np
import os.path as osp
import pysptools.util as util


def estimate_noise_covariance(M, dm=1):
    if len(M.shape) == 2:
        idx_non_zero = np.any(np.isfinite(M) & (M != 0.), axis=1)
        M = M[idx_non_zero, :]
        noise = (M[dm:, :] - M[:-dm, :]) / np.sqrt(2.)

    elif len(M.shape) == 3:
        idx_non_zero = np.any(np.isfinite(M) & (M != 0.), axis=2)
        idx_ok = idx_non_zero[dm:, :] & idx_non_zero[:-dm, :]
        noise = (M[dm:, :, :] - M[:-dm, :, :]) / np.sqrt(2.)
        noise = noise[idx_ok]

    else:
        raise ValueError(f'unexpected number of dimensions {M.shape}')

    noise_mag = np.sqrt(np.sum(noise * noise, axis=1))
    noise_med = np.median(noise_mag)
    rayleigh_std = noise_med / np.sqrt(2. * np.log(2.))
    cdf98 = np.sqrt(-2. * np.log(1. - 0.98)) * rayleigh_std
    idx_outliers = noise_mag > cdf98
    noise = noise[~idx_outliers, :]
    return np.cov(noise, rowvar=False)


def whiten(M, sigma, return_inverse=False):
    """
    Whitens a HSI cube. Use the noise covariance matrix to decorrelate
    and rescale the noise in the data (noise whitening).
    Results in transformed data in which the noise has unit variance
    and no band-to-band correlations.

    Parameters:
        M: `numpy array`
            2d matrix of HSI data (N x p).
        sigma: noise covaraince (p x p).


    Returns: `numpy array`
        Whitened HSI data (N x p).

    Reference:
        Krizhevsky, Alex, Learning Multiple Layers of Features from
        Tiny Images, MSc thesis, University of Toronto, 2009.
        See Appendix A.
    """
    U,S,V = np.linalg.svd(sigma)
    S_1_2 = S**(-0.5)
    Aw = U @ np.diag(S_1_2) @ V
    Mw = M @ Aw
    if return_inverse:
        Awinv = U @ np.diag(1./S_1_2) @ V
        return Mw, Awinv

    else:
        return Mw
