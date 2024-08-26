# Linear Regression

x = feature (input)

y = target (output)

In a 2D plot,  a data in the dataset has a coordinate (x, y), so for each feature x there is a target y.

in a dataset there are a lot of rows, so, a lot of (x, y). To determinate them, (x(i), y(i)) = ith training example (row i).

Notation wise, the x^(2) isn't x**2 but is representing the 2nd feature x of the training set.

## Flow

Training set (with feature and targets) 

->

Learning Algorithm 

->

The model f takes a new feature x didn't explored in the training set and estimate a prediction output called y-hat (y cappello).

## Representing model f

F(w,b)(X) = wX + b

It is than a straight line.

It is a linear function that is more likely to be used as a simplified model, that perhaps doesn't represent the reality of a complex prediction (otherwise there would be a curve) but help in understanding.

Being a linear equation, the model is called linear regression. 


