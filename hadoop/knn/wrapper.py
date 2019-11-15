#!/usr/bin/env python
import heapq
import subprocess
import sys

local=False

class Heap():
    def __init__(self, k):
        self.k=k
        self.heap=[]

    def add(self, x, label):
        x=-x
        heapq.heappush(self.heap,(x, label))
        if(len(self.heap)>self.k):
            heapq.heappop(self.heap)
    
    def get(self):
        return sorted(list(map(lambda  x: (-x[0],x[1]),self.heap)))
    
    def __str__(self):
        return ','.join(map(str,self.get()))


k = 3

OUTPUT_DIR = 'output_knn'
with open('test.csv') as f:
    
    for line in f.readlines():
        output_heap = Heap(k)
        status = subprocess.call("hdfs dfs -test -d "+OUTPUT_DIR,shell=True)
        if status == 0:subprocess.call("hdfs dfs -rm -r "+OUTPUT_DIR,shell=True)

        if(local==False):
            command_string = "hadoop jar /home/ayushjain1144/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-*.jar "\
            f"-input input_knn -output {OUTPUT_DIR} "\
            f"-mapper \"mapper.py {' '.join(line.split(',')[:-1])}\" " \
            f"-reducer \"reducer.py {k}\" "\
            "-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/mapper.py "\
            "-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/reducer.py "
            output_command_string = f"hadoop fs -cat {OUTPUT_DIR}/part-00000"
        else:
            command_string = f"python3 ./mapper.py {' '.join(line.split(',')[:-1])} < train.csv | sort | python3 ./reducer.py {k} > output.txt"
            output_command_string = f"cat output.txt"

        input("running " + command_string)
        subprocess.call(command_string, shell=True)

        # Predicting the class label for a given test instance.
        proc = subprocess.Popen(output_command_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        encoded_out, encoded_err = proc.communicate()
        out = encoded_out.decode(encoding='utf-8')
        err = encoded_err.decode(encoding='utf-8')

        if err:
            print('INTERNAL ERROR WHILE RUNNING INPUT')
            print(err)
            sys.exit(1)

        # Remove extra line break.
        output_lines = out.split('\n')[:-1]

        for output_line in output_lines:
            output_label, output_distances = output_line.split('\t')
            output_label = int(output_label)

            output_distances = output_distances.split(',')
            for output_distance in output_distances:
                output_distance = float(output_distance)
                output_heap.add(output_distance, output_label)

        frequency = [0]*7
        for distance,label in output_heap.get():
            frequency[label-1]+=1

        print(max(enumerate(frequency),key=lambda x:x[-1])[0]+1, line.split(',')[-1])
