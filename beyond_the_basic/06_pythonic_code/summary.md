- The Zen of  Python (import this)
- Use `for i, item in enumerate(LIST)` instead `for i in range(len(LIST))`
- Use `with open('','r/w + b') as file ...` instead open() + close()
- Use `is` to compare with `None` instead of `==`
- Use `f-strings`
- slicing `[a:b]` is creating *shallow copy* if the list like `copy.copy()`
- With Dictionaries use `get()` and `setdefault()`
- Use collections.defaultdict for Default Values
- Use Dictionaries Instead of a switch Statement
- If you need use Python's *ternary operators* `valueIfTrue if condition else valueIfFalse`
- If you need you can use chaining assignment `spam == eggs == bacon == 'string'` and comparison operators `42 < spam < 99`



For further information about dictionaries, consult Python programmer Brandon Rhodes’s incredible talks about dictionaries and how they work: 
“The Mighty Dictionary” at PyCon 2010, viewable at https://invpy.com/mightydictionary, and 
“The Dictionary Even Mightier” at PyCon 2017, viewable at https://invpy.com/dictionaryevenmightier.
