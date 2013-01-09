Title: Introducing Google App Engine Paginator
Date: 2012-08-29 11:24
Tags: appengine, python
Summary: Need for a generic paginator for large datasets? Look no further!

## Table of contents

* [Summary](#summary)
* [Getting Started](#getting-started)
* [Features](#features)


## Summary

Need a way to paginate through a GQL query easily? __gae_paginator__ handles the generation of next/previous page URLs, paginates on both unique and non-unique properties, and wants to be as efficient and easy to use as possible.

## Getting Started

1. Download [the source](https://github.com/humble/gae_paginator) and copy the `gae_paginator/` folder anywhere inside your App Engine project directory.

2. That's it! Use it like so, in your handlers:

		:::python
		import os
		  
		from google.appengine.ext.webapp import template
		import webapp2
		
		from gae_paginator import Paginator
		
		
		class YourHandler(webapp2.RequestHandler):
		
		  def get(self):
		  paginator = Paginator(YourModel, 'some_column = :1 AND other_column = :2',
		                        ['some_value', 'other_value'], expect_duplicates=True,
		                        per_page=50, paginate_on='-created')
		  page = paginator.get_page(request=self.request)
		  path = os.path.join(os.path.dirname(__file__), 'index.html')
		  self.response.out.write(template.render(path, {
		    'objects': list(page),
		    'page': page,
		  })

3. In your django template:

		:::python
		{% if page.has_previous %}
			<a href="{{ page.get_previous_url }}">&laquo; Previous page</a>
		{% endif %}
		{% if page.has_next %}
			<a href="{{ page.get_next_url }}">Next page &raquo;</a>
		{% endif %}

	Or jinja2 template:

		:::python
		{% if page.has_previous() %}
			 <a href="{{ page.get_previous_url() }}">&laquo; Previous page</a>
		{% endif %}
		{% if page.has_next() %}
			<a href="{{ page.get_next_url() }}">Next page &raquo;</a>
		{% endif %}


## Features

* Simple pagination by key
* Paginate by non-unique properties with a specified tolerance for duplicates.

  * Example: paginate songs by artist name, 10 songs per page, expect 100 duplicates. Set: `expect_duplicates=100`
* Order and paginate by a custom column (Date/DateTime and key supported and tested).
* Show next and previous buttons only when there is actual data before/after.

