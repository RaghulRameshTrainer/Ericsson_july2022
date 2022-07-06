class Employee():
    hike=1.5
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@ericsson.com'

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def appraisal(self):
        #self.hike=hike
        self.salary=int(self.salary*self.hike)

    @classmethod
    def create_object(cls,emp_str):
        fn,ln,sal=emp_str.split(',')
        return cls(fn,ln,int(sal))

    @staticmethod
    def is_workingday(day):
        if day.weekday()==5 or day.weekday()==6:
            return "It is holiday"
        return "it is workingday"

class Developer():
    def __init__(self,fname,lname,pay,tech):
        self.fname = fname
        self.lname = lname
        self.salary = pay
        self.email = self.fname + '.' + self.lname + '@ericsson.com'
        self.tech=tech

    def fullname(self,title):
        self.title=title
        return f"{self.title} {self.fname} {self.lname}"

class Manager(Employee,Developer):
    def fullname(self,title):
        #return Developer.fullname(self,title)
        return super(Employee,self).fullname(title)

mgr_1=Manager('Ankit','Kumar',200000)
mgr_2=Manager('Apurba','Majumdar',300000)
# print(mgr_1.fullname('Mr'))
# print(mgr_2.fullname('Mr'))

import datetime
dt=datetime.date(2022,7,10)
print(Manager.is_workingday(dt))
















# dev_1=Developer('Siva','Murugan',100000,'Perl')
# dev_2=Developer('Ramya','Rajesh',200000,'Mainframe')
#
# print(dev_1.fullname('Mr'))
# print(dev_2.fullname('Miss'))
#
# print("Siva's salary:", dev_1.salary)
# dev_1.appraisal()
# print("Siva's new salary:", dev_1.salary)
#
# print("Ramya's salary:", dev_2.salary)
# dev_2.appraisal()
# print("Ramya's new salary:", dev_2.salary)

# str1="Raghul,Ramesh,50000"
# str2="Levin,Lenus,60000"
# import datetime
# dt=datetime.date(2022,7,11)
# print(Employee.is_workingday(dt))
#
# emp_1=Employee.create_object(str1)   #Employee('Raghul','Ramesh',50000)
# emp_2=Employee.create_object(str2)   #Employee('Levin','Lenus',60000)
#
# emp_1.hike=1.5
# print("Raghul's Current Salary:",emp_1.salary)
# emp_1.appraisal()
# print("Raghul's Revised Salary:",emp_1.salary)
#
# print("Levin's Current Salary:",emp_2.salary)
# emp_2.appraisal()
# print("Levin's Revised Salary:",emp_2.salary)


# Features
#Abstraction
#Inheritance
#Polymorphism
#Encapsulation