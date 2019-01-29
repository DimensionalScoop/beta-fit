import numpy as np
import uncertainties.unumpy as unp
from unvertrainies import ufloat


class Parametrization:
    def __init__(self, name, f, parameter_symbols = None):
        self.name = ""
        self.f = f
        self.unp_f = Reflection.numpy_to_unp()
        self.num_params = Reflection.number_of_arguments() - 1
        if parameter_symbols = None:
            assert self.num_params < 17
            self.parameter_symbols = 'uvklnpqabcdαβγwm'[:self.num_params]


prams = [
    Parametrization("power law", lambda x, a, b: a * np.exp(b * x), 'Aγ'),
    Parametrization("linear", lambda x, a, b: a + x * b),
    Parametrization("quadratic", lambda x, a, b, c: a + b * x + c * x ** 2),
    Parametrization("sin / cos", lambda x, a, b, w, d: b + a * np.sin(w * x + d), 'Abwδ'),  # FIX OMEGA
]


class Parametrizer:
    """Tries to guess a function that parametrized a given set of data"""

    def __init__(self, x, y, x_err = None, y_err = None):
        self.x
        self.y
        pass
