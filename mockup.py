import editor

class Console:
  def ReadInput():
    pass

  def WriteOutput():
    pass

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

# Console.Main()
"""
B = 'Hello World!'

with open('test.txt') as f:
  A = f.read()
  print(A)

with open('test.txt', 'w') as f:
  f.write(B)
"""

editor.Editor.ReadFrom("test.txt")
print(editor.Editor.GetContents())
