# $inputfieldDatetimeType->sanitizeValue($value): int|string

Source: `wire/modules/Inputfield/InputfieldDatetime/InputfieldDatetimeType.php`

Sanitize value to unix timestamp integer or blank string (to represent no value)

## Usage

~~~~~
// basic usage
$int = $inputfieldDatetimeType->sanitizeValue($value);
~~~~~

## Arguments

- `$value` `string|int`

## Return value

- `int|string`
