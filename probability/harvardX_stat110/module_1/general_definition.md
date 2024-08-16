# General definition.

Probability space consist in a sample space S and a probability function P which takes an event A containd in S as input and return P(A), a real number between 0 and 1.

This function P must satisfy two axioms:

1. P(0) = 0 and P(S) = 1
2. If A1, A2, .... are disjoint events, then:

P(Unione di tutti gli eventi Aj all'infinito) = Sommatoria infinita con j=1 di P(Aj)

So, by summing the probability of the events that are disjoint (cannot happen together) you obtain the probability that one of them will happen.

Being not naive environment, we consider infinite number of events.

## Properties:

Ac is A complement, so event A disjoint of A.

1. P(Ac) = 1 - P(A)

2. if A contained in B, then P(A) <= P(B)

3. P(A union B) = P(A) + P(B) - P(A intersected B)

## Theorem of Inclusion - Exclusion

For any events A, ...., An

P(union of all Ai) = Sum i (P(Ai)) - sum i < j (P(Ai intersected Aj) + sum i < j < k (P(Ai intersected Aj intersected Ak)) - ... + (-1)^n+1 * P(A1 intersected ...... intersected An)

It is a way to count the probabilities of union of the events considering their sovrappositions.

e.g. P(A U B) = P(A) + P(B) - P(A intersected B)

We subtract intersection to not double consider the events (as the happen both times)

So, we initially sum all the individual probabilities, then we subtract each couples of events happening at the same times, plus all the probabilities of all events happen at the same time.


The previous general formula states that we:

1. Firstly: sum all the single probabilities.

2. Secondly: sub/add all the coupes, triplet etc etc (_note: alternating the signs_)

3. Intersect all the events (-1)^n+1 * P(A union .... union An) (_note: depending on n, you can subtract or add it_)

