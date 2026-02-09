# $imageSizerEngine->getBooleanValue($value): bool

Source: `wire/core/ImageSizerEngine.php`

Given a value, convert it to a boolean.

Value can be string representations like: 0, 1 off, on, yes, no, y, n, false, true.

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->getBooleanValue($value);
~~~~~

## Arguments

- `$value` `bool|int|string`

## Return value

- `bool`
