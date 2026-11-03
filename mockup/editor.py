# editor module
# it will contain the basic implementation of the editor static class
# or whatever it is
# it should not have context over how its data is used in the program
# it shpuld only know how to read from files and shit

# this should create a file object that will store appropriate stuff

# create an instance of a file that will store retrieved data
# the file will have its own history object as well to store edit history
# this will allow the program to swap between multiple opened objects
# although I'm not sure how much it will cost in terms of dynamic memory
# this should problably store some things in cache

# from this, there should be pointers to determine open files and currently viewed file
# as well as some proper stuff to encapsulate it


class Editor:
  __contents = "" # the file contents

  def ReadFrom(name):
    with open(name, "rt") as f:
      Editor.__contents = f.read()

  def GetContents():
    return Editor.__contents

  def WriteTo(name):
    with open(name, "wt") as f:
      f.write(Editor.__contents)
