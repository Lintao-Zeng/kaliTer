# coding=utf8
import sqlite3
import readline

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

        cursor.execute("select count(*) from test")
        if id != cursor.fetchone()[0]:
            id = id + 1
            repeat(id)
        else:
            id = 1
            repeat(id)
    else:
        print("try again!")
        repeatInput(id,answer)

    
def main():
    init()
    global id
    id = int(input('请输入id：'))
    repeat(id)
    release()


if __name__ == "__main__":
    main()