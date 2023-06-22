""" 
Determine the working platform
┍━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━┑
│ System              │ Value               │
┝━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━┥
│ Linux               │ linux or linux2 (*) │
│ Windows             │ win32               │
│ Windows/Cygwin      │ cygwin              │
│ Windows/MSYS2       │ msys                │
│ Mac OS X            │ darwin              │
│ OS/2                │ os2                 │
│ OS/2 EMX            │ os2emx              │
│ RiscOS              │ riscos              │
│ AtheOS              │ atheos              │
│ FreeBSD 7           │ freebsd7            │
│ FreeBSD 8           │ freebsd8            │
│ FreeBSD N           │ freebsdN            │
│ OpenBSD 6           │ openbsd6            │
│ AIX                 │ aix (**)            │
┕━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━┙
Author: Hao Chen (chen960216@gmail.com)
Created: 20230622osaka

Note:
- After Python3.9, sys.platform doesn’t contain the major version anymore. It is always 'linux', instead of 'linux2' or 'linux3' [2].

Reference
1. (Possible values from sys.platform?)[https://stackoverflow.com/questions/446209/possible-values-from-sys-platform]
2. (Python3.9 Document)[https://docs.python.org/3.9/library/sys.html#sys.platform]
"""
import sys


def detect_platform():
    platform = sys.platform

    if platform.startswith('win'):
        return "Windows"
    elif platform.startswith('darwin'):
        return "Mac OS"
    elif platform.startswith('linux'):
        return "Linux"
    elif platform.startswith('freebsd'):
        return "FreeBSD"
    else:
        return "Unknown"


if __name__ == '__main__':
    current_platform = detect_platform()
    print("Detected platform:", current_platform)
