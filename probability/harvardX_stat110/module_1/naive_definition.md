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


### Binominial coefficient

(n)         n!
( ) = -------------
(k)     (n-k)!k!

this happens for k <= n, while for k > n we got (n k) = 0

e.g. you use it when you have n = 4 people to mix in group of k = 2. How many different combination do you have? You resolve the binominial coefficient. 

note: often, being (n-k)! possible to reproduce on the numerator, try to simplify the equation. e.g. (8 3) = 8*7*6*5! / 5!*3! = 8*7*6/3! = 8*7*6 / 3*2*1 = 336 / 6 = 56


## Vandermonde's Identity

( m + n )      ( m ) (   n   )
(       ) = sum(   ) (       )
(   k   )      ( j ) ( k - j )

sum for k and j = 0

### Story proof explanation

m peacocks and n toucans from which k set of birds will be chosen.

There are (z k) possibilities (with z = m + n) for this set of birds. 

If there are j peacocks m in the set (m j) so the number available for tucans n will be k - j, then summing the cases for j gives us the V's identity.
