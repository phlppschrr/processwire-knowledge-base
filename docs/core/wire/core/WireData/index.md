# WireData

Source: `wire/core/WireData.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `ArrayAccess`


Groups:
Group: [other](group-other.md)

ProcessWire WireData

This is the base data container class used throughout ProcessWire.
It provides get and set access to properties internally stored in a $data array.
Otherwise it is identical to the Wire class.

WireData is the base data-storage class used by many ProcessWire object types and most modules.
WireData is very much like its parent `Wire` class with the fundamental difference being that it is designed
for runtime data storage. It provides this primarily through the built-in `get()` and `set()` methods for
getting and setting named properties to WireData objects. The most common example of a WireData object is
`Page`, the type used for all pages in ProcessWire.

Properties set to a WireData object can also be set or accessed directly, like `$item->property` or using
array access like `$item[$property]`. If you `foreach()` a WireData object, the default behavior is to
iterate all of the properties/values present within it.

May also be accessed as array.

Methods:
Method: [set()](method-set.md)
Method: [setQuietly()](method-setquietly.md)
Method: [setArray()](method-setarray.md)
Method: [__set()](method-__set.md)
Method: [get()](method-get.md)
Method: [data()](method-data.md)
Method: [getArray()](method-getarray.md)
Method: [getDot()](method-getdot.md)
Method: [__get()](method-__get.md)
Method: [__invoke()](method-__invoke.md)
Method: [remove()](method-remove.md)
Method: [getIterator()](method-getiterator.md)
Method: [has()](method-has.md)
Method: [and()](method-___and.md) (hookable)
Method: [__debugInfo()](method-__debuginfo.md)
