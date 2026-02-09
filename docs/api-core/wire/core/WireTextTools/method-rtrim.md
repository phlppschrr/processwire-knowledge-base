# $wireTextTools->rtrim($str, $chars = ''): string

Source: `wire/core/WireTextTools.php`

Strip whitespace (or other characters) from the end of string only (aka right trim)

## Usage

~~~~~
// basic usage
$string = $wireTextTools->rtrim($str);

// usage with all arguments
$string = $wireTextTools->rtrim($str, $chars = '');
~~~~~

## Arguments

- `$str` `string`
- `$chars` (optional) `string` Omit for default

## Return value

- `string`

## Since

3.0.168
