from numpy.random import binomial

from clients import Order

class OrderGenerator(object):
    def __init__(self, env, _lambda, _dispatcher, _print, _press, _cut, _sew, _package):

        self._env = env
        self._lambda = _lambda
        self._orders = []

        self._dispatcher = _dispatcher
        self._print   = _print
        self._press   = _press
        self._cut     = _cut
        self._sew     = _sew
        self._package = _package

        self._behavior = self._env.process(self.behavior())

    def behavior(self):
        while True:
            orders_to_generate = binomial(29, .87, 1)

            for _ in range(orders_to_generate):
                self._orders.append(
                    Order(
                        self._env,
                        self._dispatcher,
                        self._print,
                        self._press,
                        self._cut,
                        self._sew,
                        self._package
                    )
                )

            yield self._env.timeout(60 * 60)
