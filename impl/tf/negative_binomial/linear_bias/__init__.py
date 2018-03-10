# absolute imports
from impl.tf import TFEstimatorGraph, TFEstimator
# from impl.tf.negative_binomial import EstimatorGraph as NegativeBinomialEstimatorGraph
from impl.tf.negative_binomial import fit as fit_nb

from models.negative_binomial.linear_bias.estimator import AbstractEstimator

# relative imports
from .util import *
from .estimator import *
