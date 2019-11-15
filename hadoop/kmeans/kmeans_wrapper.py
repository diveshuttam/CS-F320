#!/usr/bin/python3
import subprocess
import sys
import os
from shutil import copyfile


k = 4
counter=0
for i in range(k):
    command = 'python3 kmeans_mapper.py < test_data.csv | sort | python3 kmeans_reducer.py'

    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    encoded_out, encoded_err = proc.communicate()
    out = encoded_out.decode(encoding='utf-8')
    err = encoded_err.decode(encoding='utf-8')

    if err:
        print('INTERNAL ERROR WHILE RUNNING INPUT')
        print(err)
        sys.exit(1)

    # Remove extra line break.
    output_lines = out.split('\n')[:-1]
    print(output_lines[0])

    cluster1=eval(output_lines[0])
    cluster2=eval(output_lines[1])

    new_centroids_str1 = ''

    for l1 in cluster1: 
        
        for c in l1:
            new_centroids_str1 += str(c) + ','
        new_centroids_str1 = new_centroids_str1[:-1] + '\n'

    new_centroids_str2 = ''

    for l1 in cluster2: 
        
        for c in l1:
            new_centroids_str2 += str(c) + ','
        new_centroids_str2 = new_centroids_str2[:-1] + '\n'




    open(f"cluster{i}", 'w').write(new_centroids_str1)
    open(f"cluster{i}_", 'w').write(new_centroids_str2)

    # Open a file
    path = "."
    dirs = os.listdir(path)
    max_file = max(map(lambda x:(len(open(x).readlines),x) if('cluster' in x) else 0, dirs))[0]
    copyfile(max_file, "test_data.csv")
    os.remove(max_file)
    
