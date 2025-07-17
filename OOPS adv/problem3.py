# Create a class ‘Employee’ and add salary and increment properties to it.

# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


class Employee:
    salary = 222
    increament = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increament/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increament = ((salary/self.salary) - 1)*100

o = Employee()
print(f"The salary is {o.salary} and increament is {o.increament}")
print(f"Salary after increament {o.salaryAfterIncrement}")
print(o.increament)