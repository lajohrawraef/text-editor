what do I want

a simple text editor program that will be able to read and write text files
it doesn't have to be a window program, it may be done in a console
but a window application would be nice either way
still it would be better to focus on making it be able to run in a console or something


a text editing program

write to an existing file
read from an existing file
create a new file if none

display stored text

select a seciton of text
copy, paste

store action history
undo, redo






any classes? - no, not really, everything is done from a single entity
any data? - everything is stored as is, for now

goal
1. write, read, create file, by name and by directory
2. display stored text
3. select text, copy, paste
4. store history, undo, redo

for oop, actually, I think it would be quite helpful to have separate interfaces for each responsibility


for the basics:
- the "kernel" function - read, write, create
- the graphical function - display text, have buttons, possibly have some commands or input read

I would say, C++, preferably, but it would also be helpful to sketch it out in python
should I use Qt for this????
just focus on the console execution first




console development

there are two classes/objects
the console communicator
and the actual program

Console (class)
- can read input
- will send input to the editor to write to the file
- will request the editor to read text from file
- will write output

Editor (class)
- can read file
- can write to file
- can open file
- can send over text from file

the editor should attempt to open the file
then it should read all of the contents of the file into memory (or cache, or part of contents)
and store the contents for operation
on save, it should write all the text into the file












window development
- windows -> windows desktop environment
- linux -> linux desktop environment (X11 or Qt)

any threads or similar?


