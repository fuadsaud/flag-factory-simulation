from simulation import execute_simulation

from graphdata import GraphData

import matplotlib.pyplot as plt
from pprint import PrettyPrinter

def pprint(thing):
    PrettyPrinter(indent=4).pprint(thing)

stats = execute_simulation({
    'hours': 8,
    'print': 3,
    'press': 1,
    'cut': 1,
    'sew': 5,
    'package': 2,
    'order_lambda': 2
})

gd = GraphData(stats)

colors = { 'print': 'blue', 'press': 'green', 'cut': 'yellow', 'sew': 'red', 'package': 'orange' }

tt = gd.total_time()

qt = gd.queue_time()
st =  gd.service_time()

qr = gd.queue_ratio()
sr = gd.service_ratio()

print tt
print qt
print st
print qr
print sr

fig = plt.figure(1)

ax = fig.add_subplot(221)
for resource_type, series in gd.queue_over_time().iteritems():
    ax.plot(gd.timestamps(), series, colors[resource_type])
ax.set_title('Queue')

ax = fig.add_subplot(222)
for resource_type, series in gd.service_over_time().iteritems():
    ax.plot(gd.timestamps(), series, colors[resource_type])
ax.set_title('Service')

ax = fig.add_subplot(223)
ax.bar(range(len(qr.keys())), qr.values(), color=colors.values(), align='center')
ax.set_ylim(0, 1)
ax.set_xticks(range(len(qr.keys())))
ax.set_xticklabels(qr.keys())
ax.set_title('Queue Time Ratio')

ax = fig.add_subplot(224)
ax.bar(range(len(sr.keys())), sr.values(), color=colors.values(), align='center')
ax.set_ylim(0, 1)
ax.set_xticks(range(len(sr.keys())))
ax.set_xticklabels(sr.keys())
ax.set_title('Service Time Ratio')

plt.show()