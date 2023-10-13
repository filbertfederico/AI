import random
import math

cities = {'a': (0, 0), 'b': (12, 0), 'c': (10, 10), 'd': (22, 0), 'e': (20, 10), 'f': (22, 10), 'g': (10, 20)}

# Calculate the distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def route_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    return total

def initialize_population(population_size):
    population = []
    cities_list = list(cities.keys())
    for _ in range(population_size):
        route = random.sample(cities_list, len(cities_list))
        population.append(route)
    return population

# Select two parents from the population
def select_parents(population, num_parents):
    return random.sample(population, num_parents)

# Recombine two parent routes to create an offspring
def recombine(parent1, parent2):
    start = random.randint(0, len(parent1) - 2)
    end = random.randint(start + 1, len(parent1) - 1)
    slice = parent1[start:end]
    offspring = [city for city in parent2 if city not in slice]
    return offspring[:start] + slice + offspring[start:]

# Mutate
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        index1, index2 = random.sample(range(len(route)), 2)
        route[index1], route[index2] = route[index2], route[index1]
    return route

def genetic_algorithm(population_size, generations, mutation_rate):
    population = initialize_population(population_size)
    best_route = None
    best_distance = float('inf')

    for _ in range(generations):
        parents = select_parents(population, 2)
        offspring = recombine(*parents)
        offspring = mutate(offspring, mutation_rate)

        if route_distance(offspring) < best_distance:
            best_distance = route_distance(offspring)
            best_route = offspring

    # Ensure the best route starts and ends at 'a'
    if best_route[0] != 'a':
        best_route = ['a'] + best_route
    if best_route[-1] != 'a':
        best_route.append('a')

    return best_route

population_size = 100
generations = 1000
mutation_rate = 0.1

best_route= genetic_algorithm(population_size, generations, mutation_rate)

print("Best Route:", best_route)