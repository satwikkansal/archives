title: Python programming practices for efficient and optimized code
link: https://satwikkansal.wordpress.com/2016/12/27/python-programming-practices-for-efficient-and-optimized-code/
author: satwikkansal
description: 
post_id: 381
created: 2016/12/27 06:51:36
created_gmt: 2016/12/27 06:51:36
comment_status: open
post_name: python-programming-practices-for-efficient-and-optimized-code
status: publish
post_type: post

# Python programming practices for efficient and optimized code

In this blog post,  I will try to cover common techniques to write more efficient and optimized code in Python. By efficient and optimized I mean - A code that requires minimum memory, executes faster, looks clean, is properly documented and makes it easy for other developers to collaborate. This might help you while contributing to an Open Source organization, submitting a solution to an Online Judge, working on large data processing problems like Machine Learning or while making your own project. So let's get started! 

## Don't blow off the memory

Unlike C/C++, Python's memory management is performed by the interpreter and the  users have no control over it. Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the _Python memory manager_. So you just create an object and the Python Virtual Machine handles the memory needed and where it shall be placed in the memory layout. However, a deep insight of how the things work and different ways to do them can help you minimize memory usage of your program. 

  * Use generators for calculating large sets of results. Generators give you lazy evaluation. You use them by iterating over them, either explicitly with 'for' or implicitly by passing it to any function or construct that iterates. You can think of generators as returning multiple items, as if they return a list, but instead of returning them all at once they return them one-by-one, and the generator function is paused until the next item is requested. Read more about Python Generators from [here](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/).
  * For large number/data crunching, you can use libraries like [Numpy](http://www.numpy.org/) which handle memory management gracefully.
  * Track your memory usage at object level by using inbuilt modules like [resource ](https://docs.python.org/2/library/resource.html)and [objgraph](https://mg.pov.lt/objgraph/).
  * Managing memory leaks in Python can be a tough job but luckily there are tools like [heapy](https://pypi.python.org/pypi/guppy/) for debugging memory leaks. _heapy_ can be used along with _objgraph_ to watch allocation growth of diff objects over time. _heapy_ can show which objects are holding the most memory etc._ objgraph_ can help in finding the backreferences to understand exactly why they cannot be freed. You can read more about diagnosing memory leaks in Python from [here](http://chase-seibert.github.io/blog/2013/08/03/diagnosing-memory-leaks-python.html).
  * Use format instead of ‘+’ for generating strings -  In Python,  `str` is immutable, so the left and right string have to be copied into the new string for every pair of concatenation. If you concatenate four strings of length 10, you will be copying (10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90 characters, instead of just 40 characters. And things gets quadratically worse as the number and size of the string increases. Java optimizes this case some of the times by transforming the series of concatenation to use `StringBuilder`, but CPython doesn't. So it is advised to use .format or % syntax. If you can't decide which one to choose among .format and %, check [this](http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format) interesting Stackoverflow thread.
  * Use ___slots___ when defining a Python class. You can tell Python not to use a dynamic _dict_, and only allocate space for a fixed set of attributes eliminating the overhead of one dict for every object by settings `__slots__` on the class to a fixed list of attribute names. Read more about _slots_ from [here](http://stackoverflow.com/questions/472000/usage-of-slots).
You can read a bit in detail about memory management in Python by the developers of Theano from [here](http://deeplearning.net/software/theano/tutorial/python-memory-management.html). 

## Python 2 or Python 3? Both!

When starting a new Python project or even starting with Python altogether you may have found yourself in the dilemma of choosing Python 2 or Python 3. This is a widely discussed topic with many opinions and good explanations on the internet. However, it is actually possible to write code in a way that works on both Python 2 and Python 3 interpreters. The most common way to achieve this use packages like _future, builtins_, and six to maintain a single, clean Python 3.x-compatible codebase and support both Python 2 and Python 3 with minimal overhead. `python-future` is the missing compatibility layer between Python 2 and Python 3.It provides `future` and `past` packages with backports and forward ports of features from Python 3 and 2. It also comes with `futurize` and `pasteurize`, customized 2to3-based scripts that help you to convert either Py2 or Py3 code easily to support both Python 2 and 3 in a single clean Py3-style codebase, module by module. Please do check the awesome **Cheat Sheet** for writing Python 2-3 compatible code by Ed Schofield. And if you're more into watching videos than reading then you may find his talk at PyCon AU 2014, “[Writing 2/3 compatible code](http://www.youtube.com/watch?v=KOqk8j11aAI&t=10m14s)” helpful. 

## The first impression is the last impression

Sharing code is a rewarding endeavor.  Whatever the motivation, your good intentions may not have the desired outcome if people find your code hard to use or understand. Almost every organization follows style guidelines that developers have to follow for consistency, easy debugging, and ease of collaboration. The [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is like a mini style and design guide for Python. Following are some of the popular style guidelines for Python: 

  1. [PEP-8 style guide](https://www.python.org/dev/peps/pep-0008/)
  2. [Python Idioms and efficiency](https://www.memonic.com/user/pneff/folder/python/id/1bufp)
  3. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
These guidelines discuss how to use whitespace, using commas and braces, how to, object naming guidelines, etc.Though they may be conflicting each other at some situation but all of them really have the same objective - Clean, Readable, and Debuggable standard for code. So just stick to one, or follow your own guide but don't try to follow something drastically different from widely accepted standards. 

### Using pylint

[Pylint](http://www.logilab.org/857) is a Python tool that checks a module for coding standards. _Pylint_ can be a quick and easy way of seeing if your code has captured the essence of PEP-8 and is therefore ‘friendly’ to other potential users. It also provides you reports with insightful metrics and statistics that may help you judge the quality of code. You can also customize it by creating your own _.pylintrc_ file and using it. Pylint is not the only choice, there are other tools like _PyChecker, PyFlakes,_ and packages like _pep8 and flakes8_. 

## Reports and analysis