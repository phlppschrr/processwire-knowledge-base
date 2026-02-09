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
- [`setTotal(int $total): $this`](method-settotal.md)
- [`getTotal(): int`](method-gettotal.md)
- [`setLimit(int $numLimit): $this`](method-setlimit.md)
- [`getLimit(): int`](method-getlimit.md)
- [`setStart(int $numStart): $this`](method-setstart.md)
- [`getStart(): int`](method-getstart.md)
- [`hasPagination(): bool`](method-haspagination.md)
- [`hasNextPagination(): bool`](method-hasnextpagination.md)
- [`hasPrevPagination(): bool`](method-hasprevpagination.md)
- [`getProperty(string $property): mixed`](method-getproperty.md)
- [`getPaginationString(string|array $label = '', bool|array $usePageNum = false): string`](method-getpaginationstring.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
