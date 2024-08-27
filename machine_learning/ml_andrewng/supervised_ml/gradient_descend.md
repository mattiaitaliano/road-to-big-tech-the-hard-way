# Gradient Descend

It is an algorithm to find the best choice of combination of w and b to minimize J(w, b).

It isn't only used for linear regression, but also for deep learning models.

ng a general algoritmh, it is used to find the minimum of each function that looks like multiparameters just as J(w1,w1,...,wn,b).

## Flow

1. set w = b = 0

2. keep changing w and b to reduce J(w,b)

How?

While the J(w, b) of linear regression looks like an amaca, other cost function such as for deep learning of neural network, have multiple **local** minimums.

After choosing a starting point, the algorithm put the (w,b) a tiny step towards the minimum by choosing the direction where the same step would put it at the lowest. Summing this step by step, you eventually reach a local minimum.

However, if your starting poin is on another position, the local minimum at the end might be different from the previous one.

## Maths behind it

w =  w - alpha(dJ(w,b)/dw)

alpha is the **learning rate**, a small positive number that determine the step of the algorithm. For instance, if alpha is high, the step are fewer than if it is a small amount.

The derivative dJ(w,b)/dw is the direction of the step.

b = b - alpha(dJ(w,b)/db)

same as before.

The algorithm repeat itself until w and b converge. The upload is _simultaneous_, so like to put them into the system (parentesi graffa per entrambe le equazioni).

### Simultaneous update

The right procedure is:

tmp_w = w - alpha(dJ(w, b)/dw)
tmp_b = b - alpha(dJ(w, b)/db)

w = tmp_w
b = tmp_b

so, being simultaneous, it means that the new w isn't considered into J(w,b) of b.

The incorrect one would have been:

tmp_w = w - alpha(dJ(w,b)/dw)
w = tmp_w
tmp_b = b - alpha(dJ(tmp_w, b)/db)
b = tmp_b

In this case, in fact, the b is being calculated with w = tmp_w parameter, not the original w.

**The algorithm says: repeat updating simultaneously w and b until convergence.**


