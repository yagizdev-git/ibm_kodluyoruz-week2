#defining points
points = [
            [(1,3), (6,6)],
            [(2,8), (4,7)],
            [(6,3), (8,9)]
          ]

#defining main function
def euclideanDistance(p1, p2):
  xValue = (p1[0] - p2[0]) ** 2
  yValue = (p1[1] - p2[1]) ** 2
  d = (xValue + yValue) ** 0.5
  return d;

#defining a function to print min
def printMin(list):
  minValue = min(list)
  print("Minimum value of the list is ", minValue)

#creating a list that will contain euclidean distances
distances = []

#calculating distance for all pairs
for i in range(len(points)):
  results = euclideanDistance(points[i][0],points[i][1])
  distances.append(results)

printMin(distances)
