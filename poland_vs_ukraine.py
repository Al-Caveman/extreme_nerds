# there r more extreme nerds in ##poland than in ##ukraine.  but is this
# difference statistically significant?  this simulates the p value of this
# observation.

import random

poland = [
    # extreme nerds
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    # normies
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

ukraine = [
    # extreme nerds
    1, 1, 1, 1, 1,
    # normies
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

def random_sample(population, k):
    random.shuffle(population)
    return population[0:k]

def pairwise_shuffle(a, b):
    shuffled = []
    for i in range(0, len(a)):
        if random.randint(0, 1):
            shuffled.append(a[i])
        else:
            shuffled.append(b[i])
    return shuffled

# sim begin
sim_rounds = 10000
null_rejection_failed = 0
random.seed(0)
for r in range(0, sim_rounds):
    # get equal samples from populations
    k = min(len(poland), len(ukraine))
    poland_k = random_sample(poland, k)
    ukraine_k = random_sample(ukraine, k)

    # simulate sample distribution under null hypothesis
    null = pairwise_shuffle(poland_k, ukraine_k)

    # count extreme nerds in samples
    poland_k_extreme_nerds = sum(poland_k)
    ukraine_k_extreme_nerds = sum(ukraine_k)
    null_extreme_nerds = sum(null)

    # test if difference between poland vs. ukraine is more extreme than
    # poland's vs. synthesized null
    k_diff = abs(poland_k_extreme_nerds - ukraine_k_extreme_nerds)
    null_diff = abs(poland_k_extreme_nerds - null_extreme_nerds)

    # is the difference between poland vs. ukraine more extreme than the
    # difference between poland and null?
    if null_diff >= k_diff:
        null_rejection_failed += 1


# print p value
p_value = null_rejection_failed / sim_rounds
print('p value: {}'.format(p_value))
