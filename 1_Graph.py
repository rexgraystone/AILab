# 1. Write a Python program to design & analyze the application of Artificial Intelligence for Graph Theory concept.

class City:
    def __init__(self, name):
        self.name = name
        self.connection = {}
    
    def add_connection(self, city, distance):
        self.connection[city] = distance

class StateSpaceGraph:
    def __init__(self):
        self.cities = {}

    def add_cities(self, name):
        city = City(name)
        self.cities[name] = city
    
    def add_connection(self, city1, city2, distance):
        self.cities[city1].add_connection(self.cities[city2], distance)
        self.cities[city2].add_connection(self.cities[city1], distance)

    def shortestPath(self, start, end):
        distances = {city: float('inf') for city in self.cities}
        distances[start] = 0
        visited = set()
        unvisited = set(self.cities.values())

        while unvisited:
            current_city = min(unvisited, key=lambda city: distances[city.name])
            unvisited.remove(current_city)
            visited.add(current_city)

            for neighbor, distance in current_city.connection.items():
                if neighbor in visited:
                    continue

            new_distance = distances[current_city.name] + distance
            if new_distance < distances[neighbor.name]:
                distances[neighbor.name] = new_distance

        return distances[end]
    
graph = StateSpaceGraph()

graph.add_cities('A')
graph.add_cities('B')
graph.add_cities('C')
graph.add_cities('D')
graph.add_connection('A', 'B', 5)
graph.add_connection('A', 'C', 3)
graph.add_connection('B', 'C', 2)
graph.add_connection('B', 'D', 4)
graph.add_connection('C', 'D', 1)

start = input((f"Enter the starting city: "))
end = input((f"Enter the destination city: "))
print(f"The shortest distance between the cities {start} and {end} is {graph.shortestPath(start, end)}.")