from numpy.random import uniform

class Order(object):
    def __init__(self, env, _dispatcher, _print, _press, _cut, _sew, _package):
        self._env = env

        self._times = {}
        self._times['created'] = self._env.now

        self._dispatcher = _dispatcher
        self._print   = _print
        self._press   = _press
        self._cut     = _cut
        self._sew     = _sew
        self._package = _package

        self._behavior = self.define_behavior
        self._env.process(self._behavior())

    @property
    def define_behavior(self):
        return self.regular

    def regular(self):
        yield self._env.process(self.do_dispatch())
        yield self._env.process(self.do_print())
        yield self._env.process(self.do_press())
        yield self._env.process(self.do_cut())
        yield self._env.process(self.do_sew())
        yield self._env.process(self.do_package())

    def do_dispatch(self):
        # with self._dispatcher.request() as req:
        #     yield req

        service_time = self._dispatcher.service_time

        yield self._env.timeout(service_time)

    def do_print(self):
        with self._print.request() as req:
            self._times['print_queue'] = self._env.now
            yield req
            self._times['print_start'] = self._env.now
            service_time = self._print.service_time
            yield self._env.timeout(service_time)
            self._times['print_end'] = self._env.now
            self._times['print_wait'] = service_time

    def do_press(self):
        with self._press.request() as req:
            self._times['press_queue'] = self._env.now
            yield req
            self._times['press_start'] = self._env.now
            service_time = self._press.service_time
            yield self._env.timeout(service_time)
            self._times['press_end'] = self._env.now
            self._times['press_wait'] = service_time

    def do_cut(self):
        with self._cut.request() as req:
            self._times['cut_queue'] = self._env.now
            yield req
            self._times['cut_start'] = self._env.now
            service_time = self._cut.service_time
            yield self._env.timeout(service_time)
            self._times['cut_end'] = self._env.now
            self._times['cut_wait'] = service_time

    def do_sew(self):
        with self._sew.request() as req:
            self._times['sew_queue'] = self._env.now
            yield req
            self._times['sew_start'] = self._env.now
            service_time = self._sew.service_time
            yield self._env.timeout(service_time)
            self._times['sew_end'] = self._env.now
            self._times['sew_wait'] = service_time

    def do_package(self):
        with self._package.request() as req:
            self._times['package_queue'] = self._env.now
            yield req
            self._times['package_start'] = self._env.now
            service_time = self._package.service_time
            yield self._env.timeout(service_time)
            self._times['package_end'] = self._env.now
            self._times['package_wait'] = service_time
