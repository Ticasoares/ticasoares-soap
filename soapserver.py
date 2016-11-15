#!/usr/bin/env python
import web 
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types
from random import randint

urls = ("/temperatura", "TemperaturaService",
        "/temperatura.wsdl", "TemperaturaService",
        )
render = web.template.Template("$def with (var)\n$:var")

class SoapService(SimpleWSGISoapApp):
    temperatura = 0

    @soapmethod(_returns=soap_types.String)
    def getTemperatura(self):
        return str(SoapService.temperatura)

    @soapmethod()
    def setTemperatura(self):
        SoapService.temperatura = randint(0,45)

class TemperaturaService(SoapService):
    """Class for web.py """
    def start_response(self,status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)

    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))


    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()
