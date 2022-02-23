"""
-   denm.py
-   class denm with constructor and methods
-   @author tnardoneadv - Github : https://github.com/tnardoneadv
"""

class Denm:
    """Class defining a denm message with following features:
        - Station Id : random number
        - Station Type (5:ordinary vehicles, 10:emergency vehicles, 15:road operators vehicles)
        - cause of event (3:work, 4:car accident, 5:traffic jam, 6:slippery road, 7:fog)
        - Gps Latitude from -90 to +90 (integer)
        - Gps Longitude from -180 to 80 (integer)
    """
    def __init__(self):
        self.stationId = 0
        self.stationType = 0
        self.cause = 0
        self.gpsLat = 49.242111
        self.gpsLon = 4.065633

    #Getter
    def getId(self):
        return self.stationId
    def getType(self):
        return self.stationType
    def getCause(self):
        return self.cause
    def getGpsLat(self):
        return self.gpsLat
    def getGpsLon(self):
        return self.gpsLon

    #Setter
    def setId(self,stationId):
        self.stationId = stationId
    def setType(self, stationType):
        self.stationType = stationType
    def setCause(self, cause):
        self.cause = cause
    def setGps(self, gpsLat, gpsLon):
        self.gpsLat = gpsLat
        self.gpsLon = gpsLon
