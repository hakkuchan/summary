""" · 类(class)：体现了面向对象的编程思想，类封装了对象的属性和方法
      基于类创建的对象(也称为实例化)都自动具备类的通用行为，再根据需要赋予每个对象独特的个性

    · 目录
    |
    |—— 1. 创建
    |
    |—— 2. 实例化
    |
    |—— 3. 继承
    |
    |—— 4. 多重继承
    |
    |—— 5. super()的作用
    |
    |—— 6. 限制访问
    |
    |—— 7. 动态扩充属性和方法
"""



""" 1. 创建
    · 一般形式
    class <类名>:  # 类名采用驼峰命名法 
        # 如需说明文档，编写规则与函数文档相同 
        def __init__(self, <参数表>):   # 属性函数，实例化时会自动调用该方法，把参数给对象赋值
            <代码段>        
        def <方法名>(self, <参数表>):    # 方法函数
            <代码段>
            
    · self的作用：
      在定义类时，第一个函数一般为属性函数，
      在属性函数中传入的参数（param1 param2等）被分别赋值给 self.param1 self.param2 等
      在之后的方法函数定义中，传入的第一个参数一般都为 self，进而在方法函数中可以直接调用 self.param1 self.param2 等
"""

# 例：Car类
class Car:  
    
    # 属性函数
    def __init__(self, maker, model, year): # __init__()初始化函数的作用是初始化属性 maker、model、year
        self.maker = maker  # self.maker是实参，maker是形参，传入之后方法函数的参数是self.maker
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    # 方法一（描述汽车基本参数）
    def describe_car(self):
        print(str(self.year) + ' -- ' + str(self.maker) + ' -- ' + str(self.model))
    
    # 方法二（读里程表）
    def read_odometer(self):
        print('The car has ' + str(self.odometer_reading) + ' km on it.')
    
    # 方法三（更新里程表）
    def update_odometer(self, mileage): # 通过方法修改属性，给 mileage 赋值后，self.odometer_reading就会从0变成新赋的值。
        self.odometer_reading = mileage


        

""" 2. 实例化
    · 一般形式：obj = <类名>(<参数表>)
    
    · 调用类中的方法：obj.<方法名>() 
"""
    
# 例：实例化（实例名一般用小写字母）
car1 = Car('Audi', 'r8', '2018')   # 创建实例 1
car1.describe_car()  # >>> 2018 -- Audi -- r8

car2 = Car('Benz', 'c300', '2010') # 创建实例 2
car2.describe_car()   # >>> 2010 -- Benz -- c300
car2.read_odometer()  # >>> The car has 0 km on it.
car2.update_odometer(1500)  # 把 self.odometer_reading 修改为 1500
car2.read_odometer()  # >>> The car has 15000 km on it.



""" 3. 继承
    
    · 一个类（也称子类、派生类）继承另一个类（也称：父类、基类、超类）时，
      子类自动拥有父类的属性和方法，
      在此基础上还能改写旧对象、增加新对象
    
    · 继承方法: class <子类名>(<父类名>)
"""

# 例：继承Car类并增加方法 —— 显示剩余电量
class ElecCar(Car):
    def show_battery(self, batt):
        self.battery = batt
        print('Battery remain: '+ str(self.battery) + ' %')

elec_car = ElecCar('Tesla', 'model 3', '2018')
elec_car.describe_car()   # >>> 2018 -- Audi -- model 3
elec_car.read_odometer()  # >>> The car has 0 km on it.
elec_car.show_battery(50) # >>> Battery remain: 50%



""" 4. 多重继承

    · 在设计类的时候，可通过多重继承组合多个功能，避免设计多层次的继承关系 
    
    · 多重继承方法: class <子类名>(<父类1名>, <父类2名>, ...)
"""
class Car:
    def __init__(self, car_type):
        self.car_type = car_type
    def show_car(self):
        print('This is a(n) %s, ' %self.car_type, end='')
        
class Electric:
    def show_power(self):
        print('which is electric-power.')
        
class Gasoline:
    def show_power(self):
        print('which is gasoline-power.')

        
# 例 1：多重继承 Car 和 Electric 类
class NewCar(Car, Electric):
    pass
s1 = NewCar('jeep')
s1.show_car()
s1.show_power()

# 例 2：多重继承 Car 和 Gasoline 类
class NewCar(Car, Gasoline):
    pass
s2 = NewCar('bus')
s2.show_car()
s2.show_power()



""" 5. super()的作用：调用父类的属性、方法 """

''' (1) 当子类继承父类时，如果要使用父类的属性，并增加新属性，需用 super() 调用父类的初始化方法 '''
class ReadOdometer:
    def __init__(self, odometer):
        self.odometer = odometer
    def show_odometer(self):
        print('This car has %i km on it.' %self.odometer)

class UpdateOdometer(ReadOdometer):
    def __init__(self, odometer, new_odometer):
        super().__init__(odometer) # 调用父类的初始化方法 
        self.new_odometer = new_odometer
    def plus_odometer(self):
        print('This car added %i km on it.' %(self.new_odometer - self.odometer))

odometer = UpdateOdometer(1000, 1200)
odometer.plus_odometer()


''' (2) 当子类继承父类时，如果子类方法与父类方法重名，子类方法会覆盖后者，需用 super() 调用父类的方法'''
class Car:
    def __init__(self, maker):
        self.maker = maker
    def show_info(self):
        print('This is a %s car.' %self.maker, end=' ')

# a. 子类 ElectricCar 的方法 show_info 与其继承的、父类的方法同名
class ElectricCar(Car):
    def show_info(self):
        print('This car is electric-power.')

mycar = ElectricCar('BYD')
mycar.show_info()  # 父类的 show_info 被覆盖  >>> This car is electric-power.

# b. 重写子类 ElectricCar，利用 super() 调用父类的 show_info 方法
class ElectricCar(Car):
    def show_info(self):
        super().show_info() # 调用父类的方法 
        print('This car is electric-power.')
        
mycar = ElectricCar('BYD')
mycar.show_info()  # >>> This is a BYD car. This car is electric-power.



""" 6. 限制访问：禁止属性被修改 """

''' 示例：修改实例的属性 '''
class Car:  
    def __init__(self, maker):  # 属性
        self.maker = maker
    def describe_car(self):  # 方法：描述汽车基本参数
        print('My car is made by %s.' %str(self.maker))

mycar = Car('BYD')
mycar.describe_car()  # >>> My car is made by BYD.
# 修改属性
mycar.maker = 'Audi'
mycar.describe_car()  # >>> My car is made by Audi.


''' 如果不让属性被修改(限制访问)，可以把属性的名称前加上两个下划线__ '''
class Car:  
    def __init__(self, maker):  # 属性
        self.__maker = maker
    def describe_car(self):  # 方法：描述汽车基本参数
        print('My car is made by %s.' %str(self.__maker))

mycar = Car('BYD')
mycar.describe_car()  # >>> My car is made by BYD.
# 此时无法修改属性
mycar.__maker = 'Audi'
mycar.describe_car()  # >>> My car is made by BYD.



""" 7. 动态扩充属性和方法 """

class Car:
    pass

''' (1) 给实例扩充属性和方法 '''

car1 = Car()

# 动态给实例扩充属性
car1.maker = 'BYD'
print(car1.maker)

# 动态给实例扩充方法
def set_model(self, model): # 定义一个函数作为实例方法
    self.model = model

from types import MethodType
car1.set_model = MethodType(set_model, car1) # 给实例扩充方法
car1.set_model('Han') # 调用实例方法
print(car1.model)

# 其它实例不能调用上述实例扩充的属性和方法
car2 = Car()   # 创建新的实例
car2.set_model('Qin') # >>> 'Car' object has no attribute 'set_model'


''' (2) 给类扩充属性和方法 '''

# 为了给所有实例都扩充方法，可以给 class 扩充属性或方法
Car.set_model = set_model
car3 = Car() # 创建新的实例
car3.set_model('Qin')
print(car3.model)


''' (3) 限制实例可扩充的属性 '''
class Car:
    __slots__ = ('maker')  # __slots__方法用于指定可扩充的属性

car = Car()
car.maker = 'Audi'
print(car.maker)
car.model = 'A6' # 'model'不在slots方法中，不可扩充 >>> 'Car' object has no attribute 'model'
