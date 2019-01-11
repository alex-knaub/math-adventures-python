from turtle import *

speed(5)

def square(length):
  for i in range(4):
    forward(length)
    right(90)

def triangle(sidelength=100):
  for i in range(3):
    forward(sidelength)
    right(120)

def star(sidelength=100):
  for i in range(5):
    forward(sidelength)
    right(145)


def doit():
  len = 5
  for i in range(60):
      right(5)
      len += 5
      star(len)

doit()
# if __name__ == '__main__':
#   try:
#     star()

#   except BaseException:
#     import sys
#     print(sys.exc_info()[0])
#     import traceback
#     print(traceback.format_exc())
#   finally:
#     print("Press Enter to continue ...")
#     input()
