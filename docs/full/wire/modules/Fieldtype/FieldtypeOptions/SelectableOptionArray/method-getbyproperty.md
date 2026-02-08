# $selectableOptionArray->getByProperty($property, $value, $noValue = false): bool|null|SelectableOption

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Get SelectableOption by $property matching $value, or boolean false if not found

## Arguments

- `$property` `string` May be "title", "value" or "id"
- `$value` `string|int`
- `$noValue` (optional) `bool|null` Value to return if option not present (default=false)

## Return value

bool|null|SelectableOption
