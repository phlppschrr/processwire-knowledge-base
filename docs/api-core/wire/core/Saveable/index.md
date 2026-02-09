# Saveable

Source: `wire/core/Interfaces.php`

## Summary

For classes that are saved to a database or disk.

Common methods:
- [`save()`](method-save.md)
- [`getTableData()`](method-gettabledata.md)

Groups:
Group: [other](group-other.md)

Item must have a gettable/settable 'id' property for this interface as well

## Methods
- [`save()`](method-save.md) Save the object's current state to database.
- [`getTableData(): array`](method-gettabledata.md) Get an array of this item's saveable data, should match exact with the table it saves in
