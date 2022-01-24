class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 15:
            return 1000
        elif 20 <= self.age < 60:
            return 1500
        else:
            return 1200

    def info_csv(self):
        full_name = self.full_name()
        age = str(self.age)
        indent = f"{full_name.ljust(18)}{age.ljust(5)}{self.entry_fee()}"
        return indent


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())
