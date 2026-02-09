# $wireDateTime->convertDateFormat($format, $type): string

Source: `wire/core/WireDateTime.php`

Given a PHP date() format, convert it to either 'js', 'strftime' or 'regex' format

## Usage

~~~~~
// basic usage
$string = $wireDateTime->convertDateFormat($format, $type);
~~~~~

## Arguments

- `$format` `string` PHP date() format
- `$type` `string` New format to convert to: either 'js', 'strftime', or 'regex'

## Return value

- `string`
