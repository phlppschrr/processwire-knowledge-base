# $fieldgroups->clone(Saveable $item, $name = ''): Fieldgroup|false

Source: `wire/core/Fieldgroups.php`

Create and return a cloned copy of this item

If the new item uses a 'name' field, it will contain a number at the end to make it unique

## Usage

~~~~~
// basic usage
$fieldgroup = $fieldgroups->clone($item);

// usage with all arguments
$fieldgroup = $fieldgroups->clone(Saveable $item, $name = '');
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$fieldgroups->clone()`

## Arguments

- `$item` `Saveable` Item to clone
- `$name` (optional) `string`

## Return value

- `Fieldgroup|false` $item Returns the new clone on success, or false on failure
