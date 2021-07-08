#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        if line.endswith('\n'):
            line = line[:-1]
        elems = line.split('LL->HOST EVT ')
        if len(elems) == 2:
            print('#' + elems[0] + '\\')
            print('04:' + elems[1])
            continue
        elems = line.split('HOST->LL CMD ')
        if len(elems) == 2:
            print('#' + elems[0] + '\\')
            print('01:' + elems[1])
            continue
        print('#' + line)
