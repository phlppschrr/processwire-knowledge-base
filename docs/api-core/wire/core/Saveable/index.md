# Saveable

Source: `wire/core/Interfaces.php`


Groups:
Group: [other](group-other.md)

For classes that are saved to a database or disk.

Item must have a gettable/settable 'id' property for this interface as well

Methods:
- [`save()`](method-save.md) Save the object's current state to database.
- [`getTableData(): array`](method-gettabledata.md) Get an array of this item's saveable data, should match exact with the table it saves in
