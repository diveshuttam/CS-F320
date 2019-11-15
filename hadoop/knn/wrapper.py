import heapq
import subprocess
import sys


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
# status = subprocess.call("hdfs dfs -test -d "+OUTPUT_DIR,shell=True)
# if status == 0:subprocess.call("hdfs dfs -rm -r "+OUTPUT_DIR,shell=True)

with open('test.csv') as f:
    for line in f.readlines():
        output_heap = Heap(k)
        command_string = "hadoop jar /home/ayushjain1144/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-*.jar "\
        "-input input_knn/ -output output_knn/ "\
        f"-mapper \"mapper.py {' '.join(line.split(',')[:-1])}\" " \
        f"-reducer \"reducer.py {k}\" "\
        "-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/mapper.py "\
        "-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/reducer.py "

        command_string_local = f"python3.6 ./mapper.py {' '.join(line.split(',')[:-1])} < train.csv | sort | python3.6 ./reducer.py {k} > output.txt"
        command_string = f"hadoop fs -cat {OUTPUT_DIR}"
        input("running " + command_string_local)
        subprocess.call(command_string_local, shell=True)

        # Predicting the class label for a given test instance.
        output_command_local = 'cat output.txt'
        proc = subprocess.Popen(output_command_local, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        encoded_out, encoded_err = proc.communicate()
        out = encoded_out.decode(encoding='utf-8')
        err = encoded_err.decode(encoding='utf-8')

        if err:
            print('PREDICTION FAILED')
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
