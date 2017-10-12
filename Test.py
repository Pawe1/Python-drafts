import sys

import ctypes  # An included library with Python install.

import ipgetter

def Mbox(title, text, style):
##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
    sys.stdout.write("TEST TEST")

def main():
    Mbox('Your title', 'Your text', 1)

myIP = ipgetter.myip()
Mbox('Tadaaaaa', 'Totalny SUKCES, %s' % myIP, 1)
