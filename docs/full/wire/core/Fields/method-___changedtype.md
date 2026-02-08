# $fields->changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

Source: `wire/core/Fields.php`

Hook called when a field has changed type

## Usage

~~~~~
// basic usage
$result = $fields->changedType($item, $fromType, $toType);

// usage with all arguments
$result = $fields->changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType);
~~~~~

## Hookable

- Hookable method name: `changedType`
- Implementation: `___changedType`
- Hook with: `$fields->changedType()`

## Arguments

- `$item` `Field`
- `$fromType` `Fieldtype`
- `$toType` `Fieldtype`
