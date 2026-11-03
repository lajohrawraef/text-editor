# console module
# it's purpose is to be an interface to work with the console input/output
# the abstraction should provide a connection to carry over read text into graphical output

# yes, I keep refering to these as "classes" even though they are modules

# in proper gui module, this should initialise the main window
def Initialise():
  print("Hello Console")

def Terminate():
  print("Bye Console")

class Console:
  def CheckCommand():
    pass

  def WriteHelpList():
    print('command list:')
    print('- help')
    print('- quit')
    print('- open')
    print('- close')

  def Main():
    i = True

    while i == True:
      a = input()

      match a:
        case 'help': Console.WriteHelpList()
        case 'quit': i = False
        case 'open': pass
        case 'close': pass
        case _: print('Unknown command')
