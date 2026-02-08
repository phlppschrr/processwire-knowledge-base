# $wireSaveableItems->encodeData(array $value): string

Source: `wire/core/WireSaveableItems.php`

Encode the 'data' portion of the table.

This is a front-end to wireEncodeJSON so that it can be overridden if needed.

## Usage

~~~~~
// basic usage
$string = $wireSaveableItems->encodeData($value);

// usage with all arguments
$string = $wireSaveableItems->encodeData(array $value);
~~~~~

## Arguments

- `$value` `array`

## Return value

- `string`
