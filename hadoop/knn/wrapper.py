#!/usr/bin/env python
import subprocess

OUTPUT_DIR = 'output_knn'
status = subprocess.call("hdfs dfs -test -d "+OUTPUT_DIR,shell=True)
if status == 0:subprocess.call("hdfs dfs -rm -r "+OUTPUT_DIR,shell=True)

with open('test.csv') as f:
    for line in f.readlines():
        command_string = "hadoop jar /home/ayushjain1144/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-*.jar "\
        "-input input_knn/ -output output_knn/ "\
		f"-mapper \"mapper.py {' '.join(line.split(',')[:-1])}\" " \
		"-reducer \"reducer.py 3\" "\
		"-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/mapper.py "\
		"-file /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/reducer.py "
        cstring = "hadoop jar /home/ayushjain1144/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-*.jar "\
        "-input input_knn/ -output output_knn/ "\
		"-mapper /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/mapper1.py " \
		"-reducer /home/ayushjain1144/Desktop/fods/fods/hadoop/knn/reducer1.py "
        input("running " + command_string)
        subprocess.call(command_string, shell=True)
        print()
