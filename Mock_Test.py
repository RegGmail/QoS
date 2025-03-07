# mocked test case -------------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        """
        # set up the mock
        mock_path.isfile.return_value = False
        
        reference.rm("any_path")
        
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        """
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        reference.rm('any_path')
        
        mock_os.remove.assert_called_with('any_path')
        
