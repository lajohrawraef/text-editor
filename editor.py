# editor class file
# it will contain the basic implementation of the editor static class
# or whatever it is
# it should not have context over how its data is used in the program
# it shpuld only know how to read from files and shit

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
