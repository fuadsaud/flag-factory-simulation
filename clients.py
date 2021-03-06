from numpy.random import uniform

import random

class Order(object):
    def __init__(self, env, _print, _press, _cut, _sew, _package, _orderGenerator, _prio = 255):
        self._env = env

        self._times = {}
        self._times['created'] = self._env.now

        self._print   = _print
        self._press   = _press
        self._cut     = _cut
        self._sew     = _sew
        self._package = _package
        self._prio = _prio
        self._orderGenerator = _orderGenerator
        self._behavior = self.define_behavior
        self._env.process(self._behavior())

    @property
    def define_behavior(self):
        return self.regular

    def regular(self):
        yield self._env.process(self.do_print())
        if random.randrange(0, 100, 1) == 1 :
            self.error = 'print'
            self._orderGenerator.newOrder(1)
            return

        yield self._env.process(self.do_press())
        if random.randrange(0, 100, 1) == 1 :
            self.error = 'press'
            self._orderGenerator.newOrder(1)
            return

        yield self._env.process(self.do_cut())
        if random.randrange(0, 100, 1) == 1 :
            self.error = 'cut'
            self._orderGenerator.newOrder(1);
            return
        yield self._env.process(self.do_sew())
        if random.randrange(0, 100, 1) == 1 :
            self.error = 'sew'
            self._orderGenerator.newOrder(1)
            return
        yield self._env.process(self.do_package())
        if random.randrange(0, 100, 1) == 1 :
            self.error = 'package'
            self._orderGenerator.newOrder(1)
            return

    def do_print(self):
        with self._print.request(self._prio) as req:
            self._times['print_queue'] = self._env.now
            yield req
            self._times['print_start'] = self._env.now
            self._times['print_wait'] = (self._times['print_start'] - self._times['print_queue'])
            service_time = self._print.service_time
            yield self._env.timeout(service_time)
            self._times['print_end'] = self._env.now

    def do_press(self):
        with self._press.request(self._prio) as req:
            self._times['press_queue'] = self._env.now
            yield req
            self._times['press_start'] = self._env.now
            self._times['press_wait'] = (self._times['press_start'] - self._times['press_queue'])
            service_time = self._press.service_time
            yield self._env.timeout(service_time)
            self._times['press_end'] = self._env.now
            # self._times['press_wait'] = service_time

    def do_cut(self):
        with self._cut.request(self._prio) as req:
            self._times['cut_queue'] = self._env.now
            yield req
            self._times['cut_start'] = self._env.now
            self._times['cut_wait'] = (self._times['cut_start'] - self._times['cut_queue'])
            service_time = self._cut.service_time
            yield self._env.timeout(service_time)
            self._times['cut_end'] = self._env.now
            # self._times['cut_wait'] = service_time

    def do_sew(self):
        with self._sew.request(self._prio) as req:
            self._times['sew_queue'] = self._env.now
            yield req
            self._times['sew_start'] = self._env.now
            self._times['sew_wait'] = (self._times['sew_start'] - self._times['sew_queue'])
            service_time = self._sew.service_time
            yield self._env.timeout(service_time)
            self._times['sew_end'] = self._env.now
            # self._times['sew_wait'] = service_time

    def do_package(self):
        with self._package.request(self._prio) as req:
            self._times['package_queue'] = self._env.now
            yield req
            self._times['package_start'] = self._env.now
            self._times['package_wait'] = (self._times['package_start'] - self._times['package_queue'])
            service_time = self._package.service_time
            yield self._env.timeout(service_time)
            self._times['package_end'] = self._env.now
            # self._times['package_wait'] = service_time
