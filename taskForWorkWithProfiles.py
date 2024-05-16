import cProfile
import pstats
import time
import math
from io import StringIO


class Functions:
    @staticmethod
    def factorial(x):
        return math.factorial(x)

    @staticmethod
    def calculate_squares_not_optimized(n):
        squares = {}
        for i in range(1, n + 1):
            squares[i] = i ** 2
        return squares

    @staticmethod
    def calculate_squares_optimized(n):
        return {i: i ** 2 for i in range(1, n + 1)}

    @staticmethod
    def calculate_cubes_not_optimized(n):
        cubes = {}
        for i in range(1, n + 1):
            cubes[i] = i ** 3
        return cubes

    @staticmethod
    def calculate_cubes_optimized(n):
        return {i: i ** 3 for i in range(1, n + 1)}

    @staticmethod
    def delay(seconds):
        time.sleep(seconds)


def main_not_optimized(n, delay_seconds):
    Functions.factorial(n)

    Functions.calculate_squares_not_optimized(n)

    Functions.calculate_cubes_not_optimized(n)

    Functions.delay(delay_seconds)

def main_optimized(n, delay_seconds):
    Functions.factorial(n)

    Functions.calculate_squares_optimized(n)

    Functions.calculate_cubes_optimized(n)

    Functions.delay(delay_seconds)


if __name__ == '__main__':
    try:
        with open("profile_results.txt", 'w') as f:
            f.write("Profiling results for not optimized code:\n")
            profile = cProfile.Profile()
            profile.enable()
            main_not_optimized(1000, 2)
            profile.disable()
            s = StringIO()
            ps = pstats.Stats(profile, stream=s).sort_stats("cumulative")
            ps.print_stats()
            f.write(s.getvalue())

            f.write("\n\nProfiling results for optimized code:\n")
            profile = cProfile.Profile()
            profile.enable()
            main_optimized(1000, 2)
            profile.disable()
            s = StringIO()
            ps = pstats.Stats(profile, stream=s).sort_stats("cumulative")
            ps.print_stats()
            f.write(s.getvalue())

    except Exception as e:
        print(e)
