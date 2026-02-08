# $fields->clone(Saveable $item, $name = ''): Field

Source: `wire/core/Fields.php`

Create and return a cloned copy of the given Field

## Usage

~~~~~
// basic usage
$field = $fields->clone($item);

// usage with all arguments
$field = $fields->clone(Saveable $item, $name = '');
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$fields->clone()`

## Arguments

- `$item` `Field` Field to clone
- `$name` (optional) `string` Optionally specify name for new cloned item

## Return value

- `Field` $item Returns the new clone on success, or false on failure
