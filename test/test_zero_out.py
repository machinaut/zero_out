#!/usr/bin/env python

import unittest
import zero_out
import numpy as np
import tensorflow as tf


class TestZeroOut(unittest.TestCase):
    def test_zero_out(self):
        with tf.Session(''):
            result = zero_out.zero_out([[1, 2], [3, 4]]).eval()
            np.testing.assert_equal(result, [[1, 0], [0, 0]])


if __name__ == '__main__':
    unittest.main()
