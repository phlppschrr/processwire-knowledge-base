# WirePaginatable

Source: `wire/core/Interfaces.php`

## Summary

Interface that indicates the object supports its items being paginated

Common methods:
- [`setTotal()`](method-settotal.md)
- [`getTotal()`](method-gettotal.md)
- [`setLimit()`](method-setlimit.md)
- [`getLimit()`](method-getlimit.md)
- [`setStart()`](method-setstart.md)

## Methods
- [`setTotal(int $total): $this`](method-settotal.md) Set the total number of items, if more than are in the WireArray.
- [`getTotal(): int`](method-gettotal.md) Get the total number of items in all paginations of the WireArray.
- [`setLimit(int $numLimit): $this`](method-setlimit.md) Set the limit that was used in pagination.
- [`getLimit(): int`](method-getlimit.md) Get the limit that was used in pagination.
- [`setStart(int $numStart): $this`](method-setstart.md) Set the starting offset that was used for pagination.
- [`getStart(): int`](method-getstart.md) Get the starting offset that was used for pagination.
