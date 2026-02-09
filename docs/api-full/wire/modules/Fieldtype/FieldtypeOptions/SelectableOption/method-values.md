# $selectableOption->values($returnHash = false): string|array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOption.php`

Return all values stored in this SelectableOption

## Usage

~~~~~
// basic usage
$string = $selectableOption->values();

// usage with all arguments
$string = $selectableOption->values($returnHash = false);
~~~~~

## Arguments

- `$returnHash` (optional) `bool` Makes it return a string hash of all values

## Return value

- `string|array`
