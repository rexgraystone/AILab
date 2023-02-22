# 1. Write a python program to design & analyze the application of Artificial Intelligence for Graph Theory concept.

class City:
    def __init__(self, name):
        self.name = name
        self.connection = {}
    
    def addConnection(self, city, distance):
        self.connection[city] = distance

class StateSpaceGraph:
    def __init__(self):
        self.cities = {}

    def addCities(self, name):
        city = City(name)
        self.cities[name] = city
    
    def addConnection(self, city1, city2, distance):
        self.cities[city1].addConnection(self.cities[city2], distance)
        self.cities[city2].addConnection(self.cities[city1], distance)

    def shortestPath(self, start, end):
        distances = {city: float('inf') for city in self.cities}
        distances[start] = 0
        visited = set()
        unvisited = set(self.cities.values())

        while unvisited:
            currentCity = min(unvisited, key=lambda city: distances[city.name])
            unvisited.remove(currentCity)
            visited.add(currentCity)

            for neighbor, distance in currentCity.connection.items():
                if neighbor in visited:
                    continue

            newDistance = distances[currentCity.name] + distance
            if newDistance < distances[neighbor.name]:
                distances[neighbor.name] = newDistance

        return distances[end]
    
graph = StateSpaceGraph()

graph.addCities('A')
graph.addCities('B')
graph.addCities('C')
graph.addCities('D')
graph.addConnection('A', 'B', 5)
graph.addConnection('A', 'C', 3)
graph.addConnection('B', 'C', 2)
graph.addConnection('B', 'D', 4)
graph.addConnection('C', 'D', 1)

firstCity = input((f"Enter the starting city: "))
secondCity = input((f"Enter the destination city: "))
print(f"The shortest distance between the cities {firstCity} and {secondCity} is {graph.shortestPath(firstCity, secondCity)}.")





