title: Common Python Interview Questions
link: https://satwikkansal.wordpress.com/2016/12/24/common-python-interview-questions/
author: satwikkansal
description: 
post_id: 196
created: 2016/12/24 09:09:06
created_gmt: 2016/12/24 09:09:06
comment_status: open
post_name: common-python-interview-questions
status: publish
post_type: post

# Common Python Interview Questions

This blog post will cover some of the typical Python questions asked in Interviews when you're  applying for a Python related job. I assume that you've basic knowledge of Python and can write programs in python easily. I would try to put all the content and links in this post that I've gathered from various sources on the internet including Stack Overflow, Code Mentor, Learn python the Hard Way and many other resources. So without wasting much time, Let's dive in! 

## How is Python different from other languages like C++, Java, etc?

Python is an interpreted language. That means that, unlike languages like _C_ and its variants, Python does not need to be compiled before it is run. Other interpreted languages include _PHP_ and _Ruby_. 

  * Python is dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
  * Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++'s public, private), the justification for this point is given as "we are all adults here"
  * In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
  * Writing Python code is quick but running it is often slower than compiled languages. Fortunately， Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it's really quite quick because a lot of the number crunching it does isn't actually done by Python
  * Python finds use in many spheres - web applications, automation, scientific modeling, big data applications and much more. It's also often used as "glue" code to get other languages and components to play nice.
  * Python makes difficult things easy so programmers can focus on overriding algorithms and structures rather than nitty-gritty low-level details.
  Python has five standard data types − 
  * Numbers
  * String
  * List
  * Tuple
  * Dictionary

## How is Python 2 different from Python 3?

Definitely, Python 3.x is an improvement over Python 2.x, but there are reasons to continue to use Python 2.x or to write code in such a way that it's compatible with both the versions because most of the third-party libraries and frameworks that are still written for Python 2.x. Please go through [this](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html) wonderful comparison blog post by Sebastian Raschka as this question is often asked in the interviews related to Python. 

## How does multithreading works in Python?

Python doesn't allow multi-threading in the truest sense of the word. It has a[ multi-threading package](https://docs.python.org/2/library/threading.html) (threading.py) but if you want to multi-thread to speed your code up, then it's usually not a good idea to use it. Python has a construct called the **Global Interpreter Lock (GIL).** The GIL makes sure that _only one of your 'threads' can execute at any one time._ A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. This happens very quickly so to the human eye it may seem like **your threads are** executing in parallel, but they are really just **taking turns using the same CPU core**. All this GIL passing **adds overhead to execution**. This means that if you want to make your code run faster then using the threading package often isn't a good idea. There are reasons to use Python's threading package. _If you want to run some things simultaneously, and efficiency is not a concern, then it's totally fine and convenient_. Or if you are running code that needs to wait for something (like some IO) then it could make a lot of sense. **But the threading library won't let you use extra CPU cores.** Multi-threading **can be outsourced** to:- 

  1. The operating system (by doing multi-processing)
  2. Some external application that calls your Python code (eg, Spark or Hadoop)
  3. Some code that your Python code calls (eg: you could have your Python code call a C function that does the expensive multi-threaded stuff).
To achieve actual parallelization in Python, you might have a look at [multiprocessing ](https://docs.python.org/2/library/multiprocessing.html)module of Python. A few snaps from Stackoverflow regarding this:- ![image05](https://satwikkansal.files.wordpress.com/2016/12/image05.png)![image00](https://satwikkansal.files.wordpress.com/2016/12/image00.png) Also, it's good to know difference detailed difference between Multithreading and Multiprocessing. ![threading_vs_processing.png](https://satwikkansal.files.wordpress.com/2016/12/threading_vs_processing.png)

## How does call by reference or call by value work in Python?

When asked whether Python function calling model is "call-by-value" or "call-by-reference", the correct answer is: **neither**. Instead, in Python arguments are [passed by assignment](http://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference). The rationale behind this is twofold: 

  1. the parameter passed in is actually a _reference_ to an object (but the reference is passed by value)
  2. some data types are mutable, but others aren't
So: 
  * If you pass a _mutable_ object into a method, the method gets a reference to that same object and you can mutate it to your heart's delight, but if you rebind the reference in the method, the outer scope will know nothing about it, and after you're done, the outer reference will still point at the original object.
  * If you pass an _immutable_ object to a method, you still can't rebind the outer reference, and you can't even mutate the object.
If you still don't get this, Please check [this](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/) blog-post by Jeff Knupp. Here's a small demonstration by code [code language="python"] l_mem = [] l = l_mem # the first call for i in range(2): l.append(i*i) print(l) # [0, 1] l = [3,2,1] # the second call for i in range(3): l.append(i*i) print(l) # [3, 2, 1, 0, 1, 4] l = l_mem # the third call for i in range(3): l.append(i*i) print(l) # [0, 1, 0, 1, 4] [/code] The first function call should be fairly obvious, the loop appends 0 and then 1 to the empty list, l. l is a name for a variable that points to a list stored in memory. The second call starts off by creating a new list in a new block of memory. l then refers to this new list. It then appends 0, 1 and 4 to this new list. So that's great. The third function call is the weird one. It uses the original list stored in the original memory block. That is why it starts off with 0 and 1. A cool "Balloon analogy" that I found on some Stackoverflow thread can be helpful: