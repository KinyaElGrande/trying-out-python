class Employee:
 #class variable
    raise_amount =1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps +=1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    emp1 = Employee('Kinya', 'FRancis' ,63000)


    
