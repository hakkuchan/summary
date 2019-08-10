"""
类：
    (1) 类（class）表现的是现实世界中的事物和情景;
    (2) 编写class时，定义了一大类对象都具备的通用行为：属性和方法;
    (3) 基于类创建对象，也称为实例化，每个对象都自动具备这种通用行为，再根据需要赋予每个对象独特的个性。
    (4) 写好的类不能直接操作，必须先实例化再操作
"""

""" 创建类（以Car为例）"""
class Car():  # 驼峰命名法   
    
    ''' 说明文档（编写规则与函数文档相同）'''
    
    ''' 属性函数 '''
    def __init__(self, maker, model, year): # __init__()初始化函数的作用是初始化属性 maker、model、year
        self.maker = maker  # self.maker是实参，maker是形参，传递进后面方法函数的参数是self.maker
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    ''' 方法函数 1（描述汽车参数） '''
    def describe_car(self):
        print(str(self.year) + ' -- ' + str(self.maker) + ' -- ' + str(self.model))
    
    ''' 方法函数 2（读里程表） '''
    def read_odometer(self):
        print('The car has ' + str(self.odometer_reading) + ' miles on it.')
    
    ''' 方法函数 3（更新里程表） '''
    def update_odometer(self, mileage): # 通过方法修改属性，给 mileage 赋值后，self.odometer_reading就会从0变成新赋的值。
        self.odometer_reading = mileage


""" 创建（多个）实例 """
# 实例名称一般用小写字母
new_car = Car('Audi', 'r8', '2018') # 创建示例 1
old_car = Car('Benz', 'c300', '2010') # 创建示例 2
new_car.describe_car()
old_car.describe_car()
new_car.read_odometer()
old_car.update_odometer(15000)
old_car.read_odometer()


""" 
继承类:
    (1) 一个类（也称子类、派生类）继承另一个类（也称：父类、基类、超类）时，它将自动获得另一个类的所有属性和方法
    (2) 一般情况下，一个子类只有一个父类
    (3) 子类自动拥有父类的属性和方法，在此基础上还能改写旧对象、增加新对象
    (4) 继承方法: class 子类名(父类名)
"""
class ElectricCar(Car):
    def show_battery(self, batt):
        self.battery = batt
        print('Battery remain: '+ str(self.battery) + ' %')
your_new_car = ElectricCar('Tesla', 'model 3', '2018')
your_new_car.describe_car() 
your_new_car.read_odometer() 
your_new_car.show_battery(50)