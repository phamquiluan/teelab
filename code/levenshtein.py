# In information theory, linguistics and computer science,
# the Levenshtein distance is a string metric for
# measuring the difference between two sequences. 

import numpy as np

def calc_levenshtein(a, b):
    cost_matrix = np.zeros((len(a) + 1, len(b) + 1))

    # init
    for i in range(len(a) + 1):
        cost_matrix[i, 0] = i
    for i in range(len(b) + 1):
        cost_matrix[0, i] = i
    

    # run
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            cost_matrix[i, j] = min(
                cost_matrix[i - 1, j] + 1,
                cost_matrix[i, j - 1] + 1,
                cost_matrix[i - 1, j - 1] + cost,
            )

    print(cost_matrix)
    return cost_matrix[-1, -1]


if __name__ == "__main__":
    print(calc_levenshtein("kitten", "sitting"))
    print(calc_levenshtein("kitten", "t"))
    print(calc_levenshtein("t", "t"))
