# PaginatedArray

Source: `wire/core/PaginatedArray.php`

ProcessWire Paginated WireArray

Like WireArray, but with the additional methods and properties needed for WirePaginatable interface.

PaginatedArray is a type of WireArray that supports pagination of items within it.
Here you will see methods specific to the pagination aspects of this class only. For full details on
available methods outside of pagination, please see the `WireArray` class. The most common type of
PaginatedArray is a `PageArray`.
In most cases you will not need these manipulation methods as core API calls already take care of this.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method string renderPager(array $options = array()) Renders pagination, when MarkupPageArray module installed

## setTotal()

Set the total number of items, if more than are in the WireArray.


@param int $total

@return $this

## getTotal()

Get the total number of items in the WireArray, including all paginations.

If no limit is used, this returns total number of items currently in the WireArray,
which would be the same as the `WireArray::count()` value. But when a limit is
used, this number will typically be larger than the count, as it includes all
items across all paginations, whether currently present or not.


@return int Total number of items across all paginations.

## setLimit()

Set the limit that was used in pagination.


@param int $numLimit

@return $this

## getLimit()

Get the limit that was used in pagination.

If no limit was set, then it returns the number of items currently in this WireArray.


@return int

## setStart()

Set the starting offset number to use for pagination.

This is typically the current page number (minus 1) multiplied by limit setting.


@param int $numStart

@return $this

## getStart()

Get the starting offset number that was used for pagination.


@return int

## hasPagination()

Does this WireArray have more than one pagination?


@return bool

@since 3.0.120

## hasNextPagination()

Is there a next pagination containing more items in this PaginatedArray after the current one?


@return bool

@since 3.0.120

## hasPrevPagination()

Is there a previous pagination before the current one?


@return bool

@since 3.0.120

## getProperty()

Get a property of the PageArray

These map to functions from the array and are here for convenience.
Properties include count, total, start, limit, last, first, keys, values,
These can also be accessed by direct reference, i.e. `$items->limit`.

Please see the `WireArray::getProperty()` method for full details on
non-pagination related properties that can be retrieved through this.


@param string $property Name of property you want to retrieve, can be any of the following:
  - `count` (int): Count of items currently present.
  - `total` (int): Total quantity of items across all paginations.
  - `start` (int): Current start index for pagination.
  - `limit` (int): Current limit used for pagination.
  - `last` (mixed): Last item in the WireArray.
  - `first` (mixed): First item in the WireArray.

@return mixed Value of requested property.

## getPaginationString()

Get a "1 to 10 of 50" type of string useful for pagination headlines.

This returns a string of `1 to 10 of 30` (items) or `1 of 10` (pages) for example.

Since 3.0.108 you can optionally replace either of the arguments with an $options o
array instead, and you can specify any of these options:

 - `label` (string): Label to use for items, same as $label argument (default='').
 - `zeroLabel` (string): Alternate label to use if there are zero items, since 3.0.127 (default='').
 - `usePageNum` (bool): Specify true to show page numbers rather than item numbers (default=false).
 - `count` (int): Use this count rather than count in this PaginatedArray (default=-1, disabled).
 - `start` (int): Use this start rather than start in this PaginatedArray (default=-1, disabled).
 - `limit` (int): Use this limit rather than limit in this PaginatedArray (default=-1, disabled).
 - `total` (int): Use this total rather than total in this PaginatedArray (default=-1, disabled).

~~~~~
// Get string like "Items 1 to 25 of 500"
echo $items->getPaginationString('Items');

// Get string like "Page 1 of 10"
echo $items->getPaginationString('Page', true);

// Get string where you specify all options
echo $items->getPaginationString(array(
  'label' => 'Items',
  'zeroLabel' => 'No items found', // 3.0.127+ only
  'usePageNum' => false,
  'count' => 10,
  'start' => 0,
  'limit' => 10,
  'total' => 100
));
~~~~~


@param string|array $label Label to identify item type, i.e. "Items" or "Page", etc. (default=empty).

@param bool|array $usePageNum Specify true to show page numbers rather than item numbers (default=false).

@return string Formatted string

## __debugInfo()

debugInfo PHP 5.6+ magic method

@return array
