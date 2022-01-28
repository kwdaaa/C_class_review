# class「Customer」を定義。
class Customer:
    # 「__init__」はクラスをインスタンス化（実体化）するもの。
    def __init__(self, first_name, family_name):
        # 第1引数に入ってきたもの（first_name）を変数「self.first_name」に定義する。
        self.first_name = first_name
        # 第2引数に入ってきたもの（family_name）を変数「self.family_name」に定義する。
        self.family_name = family_name

    # 関数「full_name()」を定義。
    def full_name(self):
        # 変数「self.first_name」と変数「self.family_name」を出力。
        return f"{self.first_name} {self.family_name}"


# 変数「ken」にクラス「Customer」を定義。第１引数の中身を「"Ken"」、第２引数に「"Tanaka"」
ken = Customer(first_name="Ken", family_name="Tanaka")
# クラス「Customer」の関数「full_name()」を出力。
print(ken.full_name())

# 変数「tom」にクラス「Customer」を定義。第１引数の中身を「"Tom"」、第２引数に「"Ford"」
tom = Customer(first_name="Tom", family_name="Ford")
# クラス「Customer」の関数「full_name()」を出力。
print(tom.full_name())
