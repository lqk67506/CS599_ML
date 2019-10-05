# Code
```
import csv
import random
import numpy

def kmeans(list_1 , list_2):
    # The figure that I want to finish has 10 center points, that means it is 10-means clustering
    #  and I use 10 to replace K in the following code
    mean_x1 = []
    mean_x2 = []
    t_number = 0
    f_number = 0

    # Choose 10 center points from training set randomly, and there are 5 points with true and 5 points with false
    while t_number < 5 or f_number < 5:
        center = random.randint(0, 199)
        if list_y[center] == 0:
            mean_x1.append(list_1[center])
            mean_x2.append(list_2[center])
            f_number += 1
        elif list_y[center] == 1:
            mean_x1.append(list_1[center])
            mean_x2.append(list_2[center])
            t_number += 1

    iteration_times = 0
    cluster_index = 0
    clusters = {}

    # initial the clusters, build a dictionary which include K empty cluster list
    while cluster_index < 10:
        cluster = []
        clusters[cluster_index] = cluster
        cluster_index += 1

    # Because there is no convergence range is mentioned in the textbook, I iteration 10 times to get the finial value
    while iteration_times < 10:
        clean_index = 0

        # Clean all clusters after update center point.
        while clean_index < 10:
            clusters[clean_index].clear()
            clean_index += 1
        loop_index = 0

        # Travel through all training points to put every point in cluster
        while loop_index < 200:
            mean_index = 0
            min_distance = 100
            best_index = 0

            # Travel through all centers to find the best one for the point we are checking
            while mean_index < 10:
                x_1 = list_1[loop_index]
                x_2 = list_2[loop_index]
                mean_1 = mean_x1[mean_index]
                mean_2 = mean_x2[mean_index]
                distance = numpy.sqrt((x_1-mean_1)*(x_1-mean_1) + (x_2-mean_2)*(x_2-mean_2))
                if distance <= min_distance:
                    min_distance = distance
                    best_index = mean_index
                mean_index += 1
            clusters[best_index].append(loop_index)
            loop_index += 1
        update_index = 0

        # Update centers according to the mean value of every cluster
        while update_index < 10:
            x1_total = 0
            x2_total = 0
            for point in clusters[update_index]:
                x1_total += list_1[point]
                x2_total += list_2[point]
                mean_x1[update_index] = x1_total/len(clusters[update_index])
                mean_x2[update_index] = x2_total/len(clusters[update_index])
            update_index += 1
        iteration_times += 1
        print(str(mean_x1))
    return clusters


csv_x = csv.reader(open('D:/CS599 ML/x.csv', encoding='utf-8'))
list_x1 = []
list_x2 = []
for row_x in csv_x:
    if row_x[1] != 'V1':
        x1 = float(row_x[1])
        x2 = float(row_x[2])
        list_x1.append(x1)
        list_x2.append(x2)
csv_y = csv.reader(open('D:/CS599 ML/y.csv', encoding='utf-8'))
list_y = []
for row_y in csv_y:
    if row_y[1] != 'x':
        y = int(row_y[1])
        list_y.append(y)


final_cluster = kmeans(list_x1, list_x2)
print(final_cluster)
```

# Result
```
{0: [24, 34, 41, 62, 107, 108, 109, 110, 111, 113, 116, 118, 123, 133, 136, 143, 145, 149, 150, 154, 160, 166, 172, 174, 178, 180, 183, 186, 197], 1: [114, 115, 124, 126, 128, 129, 131, 142, 148, 152, 179, 190, 193], 2: [15, 25, 27, 28, 32, 39, 40, 42, 45, 47, 48, 49, 67, 70, 72, 73, 74, 75, 85, 87, 91, 93, 99, 104, 122, 125, 137, 159, 161, 168, 177, 182], 3: [6, 10, 11, 21, 54, 78, 88], 4: [7, 16, 46, 53, 55, 94, 105, 106, 121, 132, 134, 139, 144, 151, 155, 157, 164, 167, 175, 176, 184, 185, 189, 191], 5: [17, 30, 50, 59, 81, 84, 101, 102, 156, 165, 188], 6: [5, 8, 20, 23, 31, 38, 52, 64, 69, 71, 77, 82, 83, 89], 7: [1, 2, 3, 4, 13, 14, 18, 19, 22, 33, 35, 37, 51, 56, 57, 60, 63, 68, 76, 80, 86, 95, 98, 119, 135, 146, 147, 181, 187, 194, 199], 8: [0, 9, 12, 29, 36, 43, 58, 66, 79, 92, 96, 97, 100, 141, 153, 163, 173, 196], 9: [26, 44, 61, 65, 90, 103, 112, 117, 120, 127, 130, 138, 140, 158, 162, 169, 170, 171, 192, 195, 198]}

```

# Hint
In the result, it shows the dictionary that contain all 10 clusters. The number in the clusters means the index of the points in traing
dataset. I can get the data with the index from list_x1 and list_x2

