from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer, UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap.soap11 import Soap11


class AutonomyService(ServiceBase):

    @srpc(UnsignedInteger, UnsignedInteger, _returns=UnsignedInteger)
    def travel_time(time: int, charging_time: int):
        # time in second
        # charging_time in second
        return time + charging_time


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    # logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    app = Application([AutonomyService], 'carlee.charge.server.http',
                      in_protocol=Soap11(validator='lxml'),
                      out_protocol=Soap11(),
                      )

    wsgi_app = WsgiApplication(app)

    server = make_server('127.0.0.1', 8000, wsgi_app)

    print("listening to http://127.0.0.1:8000")
    print("wsdl is at: http://localhost:8000/?wsdl")

    server.serve_forever()