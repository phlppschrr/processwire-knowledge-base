# WireData

Source: `wire/core/WireData.php`

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

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@method WireArray and($items = null)

## set()

Set a value to this object’s data

~~~~~
// Set a value for a property
$item->set('foo', 'bar');

// Set a property value directly
$item->foo = 'bar';

// Set a property using array access
$item['foo'] = 'bar';
~~~~~


@param string $key Name of property you want to set

@param mixed $value Value of property

@return $this

@see WireData::setQuietly(), WireData::get()

## setQuietly()

Same as set() but without change tracking

- If `$this->trackChanges()` is false, then this is no different than set(), since changes aren't being tracked.
- If `$this->trackChanges()` is true, then the value will be set quietly (i.e. not recorded in the changes list).


@param string $key Name of property you want to set

@param mixed $value Value of property

@return $this

@see Wire::trackChanges(), WireData::set()

## setArray()

Set an array of key=value pairs

This is the same as the `WireData::set()` method except that it can set an array
of properties at once.


@param array $data Associative array of where the keys are property names, and values are… values.

@return $this

@see WireData::set()

## __set()

Provides direct reference access to set values in the $data array

@param string $key

@param mixed $value

## get()

Retrieve the value for a previously set property, or retrieve an API variable

- If the given $key is an object, it will cast it to a string.
- If the given $key is a string with "|" pipe characters in it, it will try all till it finds a non-empty value.
- If given an API variable name, it will return that API variable unless the class has direct access API variables disabled.

~~~~~
// Retrieve the value of a property
$value = $item->get("some_property");

// Retrieve the value of the first non-empty property:
$value = $item->get("property1|property2|property2");

// Retrieve a value using array access
$value = $item["some_property"];
~~~~~


@param string|object $key Name of property you want to retrieve.

@return mixed|null Returns value of requested property, or null if the property was not found.

@see WireData::set()

## data()

Get or set a low-level data value

Like get() or set() but will only get/set from the WireData's protected $data array.
This is used to bypass any extra logic a class may have added to its get() or set()
methods. The benefit of this method over get() is that it excludes API vars and potentially
other things (defined by descending classes) that you may not want.

- To get a value, simply omit the $value argument.
- To set a value, specify both the $key and $value arguments.
- If you omit a $key and $value, this method will return the entire data array.


~~~~~
// Set a property
$item->data('some_property', 'some value');

// Get the value of a previously set property
$value = $item->data('some_property');
~~~~~

@param string|array $key Property you want to get or set, or associative array of properties you want to set.

@param mixed $value Optionally specify a value if you want to set rather than get.
 Or Specify boolean TRUE if setting an array via $key and you want to overwrite any existing values (rather than merge).

@return array|WireData|null Returns one of the following:
  - `mixed` - Actual value if getting a previously set value.
  - `null` - If you are attempting to get a value that has not been set.
  - `$this` - If you are setting a value.

## getArray()

Returns the full array of properties set to this object

If descending classes also store data in other containers, they may want to
override this method to include that data as well.


@return array Returned array is associative and indexed by property name.

## getDot()

Get a property via dot syntax: field.subfield.subfield

Some classes descending WireData may choose to add a call to this as part of their
get() method as a syntax convenience.

~~~~~
$value = $item->get("parent.title");
~~~~~


@param string $key Name of property you want to retrieve in "a.b" or "a.b.c" format

@return null|mixed Returns value if found or null if not

## __get()

Provides direct reference access to variables in the $data array

Otherwise the same as get()

@param string $name

@return mixed|null

## __invoke()

Enables use of $var('key')

@param string $key

@return mixed

## remove()

Remove a previously set property

~~~~~
$item->remove('some_property');
~~~~~


@param string $key Name of property you want to remove

@return $this

## getIterator()

Enables the object data properties to be iterable as an array

~~~~~
foreach($item as $key => $value) {
  // ...
}
~~~~~


@return \ArrayObject

## has()

Does this object have the given property?

~~~~~
if($item->has('some_property')) {
  // the item has some_property
}
~~~~~


@param string $key Name of property you want to check.

@return bool True if it has the property, false if not.

## ___and()

Take the current item and append the given item(s), returning a new WireArray

This is for syntactic convenience in fluent interfaces.
~~~~~
if($page->and($page->parents)->has("featured=1")) {
   // page or one of its parents has a featured property with value of 1
}
~~~~~


@param WireArray|WireData|string|null $items May be any of the following:
  - `WireData` object (or derivative)
  - `WireArray` object (or derivative)
  - Name of any property from this object that returns one of the above.
  - Omit argument to simply return this object in a WireArray

@return WireArray Returns a WireArray of this object *and* the one(s) given.

@throws WireException If invalid argument supplied.

## __debugInfo()

debugInfo PHP 5.6+ magic method

@return array
