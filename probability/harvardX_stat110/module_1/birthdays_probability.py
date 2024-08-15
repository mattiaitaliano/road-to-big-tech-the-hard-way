from math import log, exp
import matplotlib.pyplot as plt


def birthday_probability(n_people):
    """
    To avoid the overflow error, counting each factorial of big numbers,
    we use exp and log as exp(log(x)) = x and log(a/b) = log(a) + log(b)
    and log(a * b) = log(a) + log(b)

    The formula is P = (365!)/(365-n_people)!*365**n_people
    """
    s = n_people * log(365) # log of 365^n
    a = sum(log(i) for i in range(365, 365 - n_people, -1))
    p = 1 - exp(a - s)
    return p


if __name__ == '__main__':
    probabilities = []

    for people in range(1,101):
        p = birthday_probability(people)
        probabilities.append(p)

    
    plt.figure(figsize=(12,6))
    plt.plot([i for i in range(1,101)], probabilities, ':bo')

    plt.axhline(y = 0.5, color = 'r', linestyle = '-')

    plt.show()
