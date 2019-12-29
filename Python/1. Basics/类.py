""" 1. 类概述
    
    · 类（class）体现了面向对象的编程思想，
      类封装了对象的属性和方法

    · 基于类创建对象，也称为实例化，
      创建对象都自动具备类的通用行为，
      再根据需要赋予每个对象独特的个性
    
    · 定义的类不能直接操作，必须先实例化再操作
"""



""" 2. 创建类 

    · 一般形式
    
    class <类名>:  # 类名采用驼峰命名法 
        # 如需说明文档，编写规则与函数文档相同 
        def __init__(self, <参数表>):  # 属性函数，实例化时会自动调用该方法，把参数给对象赋值
            <代码段>        
        def <方法名>(self, <参数表>):   # 方法函数
            <代码段>


    · self的作用：
      
      在类定义中，所有函数的首个参数一般都是 self
      其作用是：实例化时传入的所有数据都赋给 self 变量
"""

# 例：Car类
class Car():  
   
    # 属性函数
    def __init__(self, maker, model, year): # __init__()初始化函数的作用是初始化属性 maker、model、year
        self.maker = maker  # self.maker是实参，maker是形参，传递进后面方法函数的参数是self.maker
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    # 方法一（描述汽车参数）
    def describe_car(self):
        print(str(self.year) + ' -- ' + str(self.maker) + ' -- ' + str(self.model))
    
    # 方法二（读里程表）
    def read_odometer(self):
        print('The car has ' + str(self.odometer_reading) + ' km on it.')
    
    # 方法三（更新里程表）
    def update_odometer(self, mileage): # 通过方法修改属性，给 mileage 赋值后，self.odometer_reading就会从0变成新赋的值。
        self.odometer_reading = mileage

        

""" 3. 调用类（创建实例、实例化）

    · 一般形式：obj = <类名>(<参数表>)
    
    · obj.<方法名>() 调用类中的方法
"""
    
# 例：实例化（实例名一般用小写字母）
car1 = Car('Audi', 'r8', '2018')   # 创建示例 1
car2 = Car('Benz', 'c300', '2010') # 创建示例 2

car1.describe_car()  # >>> 2018 -- Audi -- r8
car2.describe_car()  # >>> 2010 -- Benz -- c300

car1.read_odometer()  # >>> The car has 0 km on it.
car2.update_odometer(1500)  # 给 self.odometer_reading 赋值 1500
car2.read_odometer()  # >>> The car has 15000 km on it.



""" 4. 类的继承
    
    · 一个类（也称子类、派生类）继承另一个类（也称：父类、基类、超类）时，
      子类自动拥有父类的属性和方法，
      在此基础上还能改写旧对象、增加新对象
    
    · 继承方法: class <子类名>(<父类名>)
    
    · 一般情况下，一个子类只有一个父类 
"""

# 例：继承
class ElecCar(Car):
    def show_battery(self, batt):
        self.battery = batt
        print('Battery remain: '+ str(self.battery) + ' %')

elec_car = ElecCar('Tesla', 'model 3', '2018')
elec_car.describe_car() 
elec_car.read_odometer() 
elec_car.show_battery(50)