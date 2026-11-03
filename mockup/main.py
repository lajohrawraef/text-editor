# please don't judge my bullshit code
# I barely know how to write in Python

# the main class will act as a bridge between the console and the editor
# essentially, it should be possible to swap the console class to a proper window gui
# and change the editor to work with different file formats

# hence, responsibility for file interactions are given to the editor class
# and responsibility for gui input/output is given to the console class

# should have some metadata
# should have stored text data
class File:
  # initialise the object
  # there are default values for each field
  def __init__(self, name: "Untitled", content: ""):
    self.__name = name
    self.__content = content
    pass

  def GetContent(self):
    self.__content

  def SetContent(self, content: ""):
    self.__content = content

  def GetName(self):
    return self.__name

  def SetName(self, name: "Untitled"):
    self.__name = name


class Editor: # associates File class objects # must be static with only one instance at all times
  __fileList = []
  __fileCurrent = -1 # placeholder pointer to currently active file
  __fileCount = 0 # placeholder pointer to count the number of opened files

  def Open(name):
    if name == Null:
      return

    # open and read file
    content = ""

    with open("test.txt") as f:
      content = f.read()

    Editor.__fileList[Editor.__fileCount] = File(name, content)
    Editor.__fileCount += 1
    Editor.__fileCurrent += 1
    pass

  # aka GetContent
  def Read():
    pass

  # aka SetContent
  def Write():
    pass

  def Open():
    pass


# should be able to handle inputs and outputs
# should be able to properly display everything
class UserInterface: # should be static, only one instance at all times
  def Initialise(): pass # abstract method for initialisation
  def Terminate(): pass # abstract method for termination

class Console(UserInterface):
  def Initialise():
    a = True
    print("Start")
    # initialise thread
    # the thread will have a terminating condition
    while a == True:
      # get event message (input)
      # compate it with known cases though switch/match
      # on each case, execute a different operation

      I = input() # GetInput()
      match I:
        case "help": # print a list of allowed commands
          print("HELP")
        case "quit": # terminate the loop via an external flag
          a = False
        case "list": # list currently open files
          # refers to the editor interface to get every file in the list
          pass
        case "open": # open another file
          # refers to the editor interface to open the file
          pass
        case "close": # close an open file
          # refers to the editor interface to close the file
          pass
        case "read": # print the contents of the file
          # refers to the editor interface to read the file
          # get string and output it
          pass
        case "write": # write to the file
          # refers to the editor interface to write to the file
          # get input and override the string
          pass
        case "append": # add new text to the file
          # refers to the editor interface to append the file
          # get string and continue writing from that point
          pass
        case _: # unknown command
          print("unknown command")

  def Terminate():
    print("End")
    # terminate thread

# import editor
# import console as ui

#######################################################################


# begin main

# initialise the window/user interface
Console.Initialise() # initialise thread

# start the main loop
# since it is a console application, the loop may be the ui thread itself
# while True:
  # listen for events
  # if no events, on its turn, execute code
  # exit main loop
  # pass

# terminate the window/user interface
Console.Terminate() # terminate thread

# end main

