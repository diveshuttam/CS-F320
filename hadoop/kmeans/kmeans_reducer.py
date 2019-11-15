import sys
#import numpy
list1 = []
list2 = []
key = None
coord = []
count = 0
new_coords = [[0] * 13, [0] * 13]
new_count = [0, 0]
# print(new_coords)
  
def div(arr, val):
    return list(map(lambda x: x/val, arr))

def kmeans_reducer():
    for lines in sys.stdin:

        lines = lines.strip()
        key, data_tuple = lines.split('\t')
        key, (coord, count) = int(key), eval(data_tuple)
        map_line(key, coord, count)
        if key==0:
            list1.append(coord)
        else:
            list2.append(coord)

    # new_centroid = [[x/y for x, y in zip(new_coords, new_count)]]
    new_centroid = list(map(lambda x: div(x[0],x[1]), zip(new_coords, new_count)))

    #writing new centroids to centroids.txt

    fp = open("centroids.txt", 'w')
    new_centroids_str = ''

    for new_c in new_centroid:
        for c in new_c:
            new_centroids_str += str(c) + ','
        new_centroids_str = new_centroids_str[:-1] + '\n'
        
    fp.write(new_centroids_str)
    fp.close()

        
    print(list1)
    print(list2) 


def map_line(key, coord, count):
    new_coords[key] = [x + y for x, y in zip(new_coords[key], coord)]
    new_count[key] = new_count[key] + count


kmeans_reducer()
