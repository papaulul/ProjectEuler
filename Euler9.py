"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


triples = []
for a in range(1, 250):
    for b in range(1, 400):
        for c in range(1, 750):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    triples.append((a, b, c))
                break


for py in triples:
    print(py)
