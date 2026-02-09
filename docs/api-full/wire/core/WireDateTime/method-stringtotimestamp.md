# $wireDateTime->stringToTimestamp($str, $format): int

Source: `wire/core/WireDateTime.php`

Given a date/time string and expected format, convert it to a unix timestamp

## Usage

~~~~~
// basic usage
$int = $wireDateTime->stringToTimestamp($str, $format);
~~~~~

## Arguments

- `$str` `string` Date/time string
- `$format` `string` Format of the date/time string in PHP date syntax

## Return value

- `int` Unix timestamp
