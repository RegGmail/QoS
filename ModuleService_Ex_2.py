# file removal as a service with python~s mock patch  --------------
# From Naftuli Kay - Mock
# Link: https://www.toptal.com/python/an-introduction-to-mocking-in-python


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)
