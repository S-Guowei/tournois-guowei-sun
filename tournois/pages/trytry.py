point = {1: 7, 2: 5, 3: 4, 4: 0}
scored = {1: 5, 2: 4, 3: 4, 4: 1}
conceded = {1: 1, 2: 2, 3: 4, 4: 7}

# point = sorted(point.items(), key=lambda x:x[1], reverse=True)   #sort the points
# scored = sorted(scored.items(), key=lambda x:x[1], reverse=True)   #sort the points
# conceded = sorted(conceded.items(), key=lambda x:x[1], reverse=False)   #sort the points
# point = dict(point)       
# scored = dict(scored)       
# conceded = dict(conceded)
length = len(point)
points = {} 
for i in range(length):
    k_n = [(k,v) for k,v in point.items()][0][0] # key to compare
    for k,v in point.items():
        if v > point.get(k_n):
            k_n = k 
        elif v == point.get(k_n):
            print('loop',i,'key',k)
            if scored.get(k) > scored.get(k_n):
                k_n = k
            
            elif  scored.get(k) == scored.get(k_n):
                if conceded.get(k) < conceded.get(k):
                    k_n = k           
    # print(k_n)
    points[k_n] = [point.get(k_n), scored.get(k_n), conceded.get(k_n)]
    point.pop(k_n)
    # print('point:',point)
    # print('points:',points)
    
print(points)