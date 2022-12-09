"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay=0, description="", contract_commission=None, bonus_commission=None):
        self.name = name
        self.description = description
        self.pay = 0
        self.contract_commission = contract_commission
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.pay
        
    def __str__(self):
        return f'{self.name} works on a {self.description}'

class SalaryEmployee(Employee):

    def __init__(self, name, salary, contract_commission=None, bonus_commission=None):
        super().__init__(name, contract_commission, bonus_commission)
        self.salary = salary
        self.pay = self.set_pay()
        self.description = self.set_contract_description()

    def set_pay(self):
        self.pay += self.salary

        if self.contract_commission:
            self.pay += self.contract_commission.get_total_contract_commission()

        elif self.bonus_commission:
            self.pay += self.bonus_commission.get_bonus_commission()


    def set_contract_description(self):
        desc = f'monthly salary of {self.salary}'

        if self.contract_commission:
            desc = desc + self.contract_commission.get_contract_commission_description()

        elif self.bonus_commission:
            desc = desc + self.contract_commission.get_bonus_commission_description()

        desc = desc + f'. Their total pay is {self.get_pay()}'
        self.description = desc


class HourlyEmployee(Employee):

    def __init__(self, name, hours, hourly_rate, contract_commission=None, bonus_commission=None):
        super().__init__(name, contract_commission, bonus_commission)
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.pay = self.set_pay()
        self.description = self.set_contract_description()

    def set_pay(self):
        self.pay = self.hourly_rate * self.hours

        if self.contract_commission:
            self.pay += self.contract_commission.get_total_contract_commission()
        
        elif self.bonus_commission:
            self.pay += self.bonus_commission.get_bonus_commission()

    def set_contract_description(self):

        desc = f'contract of {self.hours} at {self.hourly_rate}/hour'

        if self.contract_commission:
            desc = desc + self.contract_commission.get_contract_commission_description()

        elif self.bonus_commission:
            desc = desc + self.contract_commission.get_bonus_commission_description()

        desc = desc + f'. Their total pay is {self.get_pay()}'
        self.description = desc


class ContractCommission:
    
    def __init__(self, contract_commission, contract_count):
        self.contract_commission = contract_commission
        self.contract_count = contract_count

    def get_total_contract_commission(self):
        return self.contract_commission * self.contract_count

    def get_contract_commission_description(self):
        return f' and recives a commission for {self.contract_count} contract(s) at {self.contract_commission}/contract'

class BonusCommission:

    def __init__(self, bonus_commission):
        self.bonus_commission = bonus_commission

    def get_bonus_commission(self):
        return self.bonus_commission

    def get_bonus_commission_description(self):
        return f' and receives a bonus commission of {self.bonus_commission}'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', hours=100, hourly_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', salary=4000, contract_commission=ContractCommission(contract_commission=200, contract_count=4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', hours=150, hourly_rate=25, contract_commission=ContractCommission(contract_commission=220, contract_count=3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', salary=2000, bonus_commission=BonusCommission(bonus_commission=1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', hours=120, hourly_rate=30, bonus_commission=BonusCommission(bonus_commission=600))
