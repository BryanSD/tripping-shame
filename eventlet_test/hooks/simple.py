from pecan.hooks import PecanHook

import eventlet


class SimpleHook(PecanHook):

    def before(self, state):
        eventlet.sleep(5)
        print "\nabout to enter the controller..."

    def after(self, state):
        print "\nmethod: \t %s" % state.request.method
        print "\nresponse: \t %s" % state.response.status
