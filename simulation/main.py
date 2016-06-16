from simulation import execute_simulation

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

timestamps = [snapshot['time'] for snapshot in stats]
resources_by_snap = [snapshot['resources'] for snapshot in stats]

resources_stats = {
    'print':   [snap[0] for snap in resources_by_snap],
    'press':   [snap[1] for snap in resources_by_snap],
    'cut':     [snap[2] for snap in resources_by_snap],
    'sew':     [snap[3] for snap in resources_by_snap],
    'package': [snap[4] for snap in resources_by_snap]
}

resources_queue_counts = {
    resource_type: [d['queue'] for d in data]
    for resource_type, data in resources_stats.iteritems()
}

resources_service_counts = {
    resource_type: [d['service'] for d in data]
    for resource_type, data in resources_stats.iteritems()
}

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
