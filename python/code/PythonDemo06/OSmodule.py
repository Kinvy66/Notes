import os

#1.name属性表示当前操作系统  nt----window, posix-----linux
print(os.name)


#2.获取当前操作系统的环境变量
print(os.environ)


#3.获取指定路径下的所有文件以及文件夹
print(os.listdir(r'E:\Code\PythonCode'))  #返回值是列表


#4.在当前目录下创建新的目录   md
#os.mkdir(r'E:\Code\PythonCode\aaa')


#5.删除指定目录
#os.rmdir(r'E:\Code\PythonCode\aaa')
#os.remove('hello.txt')  #删除指定文件 参数是文件路径


#6.重命名
#参数1：原名字  参数2：新名字
#os.rename(r'E:\Code\PythonCode\aaa',r'E:\Code\PythonCode\bbb')



#os.path
#查看当前的绝对路径
print(os.path.abspath('/aaa'))

#拼接路径
print(os.path.join(r'E:\Code\PythonCode','PythonDemo02'))  #E:\Code\PythonCode\PythonDemo02



#分隔路径【拆分路径】
print(os.path.split(r'E:\Code\PythonCode\PythonDemo02'))  #('E:\\Code\\PythonCode', 'PythonDemo02')  元组


#获取文件的扩展名
print(os.path.splitext(r'E:\Code\PythonCode\PythonDemo02\listDemo01.py'))  #('E:\\Code\\PythonCode\\PythonDemo02\\listDemo01', '.py')


#判断指定路径是否是文件夹
print(os.path.isdir(r'E:\Code\PythonCode\PythonDemo02'))


#判断指定路径是否为文件

print(os.path.isfile(r'E:\Code\PythonCode\PythonDemo02'))

#判断指定的路径是否存在
print(os.path.exists(r'E:\Code\PythonCode\PythonDemo02'))


#获取文件的大小,单位为字节
print(os.path.getsize(r'E:\Code\PythonCode\PythonDemo02'))

#当前文件的上级路径
print(os.path.dirname(r'E:\Code\PythonCode\PythonDemo02\whileDemo01.py'))   #E:\Code\PythonCode\PythonDemo02

#获取当前文件
print(os.path.basename(r'E:\Code\PythonCode\PythonDemo02\whileDemo01.py'))  #whileDemo01.py













