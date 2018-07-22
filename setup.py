#!/usr/bin/env python

import os
from setuptools import Extension, setup
from tensorflow.python.platform import sysconfig


os.environ['CC'] = 'g++'
zero_out_ops = Extension(
    name='zero_out_ops',
    sources=['zero_out/ops.cc'],
    language='c++',
    extra_compile_args=sysconfig.get_compile_flags() + ['-std=c++11'],
    extra_link_args=sysconfig.get_link_flags(),
)
setup(
    name='zero_out',
    py_modules=['zero_out'],
    ext_modules=[zero_out_ops],
    version=open('VERSION').read().strip(),
    description='ZeroOut TensorFlow Ops',
    install_requires=['tensorflow'],
    include_package_data=True,
)
