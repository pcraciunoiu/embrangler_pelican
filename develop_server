#!/usr/bin/env bash
##
# This section should match your Makefile
##
PELICAN=pelican
PELICANOPTS="--port 8002 --debug --autoreload"

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

###
# Don't change stuff below here unless you are sure
###

function start_up(){
  echo "Starting up Pelican..."
  echo $PELICAN --listen --output "$OUTPUTDIR" --settings "$CONFFILE" $PELICANOPTS "$INPUTDIR"
  poetry run $PELICAN --listen --output "$OUTPUTDIR" --settings "$CONFFILE" $PELICANOPTS "$INPUTDIR"
}

###
#  MAIN
###
start_up
