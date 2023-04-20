from django.test import TestCase

# Create your tests here.
point = {2: 4, 3: 4, 4: 7, 5: 1}
scored = {2: 5, 5: 4, 3: 6, 4: 6}
conceded = {2: 5, 5: 6, 3: 7, 4: 3}

point = sorted(point.items(), key=lambda x:x[1], reverse=True)   #sort the points
scored = sorted(scored.items(), key=lambda x:x[1], reverse=True)   #sort the points
conceded = sorted(conceded.items(), key=lambda x:x[1], reverse=False)   #sort the points
point = dict(point)       
scored = dict(scored)       
conceded = dict(conceded)
length = len(point)
points = {} 
for i in range(length):
    k_n = [(k,v) for k,v in point.items()][0][0] # key to compare
    for k,v in point.items():
        if v > point.get(k_n):
            k_n = k 
        elif v == point.get(k_n):
            if scored.get(k) > scored.get(k):
                k_n = k
            elif  scored.get(k) == scored.get(k_n):
                if conceded.get(k) < conceded.get(k):
                    k_n = k
    points[k_n] = [point.get(k_n), scored.get(k_n), conceded.get(k_n)]
    point.pop(k_n)
