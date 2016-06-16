from simulation import execute_simulation

import matplotlib.pyplot as plt
from itertools import groupby
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

def pprint(thing):
    pp.pprint(thing)

stats = execute_simulation({
    'print': 3,
    'press': 1,
    'cut': 1,
    'sew': 5,
    'package': 2,
    'order_lambda': 2
})

timestamps = [snapshot['time'] for snapshot in stats]
resources_by_snap = [snapshot['resources'] for snapshot in stats]

pprint(resources_by_snap)

resources_stats = {
    'print':   [snap[0] for snap in resources_by_snap],
    'press':   [snap[1] for snap in resources_by_snap],
    'cut':     [snap[2] for snap in resources_by_snap],
    'sew':     [snap[3] for snap in resources_by_snap],
    'package': [snap[4] for snap in resources_by_snap]
}

resources_queue_counts = [[d['queue'] for d in data] for resource_type, data in resources_stats.items()]
resources_service_counts = [[d['service'] for d in data] for resource_type, data in resources_stats.items()]

for series in zip(resources_service_counts, ['blue', 'green', 'yellow', 'red', 'orange']):
    plt.plot(timestamps, series[0], series[1])

plt.show()
