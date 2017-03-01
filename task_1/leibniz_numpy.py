import numpy as np

number_of_terms = 10

numerators = np.array([4] * number_of_terms)

denominators = np.arange(1, 2 * number_of_terms + 1, step=2, dtype=int)
mask_odd = np.arange(1, len(denominators)+1, step=2)
denominators[mask_odd] *= -1

approx_pi = (numerators / denominators).sum()
print(approx_pi)
