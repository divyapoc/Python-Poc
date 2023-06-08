# class Computer:
#     def __init__(self,brand,ram):  # init is a speacial method which will be called automatically
#         print("automatically called for each object")
#         self.brand = brand
#         self.ram = ram
#         print(brand,ram)
#     def func(self):
#         print("my computer config =",self.ram,self.brand)
#
# c1 = Computer('sony',6)  #object
# c2 = Computer('acer',4)
# c1.func()

#print(type(c1))  # we created this object


# d = "hello"
# print(type(d))  # bulit datatype
# Computer.func(c1)
# Computer.func(c2)

#inheritance
#
# class A:
#     def feature1(self):
#         print("have feature 1")
#     def feature2(self):
#         print("have feature 2")
#
# class B(A):     #child - it inherites from A and have feature of A
#     def feature3(self):
#         print("have feature 3 , featue 1 , feature2")
#
# a1 = A()
# b1 = B()
# a1.feature1()
# a1.feature2()
# b1.feature2()
# b1.feature3()

#multilevel inheritance
# class A:
#     def feature1(self):
#         print("have feature 1")
#     def feature2(self):
#         print("have feature 2")
#
# class B(A):     #child - it inherites from A and have feature of A
#     def feature3(self):
#         print(" have feature 3 , featue 1 , feature2")
#
# class C(B):  # like grandchild - it inherites from  B and B inherities from A so have features of A and B
#       def feature4(self):
#           print('feature from class A and A')
# a1 = A()
# b1 = B()
# c1 = C()
# c1.feature3()
# c1.feature2()
# c1.feature4()

#multiple inheritance

class A:
    def feature1(self):
        print("have feature 1")
    def feature2(self):
        print("have feature 2")

class B():    # only have feature 3
    def feature3(self):
        print(" have feature 3 ")

class C(B , A):  #  it inherites from both A and B
      def feature4(self):
          print('feature from class A and B')

a1 = A()
b1 = B()
c1 = C()
c1.feature2()
c1.feature4()
c1.feature3()