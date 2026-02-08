# $fields->___changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

Source: `wire/core/Fields.php`

Hook called when a field has changed type

## Usage

~~~~~
// basic usage
$result = $fields->___changedType($item, $fromType, $toType);

// usage with all arguments
$result = $fields->___changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType);
~~~~~

## Arguments

- `$item` `Field`
- `$fromType` `Fieldtype`
- `$toType` `Fieldtype`
