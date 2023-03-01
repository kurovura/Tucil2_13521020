import random
import time
import algoClPair
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Masukan berupa titik-titik sejumlah n yang dibangkitkan secaran acak

n = int(input("Masukkan jumlah titik : "))

points = [(random.randint(0, 2000), random.randint(0, 2000), random.randint(0, 2000)) for i in range(n)]
print("Titik-titik yang dibangkitkan : ")

for p in points:
    print(p)

visual = plt.figure()
ax = visual.add_subplot(111, projection='3d')
xs = [p[0] for p in points]
ys = [p[1] for p in points]
zs = [p[2] for p in points]
ax.scatter(xs, ys, zs, c='black')

# Menggunakan algoritma brute force
starting = time.time()
clPairBF, minDistBF, countEucBF = algoClPair.bfClosestPair(points)
ending = time.time()
durationBF = ending - starting

# Menggunakan algoritma divide and conquer
starting = time.time()
pointsX, pointsY, pointsZ = algoClPair.sorting(points)
clPairDC, minDistDC, countEucDC = algoClPair.dcClosestPair(pointsX, pointsY, pointsZ)
ending = time.time()
durationDC = ending - starting

# Mewarnai titik-titik pada pasangan terdekat dengan warna kuning dan garis penghubung antara pasangan terdekat dengan warna merah
for p in clPairDC:
    ax.scatter(p[0], p[1], p[2], c='yellow')
    x = [p[0], clPairDC[0][0]]
    y = [p[1], clPairDC[0][1]]
    z = [p[2], clPairDC[0][2]]
    ax.plot(x, y, z, c='red')
    
print("\nHasil pencarian pasangan titik terdekat dengan algoritma brute force : ")
print("Pasangan titik terdekat :", clPairBF)
print("Jarak terdekat:", minDistBF)
print("Jumlah operasi euclidean terpakai:", countEucBF)
print("Lama waktu pencarian:", durationBF, "detik")

print("\nHasil pencarian pasangan titik terdekat dengan algoritma divide and conquer:")
print("Pasangan titik terdekat:", clPairDC)
print("Jarak terdekat:", minDistDC)
print("Jumlah operasi euclidean terpakai:", countEucDC)
print("Lama waktu pencarian:", durationDC, "detik")

plt.show()