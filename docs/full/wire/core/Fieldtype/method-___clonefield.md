# $fieldtype->cloneField(Field $field): Field

Source: `wire/core/Fieldtype.php`

Return a cloned copy of $field

## Usage

~~~~~
// basic usage
$field = $fieldtype->cloneField($field);

// usage with all arguments
$field = $fieldtype->cloneField(Field $field);
~~~~~

## Hookable

- Hookable method name: `cloneField`
- Implementation: `___cloneField`
- Hook with: `$fieldtype->cloneField()`

## Arguments

- `$field` `Field`

## Return value

- `Field` cloned copy
