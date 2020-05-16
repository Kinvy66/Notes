#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#author: kinvy
#file: home.py
#note: 对象里调用对象的示例


class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area #定义和初始化一个属性值
        self.contain_item = []

    def __str__(self):
        return "房子的面积是:%d,可用的面积是:%d,户型是:%s,地址是:%s，房子里有:%s"%(self.area,self.left_area,self.info,self.addr,str(self.contain_item))

    def add_item(self,item):
        #self.left_area -= item.area  #获取到bed的属性
        #self.contain_item.append(item.naem)

        #第二种方法，配合bed中的方法使用
         self.left_area -= item.get_area()  #通过方法获取到bed的属性
         self.contain_item.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_area):
        self.naem = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是:%d"%(self.naem,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.naem



fangzi = Home(126,"三室一厅","北京 朝阳区 长安街 113号")  #创建一个对象
print(fangzi)   #打印对象

bed1 = Bed("席梦思",4) #创建一个对象
print(bed1)


fangzi.add_item(bed1)  #将bed的对象放到房子对象中
print(fangzi)







