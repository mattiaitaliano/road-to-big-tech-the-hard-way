# Naive definition

Primitive/simplest definition of probability:

Pnaive(A) = A / S 

So, the probability that event A occour are the number of favorable outcome of A divided by the total number of S outcomes (possibilities).

The problem is the formula is too restrictive and relies heavily on some assumptions:

1. S has to be finite
2. Each pebble has the same mass

If something is not equal, finite and simmetrical, it's not 100% right to apply for the naive definition.
However, sometimes it's reliable.

## Counting the pebbles (possibilities) on large datasets

NOTE: this is the way to count, not the probability itself. After counting A and the S numbers, just use A/S formula.

1. Multiplication (3 subsets times 4 events = 12 possibilities)
Note that multiplication works as long as we have the same amount of repetition beweent experiments (subsets) and events.Indeed, if there is a difference and no substitute events, then it's not possible to apply the multiplication counting.

2. Sampling with replacement: e.g. putting back a number already extracted at bingo. n^k where n are the events and k the times we run the experiment. the total possibilities are n^k

3. Sampling with NO replacement: the number of possible outcomes decreas by 1 each time. Then, we have two different scenarios...
    * 0 possibilities if k > n
    * n(n-1)...(n-k+1) if k <= n so [ n! / (n-k)! ]


