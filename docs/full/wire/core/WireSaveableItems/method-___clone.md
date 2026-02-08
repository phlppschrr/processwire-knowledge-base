# $wireSaveableItems->___clone(Saveable $item, $name = ''): bool|Saveable

Source: `wire/core/WireSaveableItems.php`

Create and return a cloned copy of this item

If no name is specified and the new item uses a 'name' field, it will contain a number at the end to make it unique

## Arguments

- Saveable $item Item to clone
- string $name Optionally specify new name

## Return value

bool|Saveable $item Returns the new clone on success, or false on failure
