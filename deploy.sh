#!/bin/bash
/usr/local/bin/pipenv run make html
# This must run as the `uplift` user, so as not to require sudo
chown -R uplift:www-data output/
