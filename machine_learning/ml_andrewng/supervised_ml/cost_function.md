# Cost Function
### Squared error cost function

Taking in account the linear regression, a y(i) of a training set is the output of a feature x(i).

However, when constructing the regression f(x) it is possible that for the same x(i) the predicted y-hat isn't equal to y(i) but it's different.

Fort this reason, we called error the positive delta between y(i) and y-hat:

Error: (y-hat - y(i))^2

The **cost function** is indeed the sum of all the errors for the m number of training example.

sum(m, i=1)(y-hat(i) - y(i))^2

But we need to find the average squared error, so it is possible to find y-hat(i) close to y(i) for all (x(i), y(i))

to do that, we just devide this sum by m, the total number of the training examples.

1/m * sum(m, i=1)(y-hat(i) - y(i))^2

By convention, in ML it is also devided by two. 
So:

J(w,b) = 1/2m SUM(m, i=1)(f(w,b)(x(i)) - y(i))^2

as y-hat(i) = f(w,b)(x(i)) = wx(i) + b

The final aim is to indeed find w, b so to better construct a solid predictive model reducing the error.

## Overview

The ML model is f(w,b)(x) = wX + b

Being a predictive model, the goal is to minimize the errors between the output y correct and the ones forecasted.

The cost function represent the error, so the goal is to minimize J(w,b) by adjusting the parameters w and b.

## Graph of J(w,b)

1. Hypotesis: b = 0

We plot it not like the linear regression function in x and y, but we do it with x axis = w and y axis = J(w)

We need to resolve the cost function for each w and draw all the coordinates of the curve to draw it on the graph.

J is a parabola toward down where the min value is the w for what J(w) = 0, so no error at all.

## Choose w and b

This is the real problem, in fact by minimazing for w and b the cost function J(w,b) you pick the values for b and w that make J(w,b) = 0.

## Differences.

The linear regression is a flat line, while J is a parabola.


