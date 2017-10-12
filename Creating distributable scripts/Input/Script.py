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



myIP = ipgetter.myip()
Mbox('Tadaaaaa', 'Yout IP address is %s' % myIP, 0)
