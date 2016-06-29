from __future__ import division
import numpy
class GraphData(object):
    def __init__(self, stats):
        self._stats = stats

    def timestamps(self):
        if not hasattr(self, '_timestamps'):
            self._timestamps = [snapshot['time'] for snapshot in self._stats['snapshots']]

        return self._timestamps

    def resources_by_snap(self):
        if not hasattr(self, '_resources_by_snap'):
            self._resources_by_snap = [snapshot['resources'] for snapshot in self._stats['snapshots']]

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

    def queue_time(self):
        if not hasattr(self, '_queue_time'):
            self._queue_time = {
                resource: self._reduce_time(
                    [state['queue'] for state in states],
                    self._stats['resource_counts'][resource]
                )
                for resource, states in self.resources_stats().iteritems()
            }

        return self._queue_time

    def service_time(self):
        if not hasattr(self, '_service_time'):
            self._service_time = {
                resource: self._reduce_time(
                    [state['service'] for state in states],
                    self._stats['resource_counts'][resource]
                )
                for resource, states in self.resources_stats().iteritems()
            }

        return self._service_time

    def queue_ratio(self):
        if not hasattr(self, '_queue_ratio'):
            self._queue_ratio = {
                resource: time / self.total_time() for resource, time in self.queue_time().iteritems()
            }

        return self._queue_ratio

    def service_ratio(self):
        if not hasattr(self, '_service_ratio'):
            self._service_ratio = {
                resource: time / self.total_time() for resource, time in self.service_time().iteritems()
            }

        return self._service_ratio


    def total_time(self):
        return self.timestamps()[-1]
    def orders_with_problem(self):
        return len([order for order in self._stats['orders'] if hasattr(order,'error')])

    def started_orders(self):
        return len(self._stats['orders'])

    def finished_orders(self):
        # print [resource['queue'] for resource in self.resources_by_snap()[-1]]
        return self.started_orders() - sum([resource['queue'] for resource in self.resources_by_snap()[-1]])

    def intervals(self):
        if not hasattr(self, '_interval'):
            self._intervals = []
            prev_t = 0

            for t in self.timestamps():
                self._intervals.append(t - prev_t)
                prev_t = t

        return self._intervals

    def times_details(self, type):
        tmp = [ order._times[type] for order in self._stats['orders'] if hasattr(order,'_times') and type in order._times]
        # print tmp
        return {
            "min" : min(tmp) if len(tmp)   else 0,
            "mean" : numpy.mean(tmp) if len(tmp)   else 0,
            "max" : max(tmp) if len(tmp)   else 0
        }

    def details_print(self):
        return self.times_details("print_wait")

    def details_cut(self):
        return self.times_details("cut_wait")

    def details_sew(self):
        return self.times_details("sew_wait")

    def details_package(self):
        return self.times_details("package_wait")

    def details_press(self):
        return self.times_details("press_wait")


    def _reduce_time(self, states, resource_count):
        tt = 0
        prev_state = 0

        for interval, state in zip(self.intervals(), states):
            tt += interval * prev_state

            prev_state = state

        return tt / resource_count
