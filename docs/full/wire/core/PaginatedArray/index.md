# PaginatedArray

Source: `wire/core/PaginatedArray.php`

Inherits: `WireArray`
Implements: `WirePaginatable`


Groups:
Group: [other](group-other.md)

ProcessWire Paginated WireArray

Like WireArray, but with the additional methods and properties needed for WirePaginatable interface.

PaginatedArray is a type of WireArray that supports pagination of items within it.
Here you will see methods specific to the pagination aspects of this class only. For full details on
available methods outside of pagination, please see the `WireArray` class. The most common type of
PaginatedArray is a `PageArray`.

Methods:
- [`setTotal(int $total): $this`](method-settotal.md) Set the total number of items, if more than are in the WireArray.
- [`getTotal(): int`](method-gettotal.md) Get the total number of items in the WireArray, including all paginations.
- [`setLimit(int $numLimit): $this`](method-setlimit.md) Set the limit that was used in pagination.
- [`getLimit(): int`](method-getlimit.md) Get the limit that was used in pagination.
- [`setStart(int $numStart): $this`](method-setstart.md) Set the starting offset number to use for pagination.
- [`getStart(): int`](method-getstart.md) Get the starting offset number that was used for pagination.
- [`hasPagination(): bool`](method-haspagination.md) Does this WireArray have more than one pagination?
- [`hasNextPagination(): bool`](method-hasnextpagination.md) Is there a next pagination containing more items in this PaginatedArray after the current one?
- [`hasPrevPagination(): bool`](method-hasprevpagination.md) Is there a previous pagination before the current one?
- [`getProperty(string $property): mixed`](method-getproperty.md) Get a property of the PageArray
- [`getPaginationString(string|array $label = '', bool|array $usePageNum = false): string`](method-getpaginationstring.md) Get a "1 to 10 of 50" type of string useful for pagination headlines.
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
