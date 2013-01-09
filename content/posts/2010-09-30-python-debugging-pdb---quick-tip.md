Title: Python debugging (pdb) - quick tip
Summary: Quick tip to help you keep track when debugging.
Tags: django, python, debugging

Sometimes you want to use multiple breakpoints like so:

	::python
	# some function/file...
	import pdb; pdb.set_trace()
	some_python_code_on_one_line()

	# some other function/file...
	import pdb; pdb.set_trace()
	some_other_python_code_on_one_line()

I personally get lost sometimes, tracking through many files and having to read the method name and remember where exactly it is. So it can help me keep track if I leave myself a message:

	::python
	# some function/file...
	import pdb; pdb.set_trace()
	s = 'Some function/file'
	some_python_code_on_one_line()

	# some other function/file...
	import pdb; pdb.set_trace()
	s = 'Some other function/file'
	some_other_python_code_on_one_line()

In some cases (when running django on my mac, for example), I can even do this:

	::python
	# some function/file...
	import pdb; pdb.set_trace()
	"""Some function/file"""
	some_python_code_on_one_line()

... so it actually looks like a bit cleaner, like a comment.

So instead of:

	::python
	> /path/to/some/file.py(##)method()
	-> some_python_code_on_one_line
	(Pdb)

You see:

	::python
	> /path/to/some/file.py(##)some_function()
	-> s = 'Some function/file'
	(Pdb)

Hope that helps someone.
