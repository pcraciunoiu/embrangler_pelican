Title: Python scoping: understading LEGB
Summary: Quick example of messing with python scoping
Tags: python, beginner, scoping, mozilla
Time: 8:11PM

__Update:__ Thanks to Avazu for [a clean suggestion](#what-to-do) and Fred for pointing out I should have indicated a good way to get around this.


## Summary

Python scoping fun! [Read about LEGB](http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules) to understand the basics of python scoping.

## Beef

I never bothered to read about how python scoping works until I hit this. It's not exactly something to research until you have issues with it. :)

I had something like this going on:

	#!python
	def func1(param=None):
	    def func2():
	        if not param:
	            param = 'default'
	        print param
	    # Just return func2.
	    return func2


	if __name__ == '__main__':
	    func1('test')()

__Note:__ Actual code was not as straightforward, `func2` was actually a decorator. Admittedly, using the same parameter name is not a must, but it's still a curiosity. I just wanted to fall back to a default value on run-time.

If you try to run this in python, here's what you get:

	~ $ python test.py 
	Traceback (most recent call last):
	  File "test.py", line 11, in <module>
	    func1('test')()
	  File "test.py", line 3, in func2
	    if not param:
	UnboundLocalError: local variable 'param' referenced before assignment

If you're curious, you can [read about the principles of LEGB.](http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules) You have to understand a bit about compilers and [the AST](http://en.wikipedia.org/wiki/Abstract_syntax_tree) to get what's going on behind the scenes. You might think that replacing lines 3-4 with:

	::python
	param = param or 'default'

Might work. But no. You can't assign the same parameter at the local level if the enclosing level defines it. Even this fails:

	::python
	param = param

Fun, no?

## What to do?

There are a few ways to get around this.

* Assign <code>param</code> outside of func2. This doesn't work if you need the default value to be dependent on what params func2 receives.
* Use a second variable, <code>param2</code> inside of func2 (posted below).

Here is the solution suggested by our commenter Avazu (over on [the mozilla webdev blog](http://blog.mozilla.com/webdev/2011/01/31/python-scoping-understanding-legb/#comments)):

	::python
	def func1(param=None):
	    def func2(param2=param):
	        if not param2:
	            param2 = 'default'
	        print param2
	    # Just return func2.
	    return func2


## Read more

* [LEGB (stackoverflow)](http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules)
* [Python docs on scope and namespaces.](http://docs.python.org/tutorial/classes.html#python-scopes-and-namespaces)
