# From Naftuly Kay - Mock
# Link: https://www.toptal.com/python/an-introduction-to-mocking-in-python
#Test case - without mock ------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Mock_Ex_1 import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            string = "Delete me!"
            encoded_string = bytes(string, 'utf-8')
            print(encoded_string)
            f.write(encoded_string)
    
    def test_rm(self):
        # remove the file
        print ("----> arquivo")
        print (self.tmpfilepath)

        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")
