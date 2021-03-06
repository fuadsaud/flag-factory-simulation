import simpy

from numpy.random import uniform
from numpy.random import negative_binomial

class Servant(object):
    def __init__(self, env, capacity):
        self._env = env
        self._capacity = capacity

class SimpleServant(Servant):
    def __init__(self, env, capacity):
        Servant.__init__(self, env, capacity)

        self._resource = simpy.PriorityResource(self._env, capacity=self._capacity)
    def request(self, prio):
        prio = 255
        return self._resource.request(priority=3)

class PrintServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return negative_binomial(119, 0.24878)

class PressServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return uniform(60, 91)

class CutServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return uniform(63, 121)

class SewServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return uniform(119, 178)

class PackageServant(SimpleServant):
    def __init__(self, env, capacity, alpha):
        SimpleServant.__init__(self, env, capacity)
        self._alpha = alpha

    @property
    def service_time(self):
        return uniform(57, 121)
