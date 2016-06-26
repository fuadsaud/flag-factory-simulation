from simulation import execute_simulation

from graphdata import GraphData

import matplotlib.pyplot as plt
from pprint import PrettyPrinter

def pprint(thing):
    PrettyPrinter(indent=4).pprint(thing)

stats = execute_simulation({
    'hours': 1,
    'print': 3,
    'press': 1,
    'cut': 1,
    'sew': 5,
    'package': 2,
    'order_lambda': 2
})

gd = GraphData(stats)

timestamps = gd.timestamps()
resources_queue_counts = gd.queue_over_time()
resources_service_counts = gd.service_over_time()

colors = {
    'print':   'blue',
    'press':   'green',
    'cut':     'yellow',
    'sew':     'red',
    'package': 'orange'
}

fig = plt.figure(1)

ax = fig.add_subplot(211)
for resource_type, series in resources_queue_counts.iteritems():
    ax.plot(timestamps, series, colors[resource_type])
    ax.set_title('Queue')

ax = fig.add_subplot(212)
for resource_type, series in resources_service_counts.iteritems():
    ax.plot(timestamps, series, colors[resource_type])
    ax.set_title('Service')

plt.show()
