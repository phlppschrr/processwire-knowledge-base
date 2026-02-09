# WireArray

Source: `wire/core/WireArray.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `ArrayAccess`, `Countable`


Groups:
Group: [other](group-other.md)

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

Methods:
- [`__construct()`](method-__construct.md)
- [`isValidItem(mixed $item): bool`](method-isvaliditem.md)
- [`isValidKey(string|int $key): bool`](method-isvalidkey.md)
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md)
- [`import(array|WireArray $items): $this`](method-import.md)
- [`add(int|string|array|object|Wire|WireArray $item): $this`](method-add.md)
- [`_insert(int|string|array|object $item, int|string|array|object $existingItem, bool $insertBefore = true): $this`](method-_insert.md)
- [`insertBefore(Wire|string|int $item, Wire|string|int $existingItem): $this`](method-insertbefore.md)
- [`insertAfter(Wire|string|int $item, Wire|string|int $existingItem): $this`](method-insertafter.md)
- [`replace(Wire|string|int $itemA, Wire|string|int $itemB): $this`](method-replace.md)
- [`set(int|string $key, int|string|array|object|Wire $value): $this`](method-set.md)
- [`__set(int|string $property, $value)`](method-__set.md)
- [`__isset(string|int $key): bool`](method-__isset.md)
- [`__unset(int|string $key)`](method-__unset.md)
- [`setArray(array|WireArray $data): $this`](method-setarray.md)
- [`get(int|string|array $key): WireData|Page|mixed|array|null`](method-get.md)
- [`__get(int|string $name): Wire|WireData|Page|mixed|bool`](method-__get.md)
- [`getProperty(string $property): Wire|mixed`](method-getproperty.md)
- [`getItemThatMatches(string $key, string|int|object $value): Wire|null`](method-getitemthatmatches.md)
- [`has(int|string|Wire $key): bool`](method-has.md)
- [`getArray(): array`](method-getarray.md)
- [`getAll(): $this`](method-getall.md)
- [`getKeys(): array`](method-getkeys.md)
- [`getValues(): array|Wire[]`](method-getvalues.md)
- [`getRandom(int $num = 1, bool $alwaysArray = false): WireArray|Wire|mixed|null`](method-getrandom.md)
- [`findRandom(int $num): WireArray`](method-findrandom.md)
- [`findRandomTimed(int $num, int|string $seed = 'Ymd'): WireArray`](method-findrandomtimed.md)
- [`slice(int $start, int $limit = 0): WireArray`](method-slice.md)
- [`prepend(Wire|WireArray|mixed $item): $this`](method-prepend.md)
- [`append(Wire|WireArray|mixed $item): $this`](method-append.md)
- [`unshift(Wire|WireArray|mixed $item): $this`](method-unshift.md)
- [`shift(): Wire|mixed|null`](method-shift.md)
- [`push(Wire|mixed $item): $this`](method-push.md)
- [`pop(): Wire|mixed|null`](method-pop.md)
- [`shuffle(): $this`](method-shuffle.md)
- [`index(int $num): WireArray`](method-index.md)
- [`eq(int $num): Wire|null`](method-eq.md)
- [`first(): Wire|mixed|bool`](method-first.md)
- [`last(): Wire|mixed|bool`](method-last.md)
- [`remove(int|string|Wire $key): $this`](method-remove.md)
- [`removeItems(array|Wire|string|WireArray $items): $this`](method-removeitems.md)
- [`removeAll(): $this`](method-removeall.md)
- [`sort(string|array $properties, int|null $flags = null): $this`](method-sort.md)
- [`_sort(string|array $properties, int $numNeeded = null): $this`](method-_sort.md)
- [`sortFlags(bool $sortFlags = false): int`](method-sortflags.md)
- [`stableSort(&$data, array $properties, int $numNeeded = null): array`](method-stablesort.md)
- [`getItemPropertyValue(Wire $item, string $property): mixed`](method-getitempropertyvalue.md)
- [`filterData(string|array|Selectors $selectors, bool|int $not = false): $this`](method-filterdata.md)
- [`filterDataSelectors(Selectors $selectors)`](method-filterdataselectors.md)
- [`filter(string|array|Selectors $selector): $this`](method-filter.md)
- [`not(string|array|Selectors $selector): $this`](method-not.md)
- [`find(string|array|Selectors $selector): WireArray`](method-find.md)
- [`findOne(string|array|Selectors $selector): Wire|bool`](method-findone.md)
- [`iterable(mixed $item): bool`](method-iterable.md)
- [`getIterator(): \ArrayObject|Wire[]`](method-getiterator.md)
- [`count(): int`](method-count.md)
- [`__toString(): string`](method-__tostring.md)
- [`reverse(): WireArray`](method-reverse.md)
- [`unique(int $sortFlags = SORT_STRING): WireArray`](method-unique.md)
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md)
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md)
- [`getItemsAdded(): array|Wire[]`](method-getitemsadded.md)
- [`getItemsRemoved(): array|Wire[]`](method-getitemsremoved.md)
- [`getNext(Wire $item, bool $strict = true): Wire|null`](method-getnext.md)
- [`getPrev(Wire $item, bool $strict = true): Wire|null`](method-getprev.md)
- [`implode(string $delimiter, string|callable $property = '', array $options = array()): string`](method-implode.md)
- [`explode(string|callable|array $property = '', array $options = array()): array`](method-explode.md)
- [`and(Wire|WireArray $item): WireArray`](method-___and.md) (hookable)
- [`data(string|null|array|bool $key = null, mixed|null|bool $value = null): WireArray|mixed|array|null`](method-data.md)
- [`removeData(string $key): $this`](method-removedata.md)
- [`__invoke(string $key): mixed`](method-__invoke.md)
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable)
- [`each(callable|string|array|null $func = null): array|null|string|WireArray`](method-each.md)
- [`slices(int $qty): array`](method-slices.md)
- [`setDuplicateChecking(bool $value)`](method-setduplicatechecking.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`__callStatic(string $name, array $arguments): WireArray`](method-__callstatic.md)
