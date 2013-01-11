#!/bin/bash
source `which virtualenvwrapper.sh`
workon embrangler.com
make html
deactivate
