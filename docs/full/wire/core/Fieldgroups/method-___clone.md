# $fieldgroups->___clone(Saveable $item, $name = ''): Fieldgroup|false

Source: `wire/core/Fieldgroups.php`

Create and return a cloned copy of this item

If the new item uses a 'name' field, it will contain a number at the end to make it unique

## Arguments

- Saveable $item Item to clone
- string $name

## Return value

Fieldgroup|false $item Returns the new clone on success, or false on failure
