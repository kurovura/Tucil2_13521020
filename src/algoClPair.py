def eucDist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

# Algoritma brute force
def bfClosestPair(points):
    minDist = float('inf')
    clPair = None
    countEuc = 0
    totPoints = len(points)
    for i in range(totPoints):
        for j in range(i+1, totPoints):
            dist = eucDist(points[i], points[j])
            countEuc += 1
            if dist < minDist:
                clPair = (points[i], points[j])
                minDist = dist
    return clPair, minDist, countEuc

def quicksort(points, dim):
    if len(points) <= 1:
        return points
    else :
        pivot = points[len(points) // 2][dim]
        left, right, equal = [], [], []
        for point in points:
            if point[dim] < pivot:
                left.append(point)
            elif point[dim] > pivot:
                right.append(point)
            else:
                equal.append(point)
        return quicksort(left, dim) + equal + quicksort(right, dim)

def sorting(points):
    pointsX = quicksort(points, 0)
    pointsY = quicksort(points, 1)
    pointsZ = quicksort(points, 2)
    return pointsX, pointsY, pointsZ


# Algoritma divide and conquer
def dcClosestPair(pointsX, pointsY, pointsZ):
    totPointsX = len(pointsX)
    if totPointsX <= 3:
        return bfClosestPair(pointsX)
    else:
        mid = totPointsX // 2
        midPoint = pointsX[mid]
        leftPointsY = [p for p in pointsY if p[0] <= midPoint[0]]
        rightPointsY = [p for p in pointsY if p[0] > midPoint[0]]
        leftPointsZ = [p for p in pointsZ if p[0] <= midPoint[0]]
        rightPointsZ = [p for p in pointsZ if p[0] > midPoint[0]]
        leftPair, leftMinDist, leftCountEuc = dcClosestPair(pointsX[:mid], leftPointsY, leftPointsZ)
        rightPair, rightMinDist, rightCountEuc = dcClosestPair(pointsX[mid:], rightPointsY, rightPointsZ)
        if leftMinDist < rightMinDist:
            minDist = leftMinDist
            clPair = leftPair
        else:
            minDist = rightMinDist
            clPair = rightPair
        strip = [p for p in pointsY if abs(p[0] - midPoint[0]) < minDist]
        totPointsStrip = len(strip)
        for i in range(totPointsStrip):
            j = i + 1
            while j < totPointsStrip and strip[j][1] - strip[i][1] < minDist:
                dist = eucDist(strip[i], strip[j])
                if dist < minDist:
                    minDist = dist
                    clPair = (strip[i],strip[j])
                j += 1
        countEuc = leftCountEuc + rightCountEuc + j - i
        return clPair, minDist, countEuc
