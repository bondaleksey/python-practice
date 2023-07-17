
### Python the Interpreter
CPython the Python interpreter maintained by the Python Software Foundation, avail-
able at https://www.python.org.
CPython is an implementation of the Python
language—that is, software created to follow a specification—but there
are others.
CPython is called the Python language’s *reference implementation* because
if there’s a difference between how CPython and another interpreter inter-
pret Python code, CPython’s behavior is considered canonical and correct.

### Garbage Collection

Python has garbage collection, a form of automatic
memory management that tracks when to allocate and free memory so
the programmer doesn’t have to. You can think of garbage collection as
memory recycling, because it makes memory available for new data.


### Literals
```age = 42 + len('Zophie')```

the 42 and 'Zophie' text are integer and string literals.
Think of a literal as a value that literally appears in source code text.
Only the built-in data types
can have literal values in Python source code, so the variable `age` isn’t a literal value.


### Keywords
Every programming language has its own keywords. The Python (35) keywords
are a set of names reserved for use as part of the language and cannot be
used as variable names (that is, as identifiers).

|1|2|3|4|5|
|:---:|:---:|:---:|:---:|:---:|
| and | continue | finally | is | raise |
| as | def | for | lambda | return |
|assert|del|from|None|True|
|async|elif|global|nonlocal|try|
|await|else|if|not|while|
|break|except|import|or|with|
|class|False|in|pass|yield|

[realpython - keywords](https://realpython.com/python-keywords/) 