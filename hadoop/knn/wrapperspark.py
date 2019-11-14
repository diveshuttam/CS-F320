from mapper import line_mapper
from reducer import line_reduce
filepath="hdfs://localhost:9000/user/ayushjain1144/"
input_filepath=filepath+'input_knn'
output_filepath=filepath+'output_knn'

input_textfile=sc.textFile(input_filepath)
counts = input_textfile.flatMap(line_mapper).reduceByKey(line_reduce)
counts.saveAsTextFile(output_filepath)
