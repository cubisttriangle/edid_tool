#!/usr/bin/python

import sys

from modules.Edid import Edid

if __name__=='__main__':

    edid = Edid()

    edid.load_from_file( sys.argv[1] )

    print( edid.info() )
