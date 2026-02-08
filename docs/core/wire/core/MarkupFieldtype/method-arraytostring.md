# $markupFieldtype->arrayToString($value, $encode = true): string

Source: `wire/core/MarkupFieldtype.php`

Render an unknown array or WireArray to a string

## Usage

~~~~~
// basic usage
$string = $markupFieldtype->arrayToString($value);

// usage with all arguments
$string = $markupFieldtype->arrayToString($value, $encode = true);
~~~~~

## Arguments

- `$value` `array|WireArray`
- `$encode` (optional) `bool`

## Return value

- `string`
