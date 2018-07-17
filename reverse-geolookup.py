# coding=utf-8
import geoip2.database



DEFAULT_DATABASE_PATH = 'data/GeoLite2-City.mmdb'


"""
GeoLite is a free IP geolocation database comparable to, but less accurate than, 
MaxMind’s GeoIP2 databases. The GeoLite2 Country and City databases are updated 
on the first Tuesday of each month. The GeoLite2 ASN database is updated every 
Tuesday.
In order to run this script, first download the GeoLite2 City database from
https://dev.maxmind.com/geoip/geoip2/geolite2/

You can then pass the path to the database when creating an instance of ReverseGeo
or you can put it in data, and instance the class with no arguments.
"""
class ReverseGeo:
    """ This class implements methods for accessing a GEO Database
       and return a geopoint given an IP"""

    def __init__(self, database_path=DEFAULT_DATABASE_PATH):
        self.reader = geoip2.database.Reader(database_path)

    def reverse_lookup(self, ip):
        """
        Returns a geopoint from a given ip
        :param ip: an ip address
        :return: a geopoint json
        """
        response = self.reader.city(ip)
        print response
        print response.city.names['en'] if 'en' in response.city.names else None
        print response.country.names['en'] if 'en' in response.country.names else None
        geo = {
                'coordinates': {
                    'lat': response.location.latitude,
                    'lon': response.location.longitude
                }
            } if response else None
        return geo


if __name__ == '__main__':
    test = {'city':{'name':{'es':'london'}}}
    print '1',test['city']['name']['es']
    print '2', test.get('city', '1').get('name', '2').get('es', '3')
    print '3', test.get('citio', {}).get('name', {}).get('es', '')
    print '4', test.get('city', {}).get('named', {}).get('es', '')
    print '5', test.get('city', {}).get('name', {}).get('en', '')

    rg = ReverseGeo()
    print rg.reverse_lookup('8.8.8.8')
