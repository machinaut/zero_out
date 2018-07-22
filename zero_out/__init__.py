#!/usr/bin/env python

import pkgutil
import tensorflow as tf


ops = tf.load_op_library(pkgutil.get_loader('zero_out_ops').get_filename())

zero_out = ops.zero_out
__all__ = ['zero_out']
