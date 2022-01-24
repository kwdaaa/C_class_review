class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 60:
            return 1500
        else:
            return 1200


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())
