# Python Operator Overloading Cheat Sheet

This document provides a quick reference for operator overloading in Python.

## Quick Reference

### Arithmetic Operators

| Operator | Method                  | Description      |
| :------- | :---------------------- | :--------------- |
| `+`      | `__add__(self, other)`      | Addition         |
| `-`      | `__sub__(self, other)`      | Subtraction      |
| `*`      | `__mul__(self, other)`      | Multiplication   |
| `/`      | `__truediv__(self, other)`  | Division         |

### Comparison Operators

| Operator | Method                  | Description      |
| :------- | :---------------------- | :--------------- |
| `==`     | `__eq__(self, other)`       | Equal to         |
| `<`      | `__lt__(self, other)`       | Less than        |
| `>`      | `__gt__(self, other)`       | Greater than     |

## Key Rules

1.  **ALWAYS** return a value from operator methods.
2.  It's best practice to return a **new** object instead of modifying `self`.
3.  Use `__str__` for user-facing output and `__repr__` for developer-facing output.

## Example

Here is a basic template for a class with operator overloading:

```python
class Template:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Template(self.value + other.value)
    
    def __str__(self):
        return f"Value: {self.value}"
```

## Dunder Method Tiers

You don't need to memorize every dunder method. Focus on the most common ones.

### Essential

-   `__init__`: Constructor
-   `__str__`: User-friendly string representation
-   `__repr__`: Developer-friendly string representation
-   `__add__`: Addition operator (`+`)
-   `__eq__`: Equality operator (`==`)

### Nice to Have

-   `__len__`: Length of the object (e.g., `len(obj)`)
-   `__getitem__`: Access items by index (e.g., `obj[key]`)
-   `__setitem__`: Set items by index (e.g., `obj[key] = value`)
-   `__call__`: Make an object callable (e.g., `obj()`)

### Rarely Used

-   `__getattr__`: Control attribute access
-   `__setattr__`: Control attribute assignment
-   `__getstate__`: Customize object serialization (pickling)
-   `__setstate__`: Customize object deserialization (unpickling)

**Note:** Don't worry about the rarely used dunder methods until you have a specific need for them.
