"Vectors are the usual arrays in R. Also the single variable is considered vector with size 1"

"Combine a comma-separated value in a vector by putting it into c() function "

MyVector <- c(3,45,56,732)
MyVector
is.numeric(MyVector) #true
is.integer(MyVector) #false
is.double(MyVector)  #true

"Automatically R put numbers as double, to put them as int add L at the end"

AnotherVector <- c(3L, 12L, 243L, 0L)
AnotherVector

is.numeric(AnotherVector) #true
is.integer(AnotherVector) #true
is.double(AnotherVector)  #false

"On a vector you can/must find only the same types"

FinalVector <- c("a", "B3", "hello", 7)
FinalVector #7 converted in str

is.numeric(FinalVector)    #false
is.character(FinalVector)  #true

#####################################################################

"Other basics functions are sequence and replicate"

seq(1,15)    #as writing 1:15 -> [1] 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
seq(1,15,2)  #as above but with a step of 2

z <- seq(1,15,4)
z

rep(3,50) #50 times 3 as 3,3,3,3,3,3,3,3,...,3 50 times
x <- c(80, 20)
x
rep(x, 30)
