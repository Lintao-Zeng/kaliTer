from typing import Text

##用于合并两个txt文件
f = open("in.txt")
f2 = open("in2.txt")
f3 = open("test.session.sql","a")
line = f.readline()
line2 = f2.readline()
while line:
    f3.write(line.replace("\n","")+line2.replace("\n","")+"\n")
    line = f.readline()
print("写入完成")
f.close()
f3.close()
