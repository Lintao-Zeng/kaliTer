# coding=utf8
import sqlite3
import readline
import sys

def init():
    # 连接数据库(如果不存在则创建)
    global conn
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    # 创建游标
    global cursor
    cursor = conn.cursor()

def release():
    # 关闭游标
    cursor.close()
    # 提交事物
    conn.commit()
    # 关闭连接
    conn.close()
 
def repeat(id):
    cursor.execute("select question from test where rowid=" + str(id))
    question = cursor.fetchone()[0]
    print(str(id) + "、" + str(question))

    cursor.execute("select answer from test where rowid=" + str(id))
    answer = cursor.fetchone()[0]
    repeatInput(id,answer)

def repeatInput(id,answer):
    answerIn = raw_input('answer: ')
    if answerIn == answer:
        # 打印附带内容
        cursor.execute("select content from test where rowid=" + str(id))
        print("content: "+cursor.fetchone()[0]+"\r\n")

        # 获取数据库总行数
        cursor.execute("select count(*) from test")
        if id != cursor.fetchone()[0]:
            id = id + 1
            repeat(id)
        else:
            id = 1
            repeat(id)
    elif answerIn == "show":
        # 打印answer
        cursor.execute("select answer from test where rowid=" + str(id))
        print("answer: "+cursor.fetchone()[0])
        repeatInput(id,answer)
    elif answerIn == "exit":
        sys.exit()
    else:
        print("try again!")
        repeatInput(id,answer)

    
def main():
    init()
    global id
    global index
    cursor.execute("select count(*) from test")
    index = cursor.fetchone()[0]
    print('总题数：' + str(index))
    while True:
        sid=raw_input('请输入id：')
        try:
            x=eval(sid)
            if type(x) == int and x <= index and x > 0:
                break
            elif sid == "exit":
                sys.exit()
            else:
                print('id输入超出范围或者小于等于0')
        except:
            if sid == "exit":
                sys.exit()
            else:
                print('id输入非数字')
                pass
    id = int(sid)
    repeat(id)
    release()

if __name__ == "__main__":
    main()
