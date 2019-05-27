# 练习：
# #   实现文件的复制(建议使用二进制方式进行操作)
# #   $ python3 mycp.py
# #     请输入源文件: ./src,txt
# #     请输入目标文件: ./mypass.txt
# #     提示: '文件复制成功' 或 '文件复制失败'
# #     (建议使用with语句打开文件)

def mycp():
    try:
        with open('src.txt', 'rb') as fr, open('mycp.txt', 'wb') as fw:
            while True:
                rb = fr.read(4096)
                if not rb:
                    break
                fw.write(rb)
    except:
        return False
    return True

def main():
    if mycp():
        print('文件复制成功')
    else:
        print('文件复制失败')

main()

