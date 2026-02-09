# WireArray

Source: `wire/core/WireArray.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `ArrayAccess`, `Countable`

## Summary

ProcessWire WireArray

Common methods:
- [`isValidItem()`](method-isvaliditem.md)
- [`isValidKey()`](method-isvalidkey.md)
- [`isIdentical()`](method-isidentical.md)
- [`getItemKey()`](method-getitemkey.md)
- [`makeBlankItem()`](method-makeblankitem.md)

Groups:
Group: [other](group-other.md)

WireArray is the base array access object used in the ProcessWire framework.

Several methods are duplicated here for syntactical convenience and jQuery-like usability.
Many methods act upon the array and return $this, which enables WireArrays to be used for fluent interfaces.
WireArray is the base of the PageArray (subclass) which is the most used instance.

@todo can we implement next() and prev() like on Page, as alias to getNext() and getPrev()?



WireArray is the base iterable array type used throughout the ProcessWire framework.

**Nearly all collections of items in ProcessWire are derived from the WireArray type.**
This includes collections of pages, fields, templates, modules and more. As a result, the WireArray class is one
you will be interacting with regularly in the ProcessWire API, whether you know it or not.

Below are all the public methods you can use to interact with WireArray types in ProcessWire. In addition to these
methods, you can also treat WireArray types like regular PHP arrays, in that you can `foreach()` them and get or
set elements using array syntax, i.e. `$value = $items[$key];` to get an item or `$items[] = $item;` to add an item.

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`isValidItem(mixed $item): bool`](method-isvaliditem.md) Is the given item valid for storange in this array?
- [`isValidKey(string|int $key): bool`](method-isvalidkey.md) Is the given item key valid for use in this array?
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md) Is the given WireArray identical to this one?
- [`import(array|WireArray $items): $this`](method-import.md) Import the given item(s) into this WireArray.
- [`add(int|string|array|object|Wire|WireArray $item): $this`](method-add.md) Add an item to the end of the WireArray.
- [`_insert(int|string|array|object $item, int|string|array|object $existingItem, bool $insertBefore = true): $this`](method-_insert.md) Insert an item either before or after another
- [`insertBefore(Wire|string|int $item, Wire|string|int $existingItem): $this`](method-insertbefore.md) Insert an item before an existing item
- [`insertAfter(Wire|string|int $item, Wire|string|int $existingItem): $this`](method-insertafter.md) Insert an item after an existing item
- [`replace(Wire|string|int $itemA, Wire|string|int $itemB): $this`](method-replace.md) Replace one item with the other
- [`set(int|string $key, int|string|array|object|Wire $value): $this`](method-set.md) Set an item by key in the WireArray.
- [`__set(int|string $property, $value)`](method-__set.md) Enables setting of WireArray elements in object notation.
- [`__isset(string|int $key): bool`](method-__isset.md) Ensures that isset() and empty() work for this classes properties.
- [`__unset(int|string $key)`](method-__unset.md) Ensures that unset() works for this classes data.
- [`setArray(array|WireArray $data): $this`](method-setarray.md) Like set() but accepts an array or WireArray to set multiple values at once
- [`get(int|string|array $key): WireData|Page|mixed|array|null`](method-get.md) Returns the value of the item at the given index, or null if not set.
- [`__get(int|string $name): Wire|WireData|Page|mixed|bool`](method-__get.md) Enables derefencing of WireArray elements in object notation.
- [`getProperty(string $property): Wire|mixed`](method-getproperty.md) Get a predefined property of the array, or extra data that has been set.
- [`getItemThatMatches(string $key, string|int|object $value): Wire|null`](method-getitemthatmatches.md) Return the first item in this WireArray having a property named $key with $value, or NULL if not found.
- [`has(int|string|Wire $key): bool`](method-has.md) Does this WireArray have the given item, index, or match the given selector?
- [`getArray(): array`](method-getarray.md) Get a PHP array of all the items in this WireArray with original keys maintained
- [`getAll(): $this`](method-getall.md) Returns all items in the WireArray (for syntax convenience)
- [`getKeys(): array`](method-getkeys.md) Returns a regular PHP array of all keys used in this WireArray.
- [`getValues(): array|Wire[]`](method-getvalues.md) Returns a regular PHP array of all values used in this WireArray.
- [`getRandom(int $num = 1, bool $alwaysArray = false): WireArray|Wire|mixed|null`](method-getrandom.md) Get a random item from this WireArray.
- [`findRandom(int $num): WireArray`](method-findrandom.md) Find a specified quantity of random elements from this WireArray.
- [`findRandomTimed(int $num, int|string $seed = 'Ymd'): WireArray`](method-findrandomtimed.md) Find a quantity of random elements from this WireArray based on a timed interval (or user provided seed).
- [`slice(int $start, int $limit = 0): WireArray`](method-slice.md) Get a slice of the WireArray.
- [`prepend(Wire|WireArray|mixed $item): $this`](method-prepend.md) Prepend an item to the beginning of the WireArray.
- [`append(Wire|WireArray|mixed $item): $this`](method-append.md) Append an item to the end of the WireArray
- [`unshift(Wire|WireArray|mixed $item): $this`](method-unshift.md) Unshift an element to the beginning of the WireArray (alias for prepend)
- [`shift(): Wire|mixed|null`](method-shift.md) Shift an element off the beginning of the WireArray and return it
- [`push(Wire|mixed $item): $this`](method-push.md) Push an item to the end of the WireArray.
- [`pop(): Wire|mixed|null`](method-pop.md) Pop an element off the end of the WireArray and return it
- [`shuffle(): $this`](method-shuffle.md) Shuffle/randomize this WireArray
- [`index(int $num): WireArray`](method-index.md) Returns a new WireArray of the item at the given index.
- [`eq(int $num): Wire|null`](method-eq.md) Returns the item at the given index starting from 0, or NULL if it doesn't exist.
- [`first(): Wire|mixed|bool`](method-first.md) Returns the first item in the WireArray or boolean false if empty.
- [`last(): Wire|mixed|bool`](method-last.md) Returns the last item in the WireArray or boolean false if empty.
- [`remove(int|string|Wire $key): $this`](method-remove.md) Removes the given item or index from the WireArray (if it exists).
- [`removeItems(array|Wire|string|WireArray $items): $this`](method-removeitems.md) Removes multiple identified items at once
- [`removeAll(): $this`](method-removeall.md) Removes all items from the WireArray, leaving it blank
- [`sort(string|array $properties, int|null $flags = null): $this`](method-sort.md) Sort this WireArray by the given properties.
- [`_sort(string|array $properties, int $numNeeded = null): $this`](method-_sort.md) Sort this WireArray by the given properties (internal use)
- [`sortFlags(bool $sortFlags = false): int`](method-sortflags.md) Get or set sort flags that affect behavior of any sorting functions
- [`stableSort(&$data, array $properties, int $numNeeded = null): array`](method-stablesort.md) Sort given array by first given property.
- [`getItemPropertyValue(Wire $item, string $property): mixed`](method-getitempropertyvalue.md) Get the value of $property from $item
- [`filterData(string|array|Selectors $selectors, bool|int $not = false): $this`](method-filterdata.md) Filter out Wires that don't match the selector.
- [`filterDataSelectors(Selectors $selectors)`](method-filterdataselectors.md) Prepare selectors for filtering
- [`filter(string|array|Selectors $selector): $this`](method-filter.md) Filter this WireArray to only include items that match the given selector (destructive)
- [`not(string|array|Selectors $selector): $this`](method-not.md) Filter this WireArray to only include items that DO NOT match the selector (destructive)
- [`find(string|array|Selectors $selector): WireArray`](method-find.md) Find all items in this WireArray that match the given selector.
- [`findOne(string|array|Selectors $selector): Wire|bool`](method-findone.md) Find a single item by selector
- [`iterable(mixed $item): bool`](method-iterable.md) Determines if the given item iterable as an array.
- [`getIterator(): \ArrayObject|Wire[]`](method-getiterator.md) Allows iteration of the WireArray.
- [`count(): int`](method-count.md) Returns the number of items in this WireArray.
- [`__toString(): string`](method-__tostring.md) Returns a string representation of this WireArray.
- [`reverse(): WireArray`](method-reverse.md) Return a new reversed version of this WireArray.
- [`unique(int $sortFlags = SORT_STRING): WireArray`](method-unique.md) Return a new array that is unique (no two of the same elements)
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md) Track an item added
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md) Track an item removed
- [`getItemsAdded(): array|Wire[]`](method-getitemsadded.md) Return array of all items added to this WireArray (while change tracking is enabled)
- [`getItemsRemoved(): array|Wire[]`](method-getitemsremoved.md) Return array of all items removed from this WireArray (when change tracking is enabled)
- [`getNext(Wire $item, bool $strict = true): Wire|null`](method-getnext.md) Given an item, get the item that comes after it in the WireArray
- [`getPrev(Wire $item, bool $strict = true): Wire|null`](method-getprev.md) Given an item, get the item before it in the WireArray
- [`implode(string $delimiter, string|callable $property = '', array $options = array()): string`](method-implode.md) Combine all elements into a delimiter-separated string containing the given property from each item
- [`explode(string|callable|array $property = '', array $options = array()): array`](method-explode.md) Return a plain array of the requested property from each item
- [`and(Wire|WireArray $item): WireArray`](method-___and.md) (hookable) Return a new copy of this WireArray with the given item(s) appended
- [`data(string|null|array|bool $key = null, mixed|null|bool $value = null): WireArray|mixed|array|null`](method-data.md) Store or retrieve an extra data value in this WireArray
- [`removeData(string $key): $this`](method-removedata.md) Remove a property/value previously set with the WireArray::data() method.
- [`__invoke(string $key): mixed`](method-__invoke.md) Enables use of $var('key')
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable) Handler for when an unknown/unhooked method call is executed
- [`each(callable|string|array|null $func = null): array|null|string|WireArray`](method-each.md) Perform an action upon each item in the WireArray
- [`slices(int $qty): array`](method-slices.md) Divide this WireArray into $qty slices and return array of them (each being another WireArray)
- [`setDuplicateChecking(bool $value)`](method-setduplicatechecking.md) Set the current duplicate checking state
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
- [`__callStatic(string $name, array $arguments): WireArray`](method-__callstatic.md) Static method caller, primarily for support of WireArray::new() method
