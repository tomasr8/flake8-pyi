# flags: --extend-ignore=Y037
from typing import Optional, TypeAlias, Union

MaybeCStr: TypeAlias = Optional[CStr]
CStr: TypeAlias = Union[C, str]
__version__: str
__author__: str

def make_default_c() -> C: ...

# Disallow forward refs for base classes
class D(C):  # F821 undefined name 'C'
    parent: C
    def __init__(self) -> None: ...

class C:
    other: C = ...
    def __init__(self) -> None: ...
    def from_str(self, s: str) -> C: ...

class Baz(metaclass=Meta):  # F821 undefined name 'Meta'
    ...

class Foo(Bar, Baz, metaclass=Meta):  # F821 undefined name 'Bar'  # F821 undefined name 'Meta'
    ...

class Meta(type):
    ...

class Bar(metaclass=Meta):
    ...

# Allow circular references in annotations
class A:
    foo: B
    bar: dict[str, B]

class B:
    foo: A
    bar: dict[str, A]

# This recursive definition is allowed.
# We allow it by disabling checks for anything in the subscript
class Leaf: ...
class Tree(list[Tree | Leaf]): ...

# This recursive definition is not allowed.
class Parent(Child): ...   # F821 undefined name 'Child'
class Child(Parent): ...

class MyClass:
    foo: int
    bar = foo

baz: MyClass
eggs = baz

# Not allowed, unless annotated with `TypeAlias`.
# This is the default pyflakes behaviour - when annotated with `TypeAlias`,
# pyflakes defers evaluating the value of the assignment.
# https://github.com/PyCQA/pyflakes/issues/671
X = Y  # F821 undefined name 'Y'
Y = str
Recursive = list[Recursive | str]  # Y026 Use typing_extensions.TypeAlias for type aliases, e.g. "Recursive: TypeAlias = list[Recursive | str]"  # F821 undefined name 'Recursive'

# Same as above but this time with a `TypeAlias`
U: TypeAlias = V
V = str
Recursive2: TypeAlias = list[Recursive2 | str]
