# From Naftuly Kay - Mock
# Link: https://www.toptal.com/python/an-introduction-to-mocking-in-python

# refactoring with mock ---------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Mock_Ex_1 import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('Mock_Ex_1.os')
    @mock.patch('Mock_Ex_1.os.path')

    def test_rm(self, mock_os, mock_path):

        # set up the mock
        mock_path.isfile.return_value = False
        
        rm("any path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        rm("any path")
        
        mock_os.remove.assert_called_with("any path")


