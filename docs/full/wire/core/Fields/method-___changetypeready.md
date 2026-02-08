# $fields->___changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

Source: `wire/core/Fields.php`

Hook called right before a field is about to change type

## Usage

~~~~~
// basic usage
$result = $fields->___changeTypeReady($item, $fromType, $toType);

// usage with all arguments
$result = $fields->___changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType);
~~~~~

## Arguments

- `$item` `Field`
- `$fromType` `Fieldtype`
- `$toType` `Fieldtype`
