# $selectableOptionArray->addByProperty($property, $value): SelectableOption|false

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Add option by property (id, name, title)

## Usage

~~~~~
// basic usage
$selectableOption = $selectableOptionArray->addByProperty($property, $value);
~~~~~

## Arguments

- `$property` `string` One of id, name or title
- `$value` `string|int` Value to match for above property

## Return value

- `SelectableOption|false` Returns option added or false if not found

## Exceptions

- `WireException`
