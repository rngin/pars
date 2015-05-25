# -*- coding: utf-8 -*-

__author__ = 'mohsen'

print "SERVER : [OK] starting server.."

from database import check

# check database connection
check.connect()

