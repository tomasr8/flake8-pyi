import sys

if sys.version_info[0] == 2: ...
if sys.version_info[0] == True: ...  # Y003 Unrecognized sys.version_info check  # E712 comparison to True should be 'if cond is True:' or 'if cond:'
if sys.version_info[0.0] == 2: ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[False] == 2: ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[0j] == 2: ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[0] == (2, 7): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[0] == '2': ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[1:] >= (7, 11): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[::-1] < (11, 7): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:3] >= (2, 7): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:True] >= (2, 7): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:1] == (2,): ...
if sys.version_info[:1] == (True,): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:1] == (2, 7): ...  # Y005 Version comparison must be against a length-1 tuple
if sys.version_info[:2] == (2, 7): ...
if sys.version_info[:2] == (2,): ...  # Y005 Version comparison must be against a length-2 tuple
if sys.version_info[:2] == "lol": ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:2.0] >= (3, 9): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:2j] >= (3, 9): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info[:, :] >= (2, 7): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info < [3, 0]: ...  # Y003 Unrecognized sys.version_info check
if sys.version_info < ('3', '0'): ...  # Y003 Unrecognized sys.version_info check
if sys.version_info >= (3, 4, 3): ...  # Y004 Version comparison must use only major and minor version
if sys.version_info == (3, 4): ...  # Y006 Use only < and >= for version comparisons
if sys.version_info > (3, 0): ...  # Y006 Use only < and >= for version comparisons
if sys.version_info <= (3, 0): ...  # Y006 Use only < and >= for version comparisons
if sys.version_info < (3, 5): ...
if sys.version_info >= (3, 5): ...
if (2, 7) <= sys.version_info < (3, 5): ...  # Y002 If test must be a simple comparison against sys.platform or sys.version_info

if sys.version_info >= (3, 10):
    def foo1(x, *, bar=True, baz=False): ...
elif sys.version_info >= (3, 9):
    def foo1(x, *, bar=True): ...
else:
    def foo1(x): ...

if sys.version_info < (3, 9):
    def foo2(x): ...
elif sys.version_info < (3, 10):
    def foo2(x, *, bar=True): ...

if sys.version_info < (3, 10):  # Y066 When using if/else with sys.version_info, put the code for new Python versions first, e.g. "if sys.version_info >= (3, 10)"
    def foo3(x): ...
else:
    def foo3(x, *, bar=True): ...

if sys.version_info < (3, 8):  # Y066 When using if/else with sys.version_info, put the code for new Python versions first, e.g. "if sys.version_info >= (3, 8)"
    def foo4(x): ...
elif sys.version_info < (3, 9):  # Y066 When using if/else with sys.version_info, put the code for new Python versions first, e.g. "if sys.version_info >= (3, 9)"
    def foo4(x, *, bar=True): ...
elif sys.version_info < (3, 10):  # Y066 When using if/else with sys.version_info, put the code for new Python versions first, e.g. "if sys.version_info >= (3, 10)"
    def foo4(x, *, bar=True, baz=False): ...
else:
    def foo4(x, *, bar=True, baz=False, qux=1): ...
