# $wireTextTools->ltrim($str, $chars = ''): string

Source: `wire/core/WireTextTools.php`

Strip whitespace (or other characters) from the beginning of string only (aka left trim)

## Usage

~~~~~
// basic usage
$string = $wireTextTools->ltrim($str);

// usage with all arguments
$string = $wireTextTools->ltrim($str, $chars = '');
~~~~~

## Arguments

- `$str` `string`
- `$chars` (optional) `string` Omit for default

## Return value

- `string`

## Since

3.0.168
