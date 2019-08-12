class Employee():

    num_employee = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay


        Employee.num_employee += 1

    def raise_pay(self):
        self.pay = self.pay * self.raise_amt

    @classmethod
    def string_to_emp(cls, emp_info):

        first, last, pay = emp_info.split('-')
        return cls(first, last, float(pay))

    def __add__(self, other):
        if isinstance(self,Employee):
            if isinstance(other,Employee):
                return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return len(self.first) + len(self.last)

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last  = last


    @fullname.deleter
    def fullname(self):
        print('Delete successfully')
        self.first = None
        self.last  = None

class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        Developer.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay, employee = None):
        super().__init__(first,last,pay)

        if employee is None:
            employee = []
        else:
            self.employee = employee

    def add_emp(self, dev):

        if dev not in self.employee:
            self.employee.append(dev)
        else:
            print(dev.first," is under the control of {}".format(self.first))

    def rm_emp(self, dev):

        if dev in self.employee:
            self.employee.remove(dev)
            print('Remove successfully')
        else:
            print(dev.first," is not under the control of {}".format(self.first))

    def print_emp(self):
        for dev in self.employee:
            print(' -> ',dev.first)






def main():
    # emp1 = Employee('Andrew','Li',100000.)
    emp2 = Employee('Billy','He',10000.)
    emp3 = Employee.string_to_emp('Sherry-Zuo-10000')

    dev1 = Developer('Neil','Zhong',100000,'Python')
    dev2 = Developer('Billy', 'He', 10000.,'C++')

    mgr1 = Manager('Andrew','Li',100000.,[dev1])


    # mgr1.add_emp(dev2)
    # mgr1.print_emp()
    # mgr1.rm_emp(dev2)
    # mgr1.print_emp()
    # mgr1.rm_emp(emp3)
    # mgr1.add_emp(emp3)
    # mgr1.print_emp()
    #
    # print(len(mgr1))


    print(mgr1.email)
    print(mgr1.fullname)
    mgr1.fullname = "Longxin Li"
    print(mgr1.fullname)
    del(mgr1.fullname)
    print(mgr1.fullname)


   # print(emp1.pay)
   # print(emp2.pay)
   # emp1.raise_amt = 1.05
   # emp1.raise_pay()
   # emp2.raise_pay()
   # print(emp1.pay)
   # print(emp2.pay)
   # print(Employee.num_employee)


if __name__ == "__main__":
    main()
