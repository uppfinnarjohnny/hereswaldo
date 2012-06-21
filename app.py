from bottle import route, run, request
from pygeoip import GeoIP
import os

geoip_db = GeoIP('GeoLiteCity.dat')


@route('/')
def index():
    return 'try /locate/(ip) or /locate/me'


@route('/locate/me')
def locateme():
    return geoip_db.record_by_addr(request['HTTP_X_FORWARDED_FOR'])


@route('/locate/:ip')
def locate(ip):
    return geoip_db.record_by_addr(ip)


run(server='gevent', port=os.environ.get('PORT', 8080), host='0.0.0.0')
