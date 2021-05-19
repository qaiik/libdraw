from tkinter import *
import sys

def print_at(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

if sys.argv[0] == '-h' or sys.argv[0] == '--help':
  print('Not yet')

if sys.argv[0] == '-t' or sys.argv[0] == '-term':
  if sys.argv[1] == 'at':
    c = sys.argv[2].split(',')
    text = ''.join(sys.argv[3:])
    print_at(c[0], c[1], text)

if sys.argv[0] == '-w' or sys.argv[0] == '-window':
  root = Tk()

  a = Label(root)
  root.geometry(sys.argv[2].replace('-b',''))
  root.title('')
  a.pack()
  root.mainloop()

