# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from setuptools import setup, find_packages

requirements = ['torch==1.12.1+cu113', 'Cython', 'numpy', 'pytorch-pretrained-bert', 'allennlp', 'spacy', 'tqdm', 'termcolor', 'pandas', 'fairseq', 'colorama', 'scipy']
setup(
    name = 'LAMA',
    version = '0.1.2',
    url = 'https://github.com/fairinternal/LAMA',
    author = 'Fabio Petroni & Facebook AI colleagues',
    author_email = 'fabiopetroni@fb.com',
    description = 'LAMA: LAnguage Model Analysis',
    packages = find_packages(),
    install_requires=requirements,
)
