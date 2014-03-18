# import eventlet
# eventlet.monkey_patch()

from pecan import make_app
from eventlet_test.hooks import simple
from eventlet_test import model


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        hooks=[simple.SimpleHook()],
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
