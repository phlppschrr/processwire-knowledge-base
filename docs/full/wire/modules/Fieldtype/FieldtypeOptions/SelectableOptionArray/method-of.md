# $selectableOptionArray->of($of = null): bool

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Get or set output formatting mode

## Usage

~~~~~
// basic usage
$bool = $selectableOptionArray->of();

// usage with all arguments
$bool = $selectableOptionArray->of($of = null);
~~~~~

## Arguments

- `$of` (optional) `bool|null` Omit to retrieve mode, or specify bool to set it

## Return value

- `bool` Current mode. If also setting mode, returns previous mode.
