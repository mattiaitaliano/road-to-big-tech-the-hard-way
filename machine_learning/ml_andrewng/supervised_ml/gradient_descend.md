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

## Calculating gradient descend.

![Representation](../assets/gradient_descend_slope.png)

Considering a simplified model such as J(w) with b = 0, the graph J(w) on y axis and w on x axis represent this parabola towards bottom.

The minimum, so the value of J(w) where the error is minimised, is at a certain value of w.

The gradient descend is in this case an update of w equal to:

w = w - alpha(dJ(w)/dw)

Where:

w - is the current value of w.
alpha - is a small _positive_ number between 0 and 1
dJ(w)/dw - is the derivate of J(w) in w.

The derivate represent the slope of the line that is tangent to the poin (J(w), w) on the cost curve J(w).

This slope can be a positive number (the slope is indeed calculated calculating the ratio hight/base of the triangle between two points on the curve (where the distance is close to zero).

It opens two ways:

w is the value we are calculating, alpha is always positive by definition.

1. If the slope is positive, we are subtracting to w a positive amount, then the value of w is reducing.

w = w - alpha * (positive amount)

2. If the slope is positive, we are subtracting to w a negative amount, so, we are adding a positive amount making w increasing.


w = w - alpha * (negative amount) = w - (- (alpha * (positive amount))) = w + alpha * (positive amount)



