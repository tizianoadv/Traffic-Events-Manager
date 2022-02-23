"""
-   cam.py
-   class cam with constructor and methods
-   @author tnardoneadv - Github : https://github.com/tnardoneadv
"""

class Cam:
    """Class defining a cam message with following features:
        - Station Id : random number
        - Station Type (5:ordinary vehicles, 10:emergency vehicles, 15:road operators vehicles)
        - Speed from 0 to 130 km/h (integer)
        - Heading (angle compared to the north - (integer) ) from 0 to 359
        - Gps Latitude from -90 to +90 (integer)
        - Gps Longitude from -180 to 80 (integer)
    """
    def __init__(self):
        self.stationId = 0
        self.stationType = 0
        self.speed = 0
        self.heading = 0
        self.gpsLat = 49.242111
        self.gpsLon = 4.065633

    #Getter
    def getId(self):
        return self.stationId
    def getType(self):
        return self.stationType
    def getSpeed(self):
        return self.speed
    def getHeading(self):
        return self.heading
    def getGpsLat(self):
        return self.gpsLat
    def getGpsLon(self):
        return self.gpsLon

    #Setter
    def setId(self,stationId):
        self.stationId = stationId
    def setType(self, stationType):
        self.stationType = stationType
    def setSpeed(self, speed):
        self.speed = speed
    def setHeading(self, heading):
        self.heading = heading
    def setGps(self, gpsLat, gpsLon):
        self.gpsLat = gpsLat
        self.gpsLon = gpsLon
