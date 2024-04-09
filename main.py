from functions import *

random_seed = 123456789
np.random.seed(random_seed)
random.seed(random_seed)

# Parameters
N = 30  # n. of cities to visit
border_len = 500  # length of border for random city placement
ITERATIONS_WO_IMPROVEMENT_LIMIT = 60  # maximum iterations without improvement before termination
N_POP = N * 4  # population size
CROSSOVER_PROB = 0.95  # initial probability of crossover during genetic algorithm
MUTATION_PROB = 1 / N  # initial probability of mutation during genetic algorithm

# Cities to visit
CITIES_RAND = np.random.rand(N, 2) * border_len
CITIES_CIRCLE = randomize_cities_on_circle(N, border_len // 2 - 10)

# Performing TSP on two sets of points
best_results, median_results, worst_results, n_generations, best_solution = (
    tsp(N, N_POP, CROSSOVER_PROB, MUTATION_PROB, CITIES_RAND, ITERATIONS_WO_IMPROVEMENT_LIMIT))

circle_results = tsp(N, N_POP, CROSSOVER_PROB, MUTATION_PROB, CITIES_CIRCLE,
                     ITERATIONS_WO_IMPROVEMENT_LIMIT)
circle_bs = circle_results[-1]

# Visualization
layout = [
    ["A", "A"],
    ["B", "C"],
]

fig, axes = plt.subplot_mosaic(layout, figsize=(12, 12))
fig.suptitle('Travelling salesman problem', fontsize=22)
fig.patch.set_facecolor('white')

# Line plot with statistics
temp = [i for i in range(1, n_generations + 1)]
axes["A"].plot(temp, median_results, label='Median Road', color='green', linestyle='--')
axes["A"].plot(temp, best_results, label="Best Solution", color='blue')
axes["A"].plot(temp, worst_results, label='Worst Solution', color='red', linestyle='--')
axes["A"].legend()
axes["A"].set_xlabel(f'Generations')
axes["A"].set_ylabel('Fitness function - total road')
axes["A"].set_title(f'Data = CITIES_RAND;   Number of cities = {N};     Population size = {N_POP}\n'
                    f'The shortest road found: {best_results[-1]:.4f}\n'
                    f'Total number of generations: {n_generations}')
axes["A"].set_xlim(0, n_generations)

# Points and the best route for CITIES_RAND
plot_points_and_road(CITIES_RAND, best_solution, axes["B"])
axes["B"].set_title("CITIES_RAND")

# Points and the best route for CITIES_CIRCLE
plot_points_and_road(CITIES_CIRCLE, circle_bs, axes["C"])
axes["C"].set_title("CITIES_CIRCLE")

plt.show()
