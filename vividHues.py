import os
os.system("") #allows colours to be displayed in the console

class Clr:
  BLACK = "\033[30m"
  RED = "\033[31m"
  GREEN = "\033[32m"
  YELLOW = "\033[33m"
  BLUE = "\033[34m"
  MAGENTA = "\033[35m"
  CYAN = "\033[36m"
  WHITE = "\033[37m"
  UNDERLINE = "\033[4m"
  RESET = "\033[0m"

def intro():
  print(Clr.RED, "Hi there!", Clr.RESET)
  print(Clr.UNDERLINE, "How are you?", Clr.RESET)
  print(Clr.CYAN, "Python", Clr.YELLOW, "is great!", Clr.RESET)