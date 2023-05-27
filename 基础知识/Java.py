import sys
import os
filename = sys.argv[1]
print(filename)
if filename.split('.')[-1] == 'java':
    os.system(f"javac {filename}")
classname = filename.split('\\')[-1].split('.')[0]
classpath = filename.split(classname)[0]
os.system(f"java -cp {classpath} {classname}")
input("键入Enter退出...")


