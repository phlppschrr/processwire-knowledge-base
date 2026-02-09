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
Method: [setTotal()](method-settotal.md)
Method: [getTotal()](method-gettotal.md)
Method: [setLimit()](method-setlimit.md)
Method: [getLimit()](method-getlimit.md)
Method: [setStart()](method-setstart.md)
Method: [getStart()](method-getstart.md)
Method: [hasPagination()](method-haspagination.md)
Method: [hasNextPagination()](method-hasnextpagination.md)
Method: [hasPrevPagination()](method-hasprevpagination.md)
Method: [getProperty()](method-getproperty.md)
Method: [getPaginationString()](method-getpaginationstring.md)
Method: [__debugInfo()](method-__debuginfo.md)
