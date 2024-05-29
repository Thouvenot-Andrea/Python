from Diamond.diamond import create_diamond


def test_diamond_b():
    assert create_diamond("B") == """\
 A
B B
 A"""


def test_diamond_c():
    assert create_diamond("C") == """\
  A
 B B
C   C
 B B
  A"""


def test_diamond_d():
    assert create_diamond("D") == """\
   A
  B B
 C   C
D     D
 C   C
  B B
   A"""


def test_diamond_a():
    assert create_diamond("A") == "A"


#     A
#    B B
#   C   C
#  D     D
# E       E
#  D     D
#   C   C
#    B B
#     A