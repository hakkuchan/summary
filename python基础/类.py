"""
类（class）表现的是现实世界中的事物和情景
编写class时，定义了一大类对象都具备的通用行为（属性和方法）
基于类创建对象（实例化）时，每个对象都自动具备这种通用行为，再根据需要赋予每个对象独特的个性。
"""

""" 创建类（以Car为例）"""
class Car():  # 驼峰命名法
    
    """ 说明文档（编写规则与函数文档相同）"""

    def __init__(self, maker, model, year): # 初始化函数
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 给属性指定默认值
    def describe_car(self): # 方法函数（描述汽车参数）
        print(str(self.year) + ' -- ' + str(self.maker) + ' -- ' + str(self.model))
    def read_odometer(self): # 方法函数（读里程表）
        print('The car has ' + str(self.odometer_reading) + ' miles on it.')
    def update_odometer(self, mileage): # 方法函数（更新里程表）
        self.odometer_reading = mileage
"""
解析：
在这个类里面，__init__()初始化函数的作用是初始化属性maker、model、year。
实例化的时候，赋予对象的具体maker、model、year会传递给self.xxx参数。
记住：self.xxx 是实参，“=”后面是形参，也就是说，可以写成 self.brand = maker，传递进后面程序的参数是self.brand。
self.xxx实参随后带入方法函数，describe_car(self) 和 read_odomeer(self)。
可以通过方法修改属性，比如方法update_odometer(self, mileage)，给mileage赋值后，self.odometer_reading就会从0变成新赋的值。
注意：类不能直接操作，比如 Car.read_odometer()，会报错“read_odometer() missing 1 required positional argument: 'self'”，必须要先实例化再使用。
"""


""" 创建（多个）实例 """
# 实例名称一般用小写字母
my_new_car = Car('Audi', 'r8', '2018') # 创建示例1
old_car = Car('Benz', 'c300', '2010') # 创建示例2
my_new_car.describe_car()
old_car.describe_car()
my_new_car.read_odometer()
old_car.update_odometer(15000)
old_car.read_odometer()

""" 
继承类 
一个类（子类、派生类）继承另一个类（父类、基类、超类）时，它将自动获得另一个类的所有属性和方法
一般情况下，一个子类只有一个父类
子类自动拥有父类的属性和方法，在此基础上还能改写旧对象、增加新对象
继承方法 class 子类名(父类名)
"""
class ElectricCar(Car):
    def show_battery(self, batt):
        self.battery = batt
        print('Battery remain: '+ str(self.battery) + ' %')
your_new_car = ElectricCar('Tesla', 'model 3', '2018')
your_new_car.describe_car() 
your_new_car.read_odometer() 
your_new_car.show_battery(50) 