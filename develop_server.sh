#!/usr/bin/env bash
##
# This section should match your Makefile
##
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

###
# Don't change stuff below here unless you are sure
###

function start_up(){
  echo "Starting up Pelican and SimpleHTTPServer"
  echo $PELICAN --debug --autoreload -r "$INPUTDIR" -o "$OUTPUTDIR" -s $CONFFILE $PELICANOPTS...
  $PELICAN --listen --debug --autoreload --output "$OUTPUTDIR" --settings "$CONFFILE" $PELICANOPTS "$INPUTDIR"
}

###
#  MAIN
###
start_up
