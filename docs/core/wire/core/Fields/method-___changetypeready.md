# $fields->changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

Source: `wire/core/Fields.php`

Hook called right before a field is about to change type

## Usage

~~~~~
// basic usage
$result = $fields->changeTypeReady($item, $fromType, $toType);

// usage with all arguments
$result = $fields->changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType);
~~~~~

## Hookable

- Hookable method name: `changeTypeReady`
- Implementation: `___changeTypeReady`
- Hook with: `$fields->changeTypeReady()`

## Arguments

- `$item` `Field`
- `$fromType` `Fieldtype`
- `$toType` `Fieldtype`
