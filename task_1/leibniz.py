number_of_terms = 10

indexed_denoms = enumerate(range(1, 2 * number_of_terms + 1, 2))
approx_pi = sum([4 / (pow(-1, i % 2) * x) for (i, x) in indexed_denoms])

print(approx_pi)
