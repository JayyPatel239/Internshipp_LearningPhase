
# 3Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.

'''
Yes, you **can** change the `self` parameter to anything else—like `slf`, `harry`, `this`, etc. It’s **not a keyword**, just a **convention**.

However, changing it is **not recommended**, because:

* It makes code **harder to read** for others (or your future self).
* Every Python programmer expects `self` in instance methods.

---

###  Example using `harry` instead of `self`:

```python
class MyClass:
    def __init__(harry, name):
        harry.name = name

    def say_hello(harry):
        print(f"Hello, {harry.name}!")
```

###  Usage:

```python
obj = MyClass("Python")
obj.say_hello()
```

###  Output:

```
Hello, Python!
```

---

###  Same with `slf`:

```python
class Test:
    def __init__(slf, value):
        slf.value = value

    def show(slf):
        print(f"Value: {slf.value}")
```


So yes, it **works technically**, but stick to `self` for clean, readable Python code.


'''