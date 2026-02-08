# $fieldtype->getConfigArray(Field $field): array

Source: `wire/core/Fieldtype.php`

Same as getConfigInputfields but with definition as an array instead

If both getConfigInputfields and getConfigInputfieldsArray are implemented then
definitions from both will be used. It's probably simplest just to implement one
or the other.

## Usage

~~~~~
// basic usage
$array = $fieldtype->getConfigArray($field);

// usage with all arguments
$array = $fieldtype->getConfigArray(Field $field);
~~~~~

## Hookable

- Hookable method name: `getConfigArray`
- Implementation: `___getConfigArray`
- Hook with: `$fieldtype->getConfigArray()`

## Arguments

- `$field` `Field`

## Return value

- `array`
