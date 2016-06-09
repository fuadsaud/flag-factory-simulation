import simpy

from numpy.random import weibull

class Servant(object):
    def __init__(self, env, capacity):
        self._env = env
        self._capacity = capacity

class SimpleServant(Servant):
    def __init__(self, env, capacity):
        Servant.__init__(self, env, capacity)

        self._resource = simpy.Resource(self._env, capacity=self._capacity)

    def request(self):
        return self._resource.request()

class PrintServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        # TODO: use proper distribution
        return weibull(self._alpha)

class PressServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        # TODO: use proper distribution
        return weibull(self._alpha)

class CutServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        # TODO: use proper distribution
        return weibull(self._alpha)

class SewServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        # TODO: use proper distribution
        return weibull(self._alpha)

class PackageServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        # TODO: use proper distribution
        return weibull(self._alpha)
