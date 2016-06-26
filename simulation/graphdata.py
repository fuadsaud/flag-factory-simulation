class GraphData(object):
    def __init__(self, stats):
        self._stats = stats

    def timestamps(self):
        if not hasattr(self, '_timestamps'):
            self._timestamps = [snapshot['time'] for snapshot in self._stats]

        return self._timestamps

    def resources_by_snap(self):
        if not hasattr(self, '_resources_by_snap'):
            self._resources_by_snap = [snapshot['resources'] for snapshot in self._stats]

        return self._resources_by_snap

    def resources_stats(self):
        if not hasattr(self, '_resources_stats'):
            self._resources_stats = {
                'print':   [snap[0] for snap in self.resources_by_snap()],
                'press':   [snap[1] for snap in self.resources_by_snap()],
                'cut':     [snap[2] for snap in self.resources_by_snap()],
                'sew':     [snap[3] for snap in self.resources_by_snap()],
                'package': [snap[4] for snap in self.resources_by_snap()]
            }

        return self._resources_stats

    def service_over_time(self):
        if not hasattr(self, '_service_over_time'):
            self._service_over_time = {
                resource_type: [d['service'] for d in data]
                for resource_type, data in self.resources_stats().iteritems()
            }

        return self._service_over_time

    def queue_over_time(self):
        if not hasattr(self, '_queue_over_time'):
            self._queue_over_time = {
                resource_type: [d['queue'] for d in data]
                for resource_type, data in self.resources_stats().iteritems()
            }

        return self._queue_over_time
