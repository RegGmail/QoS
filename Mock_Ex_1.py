# From Naftuly Kay - Mock
# Link: https://www.toptal.com/python/an-introduction-to-mocking-in-python

# a simple delete function --------------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

