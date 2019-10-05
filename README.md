# CS599_ML
The project that I choose is building a K-mean algorithm to rebuild the figure 13.2 on textbook

# Introduction
```
The purpose of the project is applying K-means to the mixture data example, print the decision boundary
according to the result and the bayes decesion boundary. Then, we need calculate the training error, 
test error and bayes error.
```
# Dataset
```
The dataset is download online, the dataset is look like:
x	       200 x 2 matrix of training predictors
y	       class variable; logical vector of TRUES and 
	       FALSES - 100 of each
xnew	       matrix 6831 x 2 of lattice points in predictor space
prob	       vector of 6831 probabilities (of class TRUE) at each 
	       lattice point
marginal       marginal probability at each lattice point
px1	       69 lattice coordinates for x.1
px2	       99 lattice values for x.2  (69*99=6831)
means	       20 x 2 matrix of the mixture centers, first ten for one
	       class, next ten for the other

the Bayes error rate is computed as
bayes.error<-sum(marginal*(prob*I(prob<0.5)+(1-prob)*I(prob>=.5)))

If pred is a vector of predictions (of the logit, say):

pred<-predict.logit(xnew)

then the test error is 

test.error<-sum(marginal*(prob*I(pred <0)+(1-prob)*I(pred>=0)))

```
# Steps
```
First, we need do K-mean clustering on the training dataset. The training dataset is the x which contains 200 2-D 
points. Because we have dataset y which shows TRUE or FALSE of all points in dataset x, we can calculate the
training error. Then, we need apply the result of K-mean in lattice dataset xnew which contain 6831 lattice points.
Calculate the distance between each lattice points and the center points that decide by K-mean, mark them the same 
y value with the y value of center points that they close to. After that, draw the boundary using the lattice points
which are divided into different clusters and draw Bayes decesion boundary.Finally, calculate test error and Bayes 
error with the function above
```

# Current finished
```
Now, I have not finished any figure yet. What I have done is divide the training dataset into different clusters.
Same with what I introudce in week 1, I choose 10 points randomly as the center points, that also means the 
training dataset points will be divide into 10 clusters. What I need mention is these 10 points are choosed 
from training dataset and there are 5 center points with TRUE y value and 5 center points with FALSE y value.
Then, because there is no content about convergence range, I iteration the program for 10 times, which means
I will update the center points for 10 times. In every iteration, I calculate the distance between training 
points and center points to find the closest center points for every training points. Then, put the points in
clusters. After that, I calculate the mean of every points and set them as the new center points of the clusters.
Finally, clear every clusters and using new center points to do next iteration.
```

# Current result
```
Now, I can get clusters of training set and the center points. The result shows that the mean values do not change
after 7-9 times loop and I can get the final center points and clusters for training set.
```

# Future work
```
Now, although I cannot provide any fingures, I have finished the most important part of the project which is finishing
K-mean clustering for training dataset.
In the future, I need put every lattice points in different clusters and mark them with TRUE or FALSE at first. After
that, I can get a boundary that generate by K-mean algorithm. After that, I need print the bayes decesion boundary.
Finally, I will calculate the test error and bayes error.
```
