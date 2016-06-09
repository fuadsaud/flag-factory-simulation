import simpy

from resources import PrintServant
from resources import PressServant
from resources import CutServant
from resources import SewServant
from resources import PackageServant

from generators import OrderGenerator

# from collectors import DataCollector

def execute_simulation(configuration):
    environment = simpy.Environment()

    _print   = PrintServant(environment, configuration['print'], 1.0)
    _press   = PressServant(environment, configuration['press'], 1.0)
    _cut     = CutServant(environment, configuration['cut'], 1.0)
    _sew     = SewServant(environment, configuration['sew'], 1.0)
    _package = PackageServant(environment, configuration['package'], 1.0)

    order_generator = OrderGenerator(environment, configuration['order_lambda'], _print, _press, _cut, _sew, _package)

    environment.run(until=8 * 60 * 60)

    # print len(order_generator._orders)

    for order in order_generator._orders:
        print order._times

    # client_incoming = list(DataCollector.client_incoming)
    # client_outgoing = list(DataCollector.client_outgoing)

    # DataCollector.reset()

    # return client_incoming, client_outgoing, [c.serialize for c in client_generator.clients], [t.serialize for t in truck_generator.trucks]

