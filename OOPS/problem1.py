# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer():
    company = "Microsoft"

    def __init__(self, name, lang, salary):
        self.name = name
        self.lang = lang
        self.salary = salary

p = Programmer("Hasan", "python", 120000)
print(p.name, p.lang, p.salary)

p = Programmer("Aiman", "Java", 140000)
print(p.name, p.lang, p.salary)

p = Programmer("Aqib", "JavaScript", 220000)
print(p.name, p.lang, p.salary)

