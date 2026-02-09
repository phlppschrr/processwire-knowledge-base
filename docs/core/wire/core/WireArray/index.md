# WireArray

Source: `wire/core/WireArray.php`

ProcessWire WireArray

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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [isValidItem()](method-isvaliditem.md)
Method: [isValidKey()](method-isvalidkey.md)
Method: [isIdentical()](method-isidentical.md)
Method: [import()](method-import.md)
Method: [add()](method-add.md)
Method: [_insert()](method-_insert.md)
Method: [insertBefore()](method-insertbefore.md)
Method: [insertAfter()](method-insertafter.md)
Method: [replace()](method-replace.md)
Method: [set()](method-set.md)
Method: [__set()](method-__set.md)
Method: [__isset()](method-__isset.md)
Method: [__unset()](method-__unset.md)
Method: [setArray()](method-setarray.md)
Method: [get()](method-get.md)
Method: [__get()](method-__get.md)
Method: [getProperty()](method-getproperty.md)
Method: [getItemThatMatches()](method-getitemthatmatches.md)
Method: [has()](method-has.md)
Method: [getArray()](method-getarray.md)
Method: [getAll()](method-getall.md)
Method: [getKeys()](method-getkeys.md)
Method: [getValues()](method-getvalues.md)
Method: [getRandom()](method-getrandom.md)
Method: [findRandom()](method-findrandom.md)
Method: [findRandomTimed()](method-findrandomtimed.md)
Method: [slice()](method-slice.md)
Method: [prepend()](method-prepend.md)
Method: [append()](method-append.md)
Method: [unshift()](method-unshift.md)
Method: [shift()](method-shift.md)
Method: [push()](method-push.md)
Method: [pop()](method-pop.md)
Method: [shuffle()](method-shuffle.md)
Method: [index()](method-index.md)
Method: [eq()](method-eq.md)
Method: [first()](method-first.md)
Method: [last()](method-last.md)
Method: [remove()](method-remove.md)
Method: [removeItems()](method-removeitems.md)
Method: [removeAll()](method-removeall.md)
Method: [sort()](method-sort.md)
Method: [_sort()](method-_sort.md)
Method: [sortFlags()](method-sortflags.md)
Method: [stableSort()](method-stablesort.md)
Method: [getItemPropertyValue()](method-getitempropertyvalue.md)
Method: [filterData()](method-filterdata.md)
Method: [filterDataSelectors()](method-filterdataselectors.md)
Method: [filter()](method-filter.md)
Method: [not()](method-not.md)
Method: [find()](method-find.md)
Method: [findOne()](method-findone.md)
Method: [iterable()](method-iterable.md)
Method: [getIterator()](method-getiterator.md)
Method: [count()](method-count.md)
Method: [__toString()](method-__tostring.md)
Method: [reverse()](method-reverse.md)
Method: [unique()](method-unique.md)
Method: [trackAdd()](method-trackadd.md)
Method: [trackRemove()](method-trackremove.md)
Method: [getItemsAdded()](method-getitemsadded.md)
Method: [getItemsRemoved()](method-getitemsremoved.md)
Method: [getNext()](method-getnext.md)
Method: [getPrev()](method-getprev.md)
Method: [implode()](method-implode.md)
Method: [explode()](method-explode.md)
Method: [and()](method-___and.md) (hookable)
Method: [data()](method-data.md)
Method: [removeData()](method-removedata.md)
Method: [__invoke()](method-__invoke.md)
Method: [callUnknown()](method-___callunknown.md) (hookable)
Method: [each()](method-each.md)
Method: [slices()](method-slices.md)
Method: [setDuplicateChecking()](method-setduplicatechecking.md)
Method: [__debugInfo()](method-__debuginfo.md)
Method: [__callStatic()](method-__callstatic.md)
