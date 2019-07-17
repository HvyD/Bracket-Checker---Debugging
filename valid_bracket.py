#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
#HvyD made this!

import unittest

def is_valid(code):
    openers_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    openers = set(openers_closers.keys())
    closers = set(openers_closers.values())

    openers_check = []
    for char in code:
        if char in openers:
            openers_check.append(char)
        elif char in closers:
            if not openers_check:
                return False
            else:
                last_unclosed_opener = openers_check.pop()
                if not openers_closers[last_unclosed_opener] == char:
                    return False

    return openers_check == []

