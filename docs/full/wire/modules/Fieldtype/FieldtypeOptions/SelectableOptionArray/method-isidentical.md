# $selectableOptionArray->isIdentical(WireArray $items, $strict = true): bool

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Is the given WireArray identical to this one?

## Usage

~~~~~
// basic usage
$bool = $selectableOptionArray->isIdentical($items);

// usage with all arguments
$bool = $selectableOptionArray->isIdentical(WireArray $items, $strict = true);
~~~~~

## Arguments

- `$items` `WireArray`
- `$strict` (optional) `bool|int`

## Return value

- `bool`
