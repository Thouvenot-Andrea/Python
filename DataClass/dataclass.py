from dataclasses import dataclass
from typing import ClassVar


@dataclass
class User:
    first_name: str
    last_name: str
    c: ClassVar[int]  # attribue de class avec ClassVar est specifier a l'intérieur des crochets le type de donné
#     pour mettre des valeur par défault il suffit de mettre a la fin = puis la valeur par défault

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"


patrick = User(first_name="Patrick", last_name="Uno")
print(patrick.first_name)
print(patrick.last_name)
print(patrick.__dict__)
print(patrick.full_name)

# remplace ce qui a en dessous la methode init


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


patrick = User(first_name="Patrick", last_name="Dos")

print(patrick.first_name, patrick.last_name)
