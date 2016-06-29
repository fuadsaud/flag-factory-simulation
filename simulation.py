import simpy

import pprint

from functools import partial, wraps

from resources import PrintServant
from resources import PressServant
from resources import CutServant
from resources import SewServant
from resources import PackageServant

from generators import OrderGenerator

pp = pprint.PrettyPrinter(indent=4)

def patch_resource(resource, pre=None, post=None):
    """Patch *resource* so that it calls the callable *pre* before each
    put/get/request/release operation and the callable *post* after each
    operation.  The only argument to these functions is the resource
    instance.

    """
    def get_wrapper(func):
        # Generate a wrapper for put/get/request/release
        @wraps(func)
        def wrapper(*args, **kwargs):
            # This is the actual wrapper
            # Call "pre" callback
            if pre:
                pre(resource)

            # Perform actual operation
            ret = func(*args, **kwargs)

            # Call "post" callback
            if post:
                post(resource)

            return ret
        return wrapper

    # Replace the original operations with our wrapper
    for name in ['put', 'get', 'request', 'release']:
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))

def monitor(data, all_resources, resource):
    """This is our monitoring callback."""
    data.append(
        {
            'time': resource._resource._env.now,
            'resources': [
                {
                    'service': res._resource.count,
                    'queue': len(res._resource.queue),
                    'type': res.__class__.__name__
                }
                for res
                in all_resources
            ]
        }
    )

def execute_simulation(configuration):
    environment = simpy.Environment()

    _print   = PrintServant(environment, configuration['print'], 1.0)
    _press   = PressServant(environment, configuration['press'], 1.0)
    _cut     = CutServant(environment, configuration['cut'], 1.0)
    _sew     = SewServant(environment, configuration['sew'], 1.0)
    _package = PackageServant(environment, configuration['package'], 1.0)

    resources = [_print, _press, _cut, _sew, _package]

    order_generator = OrderGenerator(
        environment,
        configuration['order_lambda'],
        _print, _press, _cut, _sew, _package,
        configuration['orders_count']
    )

    stats = []

    for res in resources:
        patch_resource(res, post=partial(monitor, stats, resources))

    environment.run(until=configuration['hours'] * 60 * 60)

    return {
        'snapshots': stats,
        'resource_counts': {
            'print':   configuration['print'],
            'press':   configuration['press'],
            'cut':     configuration['cut'],
            'sew':     configuration['sew'],
            'package': configuration['package'],
        },
        'orders': order_generator._orders
    }
