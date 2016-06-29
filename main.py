from simulation import execute_simulation
from numpy.random import binomial
from graphdata import GraphData

import matplotlib.pyplot as plt
from pprint import PrettyPrinter

def pprint(thing):
    PrettyPrinter(indent=4).pprint(thing)

config = {
    'hours': 8,
    'print': 3,
    'press': 1,
    'cut': 1,
    'sew': 5,
    'package': 2,
    'orders_count': lambda: binomial(29,.87,1),
    'order_lambda': 2
}

stats = execute_simulation(config)

gd = GraphData(stats)

resources = ['print', 'press', 'cut', 'sew', 'package']
colors = ['blue', 'green', 'yellow', 'red', 'orange']
colors_map = dict(zip(resources, colors))

tt = gd.total_time()

qt = gd.queue_time()
st =  gd.service_time()

qr = gd.queue_ratio()
sr = gd.service_ratio()

# print tt
# print qt
# print st
# print qr
# print sr


print('*************DATA****************')
print "Orders created: %d" % (gd.started_orders())
print "Orders not finished: %d" % (gd.started_orders() - gd.finished_orders())
print "Orders with problem: %d" % (gd.orders_with_problem())

tmp = gd.details_print();
print "Print Queue time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_press();
print "Press Queue time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_sew();
print "Sew Queue time \t\t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_cut();
print "Cut Queue time \t\t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_package();
print "Package Queue time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])

tmp = gd.details_print_service();
print "Print Service time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_press_service();
print "Press Service time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_sew_service();
print "Sew Service time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_cut_service();
print "Cut Service time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
tmp = gd.details_package_service();
print "Package Service time \t\tmin: %s,mean: %s, max: %s" % (tmp["min"],tmp['mean'], tmp['max'])
print('*********************************')



fig = plt.figure(1)

ax = fig.add_subplot(221)
for resource_type, series in gd.queue_over_time().iteritems():
    ax.plot(gd.timestamps(), series, colors_map[resource_type])
ax.set_title('Queue')

ax = fig.add_subplot(222)
for resource_type, series in gd.service_over_time().iteritems():
    ax.plot(gd.timestamps(), series, colors_map[resource_type])
ax.set_title('Service')

ax = fig.add_subplot(223)
ax.bar(range(len(resources)), [qr[r] for r in resources], color=colors, align='center')
ax.set_ylim(0, 1)
ax.set_xticks(range(len(resources)))
ax.set_xticklabels(resources)
ax.set_title('Queue Time Ratio')

ax = fig.add_subplot(224)
print sr
print sr.keys()
ax.bar(range(len(resources)), [sr[r] for r in resources], color=colors, align='center')
ax.set_ylim(0, 1)
ax.set_xticks(range(len(resources)))
ax.set_xticklabels(resources)
ax.set_title('Service Time Ratio')

plt.show()
