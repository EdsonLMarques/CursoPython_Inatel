import folium

class Data:
    def __init__(self,path):
        self._file = open(path, "r")
        self._pointsList = []
        self._inputRead()
        self._processPoint()

    def _inputRead(self):
        self._data = self._file.read().split("\n")
        self._latList = self._data[0].split(",")
        self._lonList = self._data[1].split(",")
        self._textList = self._data[2].split(",")

    def _processPoint(self):
        if len(self._latList) == len(self._lonList) == len(self._textList):
            for i in range(0, len(self._latList) - 1):
                self._pointsList.append([self._latList[i], self._lonList[i], self._textList[i]])

    def getPointList(self):
        return self._pointsList


def plotMap(data):
    lat_lon = [data.getPointList()[0][0], data.getPointList()[0][1]]
    map = folium.Map(location=lat_lon, zoom_start=16)
    for point in data.getPointList():
        lat_lon = [point[0], point[1]]
        tooltip_text = point[2]
        folium.Marker(location=lat_lon, tooltip=tooltip_text).add_to(map)
    return map


# main script
if __name__ == "__main__":
    data = Data("lat_lon.txt")
    map = plotMap(data)
    map.save("map.html")
