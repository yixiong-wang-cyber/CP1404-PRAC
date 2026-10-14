"""Simulate a gopher population over a ten-year period."""

import random

STARTING_POPULATION = 1000
MIN_BIRTH_RATE = 0.10
MAX_BIRTH_RATE = 0.20
MIN_DEATH_RATE = 0.05
MAX_DEATH_RATE = 0.25
NUMBER_OF_YEARS = 10


def main():
    """Simulate and display the gopher population for ten years."""
    population = STARTING_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")
    for year in range(1, NUMBER_OF_YEARS + 1):
        born = int(population * random.uniform(MIN_BIRTH_RATE, MAX_BIRTH_RATE))
        died = int(population * random.uniform(MIN_DEATH_RATE, MAX_DEATH_RATE))
        population += born - died
        print(f"Year {year}")
        print()
        print(f"{born} gophers were born. {died} died.")
        print(f"Population: {population}")


main()
