class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.age)

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.age)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age)
