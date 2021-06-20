from typing import Text

##用于生成sql脚本
f = open("out.txt")# 格式：text1@@text2@@text3
f2 = open("test.session.sql","w")
line = f.readline()
while line:
    arr = line.replace("\n","").split('@@')
    f2.write("insert into test values ('"+arr[0]+"','"+arr[1]+"','"+arr[2]+"');\n")
    line = f.readline()
print("写入完成")
f.close()
f2.close()
