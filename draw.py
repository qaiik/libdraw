from tkinter import *
import sys

def print_at(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
  print('Not yet')

if sys.argv[1] == '-t' or sys.argv[1] == '-term':
  if sys.argv[2] == 'at':
    c = sys.argv[3].split(',')
    text = ''.join(sys.argv[4:])
    print_at(c[0], c[1], text)

if sys.argv[1] == '-w' or sys.argv[1] == '-window':
  root = Tk()

  a = Label(root)
  root.geometry(sys.argv[2].replace('-b',''))
  root.title('')
  a.pack()
  root.mainloop()

