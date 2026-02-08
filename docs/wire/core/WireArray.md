# WireArray

Source: `wire/core/WireArray.php`

ProcessWire WireArray

WireArray is the base array access object used in the ProcessWire framework.

Several methods are duplicated here for syntactical convenience and jQuery-like usability.
Many methods act upon the array and return $this, which enables WireArrays to be used for fluent interfaces.
WireArray is the base of the PageArray (subclass) which is the most used instance.

@todo can we implement next() and prev() like on Page, as alias to getNext() and getPrev()?

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com


WireArray is the base iterable array type used throughout the ProcessWire framework.

**Nearly all collections of items in ProcessWire are derived from the WireArray type.**
This includes collections of pages, fields, templates, modules and more. As a result, the WireArray class is one
you will be interacting with regularly in the ProcessWire API, whether you know it or not.

Below are all the public methods you can use to interact with WireArray types in ProcessWire. In addition to these
methods, you can also treat WireArray types like regular PHP arrays, in that you can `foreach()` them and get or
set elements using array syntax, i.e. `$value = $items[$key];` to get an item or `$items[] = $item;` to add an item.

## other

@method WireArray and($item)

@property int $count Number of items

@property Wire|null $first First item

@property Wire|null $last Last item

@property array $keys All keys used in this WireArray

@property array $values All values used in this WireArray

## __construct()

Construct

## isValidItem()

Is the given item valid for storange in this array?

Template method that descending classes may use to validate items added to this WireArray


@param mixed $item Item to test for validity

@return bool True if item is valid and may be added, false if not

## isValidKey()

Is the given item key valid for use in this array?

Template method that descendant classes may use to validate the key of items added to this WireArray


@param string|int $key Key to test

@return bool True if key is valid and may be used, false if not

## isIdentical()

Is the given WireArray identical to this one?


@param WireArray $items

@param bool|int $strict Use strict mode? Optionally specify one of the following:
	`true` (boolean): Default. Compares items, item object instances, order, and any other data contained in WireArray.
	`false` (boolean): Compares only that items in the WireArray resolve to the same order and values (though not object instances).

@return bool True if identical, false if not.

## import()

Import the given item(s) into this WireArray.

- Adds imported items to the end of the WireArray.
- Skips over any items already present in the WireArray (when duplicateChecking is enabled)


@param array|WireArray $items Items to import.

@return $this

@throws WireException If given items not compatible with the WireArray

## add()

Add an item to the end of the WireArray.

~~~~~
$items->add($item);
~~~~~


@param int|string|array|object|Wire|WireArray $item Item to add.

@return $this

@throws WireException If given an item that can't be stored by this WireArray.

@see WireArray::prepend(), WireArray::append()

## _insert()

Insert an item either before or after another

Provides the implementation for the insertBefore and insertAfter functions

@param int|string|array|object $item Item you want to insert

@param int|string|array|object $existingItem Item already present that you want to insert before/afer

@param bool $insertBefore True if you want to insert before, false if after

@return $this

@throws WireException if given an invalid item

## insertBefore()

Insert an item before an existing item

~~~~~
$items->insertBefore($newItem, $existingItem);
~~~~~


@param Wire|string|int $item Item you want to insert.

@param Wire|string|int $existingItem Item already present that you want to insert before.

@return $this

## insertAfter()

Insert an item after an existing item

~~~~~
$items->insertAfter($newItem, $existingItem);
~~~~~


@param Wire|string|int $item Item you want to insert

@param Wire|string|int $existingItem Item already present that you want to insert after

@return $this

## replace()

Replace one item with the other

- The order of the arguments does not matter.
- If both items are already present, they will change places.
- If one item is not already present, it will replace the one that is.
- If neither item is present, both will be added at the end.

~~~~~
$items->replace($existingItem, $newItem);
~~~~~


@param Wire|string|int $itemA

@param Wire|string|int $itemB

@return $this

## set()

Set an item by key in the WireArray.


@param int|string $key Key of item to set.

@param int|string|array|object|Wire $value Item value to set.

@throws WireException If given an item not compatible with this WireArray.

@return $this

## __set()

Enables setting of WireArray elements in object notation.

Example: $myArray->myElement = 10;
Not applicable to numerically indexed arrays.

@param int|string $property Key of item to set.

@param int|string|array|object Value of item to set.

@throws WireException

## __isset()

Ensures that isset() and empty() work for this classes properties.

@param string|int $key

@return bool

## __unset()

Ensures that unset() works for this classes data.

@param int|string $key

## setArray()

Like set() but accepts an array or WireArray to set multiple values at once


@param array|WireArray $data Array or WireArray of data that you want to set.

@return $this

## get()

Returns the value of the item at the given index, or null if not set.

You may also specify a selector, in which case this method will return the same result as
the `WireArray::findOne()` method. See the $key argument description for more details on
what can be provided.


@param int|string|array $key Provide any of the following:
 - Key of item to retrieve.
 - Array of keys, in which case an array of matching items will be returned, indexed by your keys.
 - A selector string or selector array, to return the first item that matches the selector.
 - A string of text with "{var}" tags in it that will be populated with any matching properties from this WireArray.
 - A string like "foobar[]" which returns an array of all "foobar" properties from each item in the WireArray.
 - A string containing the "name" property of any item, and the matching item will be returned.

@return WireData|Page|mixed|array|null Value of item requested, or null if it doesn't exist.

@throws WireException

## __get()

Enables derefencing of WireArray elements in object notation.

Example: $myArray->myElement
Not applicable to numerically indexed arrays.
Fuel properties and hooked properties have precedence with this type of call.

@param int|string $name

@return Wire|WireData|Page|mixed|bool Value of item requested, or false if it doesn't exist.

## getProperty()

Get a predefined property of the array, or extra data that has been set.

Default properties include;

- `count` (int): Number of items present in this WireArray.
- `last` (mixed): Last item in this WireArray.
- `first` (mixed): First item in this WireArray.
- `keys` (array): Keys used in this WireArray.
- `values` (array): Values present in this WireArray.

These can also be accessed by direct reference.

~~~~~
// Get count
$count = $items->getProperty('count');

// Same as above using direct access property
$count = $items->count;
~~~~~


@param string $property Name of property to retrieve

@return Wire|mixed

## getItemThatMatches()

Return the first item in this WireArray having a property named $key with $value, or NULL if not found.

Used internally by get() and has() methods.

@param string $key Property to match.

@param string|int|object $value $value to match.

@return Wire|null

## has()

Does this WireArray have the given item, index, or match the given selector?

If the WireArray uses numeric keys, then this will also match a WireData object's "name" field.

~~~~~
// See if it has a given $item
if($items->has($item)) {
  // Has the given $item
}

// See if it has an object with a "name" property matching our text
if($items->has("name=something")) {
  // Has an item with a "name" property equal to "something"
}

// Same as above, but works since "name" is assumed for many types
if($items->has("something")) {
  // It has it
}
~~~~~


@param int|string|Wire $key Key of item to check or selector.

@return bool True if the item exists, false if not.

## getArray()

Get a PHP array of all the items in this WireArray with original keys maintained


@return array Copy of the array that WireArray uses internally.

@see WireArray::getValues()

## getAll()

Returns all items in the WireArray (for syntax convenience)

This is for syntax convenience, as it simply returns this instance of the WireArray.


@return $this

## getKeys()

Returns a regular PHP array of all keys used in this WireArray.


@return array Keys used in the WireArray.

## getValues()

Returns a regular PHP array of all values used in this WireArray.

Unlike the `WireArray::getArray()` method, this does not attempt to maintain original
keys of the items. The returned array is reindexed from 0.


@return array|Wire[] Values used in the WireArray.

@see WireArray::getArray()

## getRandom()

Get a random item from this WireArray.

- If one item is requested (default), the item is returned (unless `$alwaysArray` argument is true).
- If multiple items are requested, a new `WireArray` of those items is returned.
- We recommend using this method when you just need 1 random item, and using the `WireArray::findRandom()` method
  when you need multiple random items.

~~~~~
// Get a single random item
$randomItem = $items->getRandom();

// Get 3 random items
$randomItems = $items->getRandom(3);
~~~~~


@param int $num Number of items to return. Optional and defaults to 1.

@param bool $alwaysArray If true, then method will always return an array of items, even if it only contains 1 item.

@return WireArray|Wire|mixed|null Returns value of item, or new WireArray of items if more than one requested.

@see WireArray::findRandom(), WireArray::findRandomTimed()

## findRandom()

Find a specified quantity of random elements from this WireArray.

Unlike `WireArray::getRandom()` this method always returns a WireArray (or derived type).

~~~~~
// Get 3 random items
$randomItems = $items->findRandom(3);
~~~~~


@param int $num Number of items to return

@return WireArray

@see WireArray::getRandom(), WireArray::findRandomTimed()

## findRandomTimed()

Find a quantity of random elements from this WireArray based on a timed interval (or user provided seed).

If no `$seed` is provided, today's date (day) is used to seed the random number
generator, so you can use this function to rotate items on a daily basis.

_Idea and implementation provided by [mindplay.dk](https://twitter.com/mindplaydk)_

~~~~~
// Get same 3 random items per day
$randomItems = $items->findRandomTimed(3);

// Get same 3 random items per hour
$randomItems = $items->findRandomTimed('YmdH');
~~~~~


@param int $num The amount of items to extract from the given list

@param int|string $seed Optionally provide one of the following:
  - A PHP [date()](http://php.net/manual/en/function.date.php) format string.
  - A number used to see the random number generator.
  - The default is the PHP date format "Ymd" which makes it randomize once daily.

@return WireArray

@see WireArray::findRandom()

## slice()

Get a slice of the WireArray.

Given a starting point and a number of items, returns a new WireArray of those items.
If `$limit` is omitted, then it includes everything beyond the starting point.

~~~~~
// Get first 3 items
$myItems = $items->slice(0, 3);
~~~~~


@param int $start Starting index.

@param int $limit Number of items to include. If omitted, includes the rest of the array.

@return WireArray Returns a new WireArray.

## prepend()

Prepend an item to the beginning of the WireArray.

~~~~~
// Add item to beginning
$items->prepend($item);
~~~~~


@param Wire|WireArray|mixed $item Item to prepend.

@return $this This instance.

@throws WireException

@see WireArray::append()

## append()

Append an item to the end of the WireArray

This is a functionally identical alias of the `WireArray::add()` method here for
naming consistency with the `WireArray::prepend()` method.

~~~~~
// Add item to end
$items->append($item);
~~~~~


@param Wire|WireArray|mixed $item Item to append.

@return $this This instance.

@see WireArray::prepend(), WireArray::add()

## unshift()

Unshift an element to the beginning of the WireArray (alias for prepend)

This is for consistency with PHP's naming convention of the `array_unshift()` method.


@param Wire|WireArray|mixed $item Item to prepend.

@return $this This instance.

@see WireArray::shift(), WireArray::prepend()

## shift()

Shift an element off the beginning of the WireArray and return it

Consistent with behavior of PHP's `array_shift()` method.


@return Wire|mixed|null Item shifted off the beginning or NULL if empty.

@see WireArray::unshift()

## push()

Push an item to the end of the WireArray.

Same as `WireArray::add()` and `WireArray::append()`, but here for syntax convenience.


@param Wire|mixed $item Item to push.

@return $this This instance.

@see WireArray::pop()

## pop()

Pop an element off the end of the WireArray and return it


@return Wire|mixed|null Item popped off the end or NULL if empty.

## shuffle()

Shuffle/randomize this WireArray


@return $this This instance.

## index()

Returns a new WireArray of the item at the given index.

Unlike `WireArray::get()` this returns a new WireArray with a single item, or a blank WireArray if item doesn't exist.
Applicable to numerically indexed WireArray only.


@param int $num Index number

@return WireArray

@see WireArray::eq()

## eq()

Returns the item at the given index starting from 0, or NULL if it doesn't exist.

Unlike the `WireArray::index()` method, this returns an actual item and not another WireArray.


@param int $num Return the n'th item in this WireArray. Specify a negative number to count from the end rather than the start.

@return Wire|null

@see WireArray::index()

## first()

Returns the first item in the WireArray or boolean false if empty.

Note that this resets the internal WireArray pointer, which would affect other active iterations.

~~~~~
$item = $items->first();
~~~~~


@return Wire|mixed|bool

## last()

Returns the last item in the WireArray or boolean false if empty.

Note that this resets the internal WireArray pointer, which would affect other active iterations.

~~~~~
$item = $items->last();
~~~~~


@return Wire|mixed|bool

## remove()

Removes the given item or index from the WireArray (if it exists).


@param int|string|Wire $key Item to remove (object), or index of that item, or (3.0.196+) selector string.

@return $this This instance.

## removeItems()

Removes multiple identified items at once


@param array|Wire|string|WireArray $items Items to remove

@return $this

## removeAll()

Removes all items from the WireArray, leaving it blank


@return $this

## sort()

Sort this WireArray by the given properties.

- Sort properties can be given as a string in the format `name, datestamp` or as an array of strings,
  i.e. `["name", "datestamp"]`.

- You may also specify the properties as `property.subproperty`, where property resolves to a Wire derived object
  in each item, and subproperty resolves to a property within that object.

- Prepend or append a minus "-" to reverse the sort (per field).

~~~~~
// Sort newest to oldest
$items->sort("-created");

// Sort by last_name then first_name
$items->sort("last_name, first_name");
~~~~~


@param string|array $properties Field names to sort by (CSV string or array).

@param int|null $flags Optionally specify sort flags (see sortFlags method for details).

@return $this reference to current instance.

## _sort()

Sort this WireArray by the given properties (internal use)

This function contains additions and modifications by @niklaka.

$properties can be given as a sortByField string, i.e. "name, datestamp" OR as an array of strings, i.e. array("name", "datestamp")
You may also specify the properties as "property.subproperty", where property resolves to a Wire derived object,
and subproperty resolves to a property within that object.

@param string|array $properties Field names to sort by (comma separated string or an array). Prepend or append a minus "-" to reverse the sort (per field).

@param int $numNeeded *Internal* amount of rows that need to be sorted (optimization used by filterData)

@return $this reference to current instance.

## sortFlags()

Get or set sort flags that affect behavior of any sorting functions

The following constants may be used when setting the sort flags:

- `SORT_REGULAR` compare items normally (don’t change types)
- `SORT_NUMERIC` compare items numerically
- `SORT_STRING` compare items as strings
- `SORT_LOCALE_STRING` compare items as strings, based on the current locale
- `SORT_NATURAL` compare items as strings using “natural ordering” like natsort()
- `SORT_FLAG_CASE` can be combined (bitwise OR) with SORT_STRING or SORT_NATURAL to sort strings case-insensitively
- `SORT_APPEND_NULLS` can be used on its own or combined with any of above (bitwise OR) to specify that null
   or blank values should be treated as unsortable and appended to the end of the sortable set rather than sorted as
   blank values. This duplicates the behavior prior to 3.0.194 (available only in 3.0.194+). Note that this flag
   is unique to ProcessWire only and is not in PHP.

For more details, see `$sort_flags` argument at: https://www.php.net/manual/en/function.sort.php


@param bool $sortFlags Optionally specify flag(s) to set

@return int Returns current flags

@since 3.0.129

## stableSort()

Sort given array by first given property.

This function contains additions and modifications by @niklaka.

@param array|WireArray &$data Reference to an array to sort.

@param array $properties Array of properties: first property is used now and others in recursion, if needed.

@param int $numNeeded *Internal* amount of rows that need to be sorted (optimization used by filterData)

@return array Sorted array (at least $numNeeded items, if $numNeeded is given)

## getItemPropertyValue()

Get the value of $property from $item

Used by the WireArray::sort method to retrieve a value from a Wire object.
Primarily here as a template method so that it can be overridden.
Lets it prepare the Wire for any states needed for sorting.

@param Wire $item

@param string $property

@return mixed

## filterData()

Filter out Wires that don't match the selector.

This is applicable to and destructive to the WireArray.
This function contains additions and modifications by @niklaka.

@param string|array|Selectors $selectors Selector string|array to use as the filter.

@param bool|int $not Make this a "not" filter? Use int 1 for “not all” mode as if selectors had brackets around it. (default is false)

@return $this reference to current [filtered] instance

## filterDataSelectors()

Prepare selectors for filtering

Template method for descending classes to modify selectors if needed

@param Selectors $selectors

## filter()

Filter this WireArray to only include items that match the given selector (destructive)

~~~~~
// Filter $items to contain only those with "featured" property having value 1
$items->filter("featured=1");
~~~~~


@param string|array|Selectors $selector Selector string or array to use as the filter.

@return $this reference to current instance.

@see filterData

## not()

Filter this WireArray to only include items that DO NOT match the selector (destructive)

~~~~~
// returns all pages that don't have a 'nonav' variable set to a positive value.
$pages->not("nonav");
~~~~~


@param string|array|Selectors $selector

@return $this reference to current instance.

@see filterData

## find()

Find all items in this WireArray that match the given selector.

This is non destructive and returns a brand new WireArray.

~~~~~
// Find all items with a title property containing the word "foo"
$matches = $items->find("title%=foo");
if($matches->count()) {
  echo "Found $matches->count items";
} else {
  echo "Sorry, no items were found";
}
~~~~~


@param string|array|Selectors $selector

@return WireArray

## findOne()

Find a single item by selector

This is the same as `WireArray::find()` except that it returns a single
item rather than a new WireArray of items.

~~~~~
// Get an item with name "foo-bar"
$item = $items->findOne("name=foo-bar");
if($item) {
  // item was found
} else {
  // item was not found
}
~~~~~


@param string|array|Selectors $selector

@return Wire|bool Returns item from WireArray or false if the result is empty.

@see WireArray::find()

## iterable()

Determines if the given item iterable as an array.

- Returns true for arrays and WireArray derived objects.
- Can be called statically like this `WireArray::iterable($a)`.


@param mixed $item Item to check for iterability.

@return bool True if item is an iterable array or WireArray (or subclass of WireArray).

## getIterator()

Allows iteration of the WireArray.

- Fulfills PHP's IteratorAggregate interface so that you can traverse the WireArray.
- No need to call this method directly, just use PHP's `foreach()` method on the WireArray.

~~~~~
// Traversing a WireArray with foreach:
foreach($items as $item) {
  // ...
}
~~~~~


@return \ArrayObject|Wire[]

## count()

Returns the number of items in this WireArray.

Fulfills PHP's Countable interface, meaning it also enables this WireArray to be used with PHP's `count()` function.

~~~~~
// These two are the same
$qty = $items->count();
$qty = count($items);
~~~~~


@return int

## __toString()

Returns a string representation of this WireArray.

@return string

## reverse()

Return a new reversed version of this WireArray.


@return WireArray

## unique()

Return a new array that is unique (no two of the same elements)

This is the equivalent to PHP's [array_unique()](http://php.net/manual/en/function.array-unique.php) function.


@param int $sortFlags Sort flags per PHP's `array_unique()` function (default=`SORT_STRING`)

@return WireArray

## trackAdd()

Track an item added

@param Wire|mixed $item

@param int|string $key

## trackRemove()

Track an item removed

@param Wire|mixed $item

@param int|string $key

## getItemsAdded()

Return array of all items added to this WireArray (while change tracking is enabled)


@return array|Wire[]

## getItemsRemoved()

Return array of all items removed from this WireArray (when change tracking is enabled)


@return array|Wire[]

## getNext()

Given an item, get the item that comes after it in the WireArray


@param Wire $item

@param bool $strict If false, string comparison will be used rather than exact instance comparison.

@return Wire|null Returns next item if found, or null if not

## getPrev()

Given an item, get the item before it in the WireArray


@param Wire $item

@param bool $strict If false, string comparison will be used rather than exact instance comparison.

@return Wire|null Returns item that comes before given item, or null if not found

## implode()

Combine all elements into a delimiter-separated string containing the given property from each item

Similar to PHP's `implode()` function.

[Introduction of implode method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

@param string $delimiter The delimiter to separate each item by (or the glue to tie them together).
	If not needed, this argument may be omitted and $property supplied first (also shifting $options to 2nd arg).

@param string|callable $property The property to retrieve from each item, or a function that returns the value to store.
	If a function/closure is provided it is given the $item (argument 1) and the $key (argument 2), and it should
	return the value (string) to use. If delimiter is omitted, this becomes the first argument.

@param array $options Optional options to modify the behavior:
 - `skipEmpty` (bool): Whether empty items should be skipped (default=true)
 - `prepend` (string): String to prepend to result. Ignored if result is blank.
 - `append` (string): String to append to result. Ignored if result is blank.
 - Please note that if delimiter is omitted, $options becomes the second argument.

@return string

@see WireArray::each(), WireArray::explode()

## explode()

Return a plain array of the requested property from each item

You may provide an array of properties as the $property, in which case it will return an
array of associative arrays with all requested properties for each item.

You may also provide a function as the $property. That function receives the $item
as the first argument and $key as the second. It should return the value that will be stored.

The keys of the returned array remain consistent with the original WireArray.

[Introduction of explode method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

@param string|callable|array $property Property or properties to retrieve, or callable function that should receive items.

@param array $options Options to modify default behavior:
 - `getMethod` (string): Method to call on each item to retrieve $property (default = "get")
 - `key` (string|null): Property of Wire objects to use for key of array, or omit (null) for non-associative array (default).

@return array

@see WireArray::each(), WireArray::implode()

## ___and()

Return a new copy of this WireArray with the given item(s) appended

Primarily for syntax convenience in fluent interfaces.

~~~~~
if($page->parents->and($page)->has($featured)) {
  // either $page or its parents has the $featured page
}
~~~~~

[Introduction of and method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

@param Wire|WireArray $item Item(s) to append

@return WireArray New WireArray containing this one and the given item(s).

## data()

Store or retrieve an extra data value in this WireArray

The data() function is exactly the same thing that it is in jQuery: <http://api.jquery.com/data/>.

~~~~~~
// set a data value named 'foo' to value 'bar'
$a->data('foo', 'bar');

// retrieve the previously set data value
$bar = $a->data('foo');

// get all previously set data
$all = $a->data();
~~~~~~

[Introduction of data method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

@param string|null|array|bool $key Name of data property you want to get or set, or:
 - Omit to get all data properties.
 - Specify associative array of [property => value] to set multiple properties.
 - Specify associative array and boolean TRUE for $value argument to replace all data with the new array given in $key.
 - Specify regular array of property names to return multiple properties.
 - Specify boolean FALSE to unset property name specified in $value argument.

@param mixed|null|bool $value Value of data property you want to set. Omit when getting properties.
 - Specify boolean TRUE to replace all data with associative array of data given in $key argument.

@return WireArray|mixed|array|null Returns one of the following, depending on specified arguments:
 - `mixed` when getting a single property: whatever you set is what you will get back.
 - `null` if the property you are trying to get does not exist in the data.
 - `$this` reference to this WireArray if you were setting a value.
 - `array` of all data if you specified no arguments or requested multiple keys.

## removeData()

Remove a property/value previously set with the WireArray::data() method.


@param string $key Name of property you want to remove

@return $this

## __invoke()

Enables use of $var('key')

@param string $key

@return mixed

## ___callUnknown()

Handler for when an unknown/unhooked method call is executed

If interested in hooking this, please see the `Wire::callUnknown()` method for more
details on the purpose and potential hooking implementation of this method.

The implementation built-in to WireArray provides a couple of handy capabilities to all
WireArray derived classes (assuming that `$items` is an instance of any WireArray):

- It enables you to call `$items->foobar()` and receive a regular PHP array
  containing the value of the "foobar" property from each item in this WireArray.
  It is equivalent to calling `$items->explode('foobar')`. Of course, substitute
  "foobar" with the name of any property present on items in the WireArray.

- It enables you to call `$items->foobar(", ")` and receive a string containing
  the value of the "foobar" property from each item, delimited by the string you
  provided as an argument (a comma and space ", " in this case). This is equivalent
  to calling `$items->implode(", ", "foobar")`.

- Also note that if you call `$items->foobar(", ", $options)` where $options is an
  array, it is equivalent to `$items->implode(", ", "foobar", $options)`.

~~~~~
// Get array of all "title" values from each item
$titlesArray = $items->title();

// Get a newline separated string of all "title" values from each item
$titlesString = $items->title("\n");
~~~~~


@param string $method Requested method name

@param array $arguments Arguments provided to the method

@return null|mixed

@throws WireException

## each()

Perform an action upon each item in the WireArray

This is typically used to execute a function for each item, or to build a string
or array from each item.

~~~~~
// Generate navigation list of page children:
echo $page->children()->each(function($child) {
  return "<li><a href='$child->url'>$child->title</a></li>";
});

// If 2 arguments specified to custom function(), 1st is the key, 2nd is the value
echo $page->children()->each(function($key, $child) {
  return "<li><a href='$child->url'>$key: $child->title</a></li>";
});

// Same as above using different method (template string):
echo $page->children()->each("<li><a href='{url}'>{title}</a></li>");

// If WireArray used to hold non-object items, use only {key} and/or {value}
echo $items->each('<li>{key}: {value}</li>');

// Get an array of all "title" properties
$titles = $page->children()->each("title");

// Get array of "title" and "url" properties. Returns an array
// containing an associative array for each item with "title" and "url"
$properties = $page->children()->each(["title", "url"]);
~~~~~


@param callable|string|array|null $func Accepts any of the following:
1. Callable function that each item will be passed to as first argument. If this
   function returns a string, it will be appended to that of the other items and
   the result returned by this each() method.
2. Markup or text string with variable {tags} within it where each {tag} resolves
   to a property in each item. This each() method will return the concatenated result.
3. A property name (string) common to items in this WireArray. The result will be
   returned as an array.
4. An array of property names common to items in this WireArray. The result will be
   returned as an array of associative arrays indexed by property name.

@return array|null|string|WireArray Returns one of the following (related to numbers above):
  - `$this` (1a): WireArray if given a function that has no return values (if using option #1 in arguments).
  - `string` (1b): Containing the concatenated results of all function calls, if your function
    returns strings (if using option #1 in arguments).
  - `string` (2): Returns the processed and concatenated result (string) of all items in your
    template string (if using option #2 in arguments).
  - `array` (3): Returns regular PHP array of the property values for each item you requested
    (if using option #3 in arguments).
  - `array` (4): Returns an array of associative arrays containing the property values for each item
    you requested (if using option #4 in arguments).

@see WireArray::implode(), WireArray::explode()

## slices()

Divide this WireArray into $qty slices and return array of them (each being another WireArray)

This is not destructive to the original WireArray as it returns new WireArray objects.


@param int $qty Number of slices

@return array Array of WireArray objects

## setDuplicateChecking()

Set the current duplicate checking state

Applies only to non-associative WireArray types.

@param bool $value True to enable dup check, false to disable

## __debugInfo()

debugInfo PHP 5.6+ magic method

@return array

## __callStatic()

Static method caller, primarily for support of WireArray::new() method

@param string $name

@param array $arguments

@return WireArray

@throws WireException
