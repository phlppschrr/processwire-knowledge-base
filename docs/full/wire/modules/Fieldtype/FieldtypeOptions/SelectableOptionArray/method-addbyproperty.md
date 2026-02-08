# $selectableOptionArray->addByProperty($property, $value): SelectableOption|false

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Add option by property (id, name, title)

## Arguments

- string $property One of id, name or title
- string|int $value Value to match for above property

## Return value

SelectableOption|false Returns option added or false if not found

## Throws

- WireException
