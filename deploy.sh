#!/bin/bash
pipenv run make html
# TODO: figure out how to chown/fix post-deploy static issues
# sudo chown -R uplift:www-data output/
