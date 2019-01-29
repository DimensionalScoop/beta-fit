from typing import Tuple, Function
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp


class BetaFit:
    def __init__(self, f: Function, estimated_parameters: Iterable):
        """
        f: the function the data is later fitted to. The functions first argument must be the
            independent variable (`x`), all other arguments will be treated as
            parameters to be fitted.
        estimated_parameters: an array with rough estimates for the parameters. They should be
            within a few order of magnitude of the real parameters.
        """

        self.done_training = False
        self.done_fit = False
        self.estimated_parameters = None

        self.model = None
        self.x = None
        self.y = None


    def fit(self,
            x: np.ndarray, y: np.ndarray,
            x_err: np.ndarray = None, y_err: np.ndarray = None,
            time_limit = 100
            ) -> Tuple[ufloat]:
        """

        return: Tuple of estimated params as ufloats .
        """
        if self.x is not None:
            log.warning('Fitting new data with same model, overwriting old'
                        'results')
        self.x = x
        self.y = y
        x, y = self.preprocess(x, y, x_err, y_err)
        self.train(time_limit) if not self.done_training
        pass


    def describe(self) -> dict:
        """Prints and returns a summary of the fit results and estimates for the goodness of fit."""
        pass

    # def _chi_squared(self, x,



if __name__ == '__main__':
    f = lambda x, k, l: k * np.exp(-l * x)
    fitter = BetaFit(f)
    fitter.fit(x, y)
