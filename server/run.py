# -*- coding: utf-8 -*-

__author__ = 'mohsen'

print "starting server.."

import _mysql
import sys
from configs import data


# MYSQL DATABASE CHECK
try:
    con = _mysql.connect(data.HOST, data.USER_NAME, data.PASSWORD, data.DATA_BASE)

    con.query("SELECT VERSION()")
    result = con.use_result()


    print "[OK] MySQL version: %s" % \
        result.fetch_row()[0]

except _mysql.Error, e:

    print "[ERROR] Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()