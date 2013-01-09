#!/bin/env python

import datetime
import os
import re
import sys

rep_disallowed = re.compile('[\.\\\/\]\[\(\)?><:\'";,-=+_| ]+')

today = datetime.datetime.today()


def get_filename(title):
  date = today.strftime('%Y-%m-%d')
  title = title.lower()
  title = rep_disallowed.sub('-', title)
  return "content/posts/%s-%s.md" % (date, title)


def get_template_date():
  return today.strftime('%Y-%m-%d %H:%M')


template = """
Title: {title}
Date: {date}
Tags: tag1, tag2
Summary: [TODO]

Text.

Table of contents:

1. [Item 1](#item-1)
1. [Item two!](#item-two)
    1. [Sub-item one](#sub-item-one)
    1. [sub-item 2](#sub-item-2)

1. [Item 3?](#item-3)

## Item 1

## Item two!

### Sub-item one

### Sub-item 2

## Item 3?

"""

if __name__ == '__main__':
    title = " ".join(sys.argv[1:])
    if len(title) < 2:
      sys.exit("Title too short")

    filename = get_filename(title)
    template_date = get_template_date()
    # Only create the file if it doesn't exist.
    if not os.path.exists(filename):
      with file(filename, 'w') as f:
        f.write(template.format(
          title=title,
          date=template_date).strip() + '\n\n')
    # Then edit it.
    os.system('vim ' + filename)
