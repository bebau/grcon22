
# create 97 len preamble with 7 idles and first 7 primes
preamble = [1,0] * 7
for run in [2,3,5,7,11,13,17]:
    preamble += [1]*run + [0]
preamble = np.array(preamble, dtype=bool)

