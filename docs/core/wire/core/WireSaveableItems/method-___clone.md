# $wireSaveableItems->___clone(Saveable $item, $name = ''): bool|Saveable

Source: `wire/core/WireSaveableItems.php`

Create and return a cloned copy of this item

If no name is specified and the new item uses a 'name' field, it will contain a number at the end to make it unique

## Arguments

- `$item` `Saveable` Item to clone
- `$name` (optional) `string` Optionally specify new name

## Return value

bool|Saveable $item Returns the new clone on success, or false on failure
