# -*- coding: utf-8 -*-

__author__ = 'mohsen'

import _mysql
import sys
from configs import data


# MYSQL DATABASE CHECK
def connect():

    try:
        con = _mysql.connect(data.HOST, data.USER_NAME, data.PASSWORD, data.DATA_BASE)

        con.query("SELECT VERSION()")
        result = con.use_result()

        print "SERVER : [OK] MySQL version: %s" % \
        result.fetch_row()[0]

    except _mysql.Error, e:

        print "SERVER : [ERROR] Error %d: %s" % (e.args[0], e.args[1])
        con = False
        sys.exit(1)

    finally:

        if con:
            con.close()


def select():

    con = _mysql.connect(data.HOST, data.USER_NAME, data.PASSWORD, data.DATA_BASE)

    con.query("SELECT * FROM opec_basket_price")
    result = con.use_result()
    print result.fetch_row()[0]