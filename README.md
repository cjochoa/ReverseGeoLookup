# Reverse GeoLookup

This class performs a reverse geolookup, returning a geopoint from an IP.
**It depends on GeoLite City database**. GeoLite is a free IP geolocation database comparable to, but less accurate than, MaxMind’s GeoIP2 databases. The GeoLite2 Country and City databases are updated on the first Tuesday of each month. The GeoLite2 ASN database is updated every Tuesday.  
In order to run this script, first download the GeoLite2 City database from  [here](https://dev.maxmind.com/geoip/geoip2/geolite2/) 
  
You can then pass the path to the database when creating an instance of ReverseGeo or you can put it in the data folder, and instance the class with no arguments.