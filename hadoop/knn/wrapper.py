import subprocess

with open('test.csv') as f:
    for line in f.readlines():
        cmd = './mapper.py '+' '.join(line.split(',')[:-1])+' < train.csv | sort | ./reducer.py 3'
        input("running " + cmd)
        subprocess.call(cmd, shell=True)
        print()