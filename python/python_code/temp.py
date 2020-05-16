#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#author: kinvy
#file:   temp.py

class Cat:        #创建一个Cat类
  '''
  定义一个类
  '''
  #初始化对象
  def __init__(self,new_name,new_age):  #创建对像会自动调用,并且要把name和age这两个属性传入
    #print("---初始化---")
    self.name = new_name
    self.age = new_age



  #方法
  def eat(self): #方法必须写一个变量，可以不是self，但一般用self
      print("cat is eatting")

  def drink(self):
      print("cat is drinking")

  def introduce(self):
      print("%s的年龄是:%d"%(self.name,self.age))  #self.name表示调用对象的属性

#创建一个对象
#tom = Cat()
tom = Cat("汤姆",40)

#调用tom指向的对象中的方法
tom.eat()
tom.drink()

#给tom指向的对象添加2个属性
#tom.name = "汤姆"
#tom.age = 40

#获取属性的第一种方法
#print("%s的年龄是:%d"%(tom.name,tom.age))  #self.name表示调用对象的属性

#第二种方法
tom.introduce()


