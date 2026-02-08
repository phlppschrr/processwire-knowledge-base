# $functionsWireAPI->wireDatetime($format = '', $value = ''): WireDateTime|string|int

Source: `wire/core/FunctionsWireAPI.php`

Access the $datetime API variable as a function

~~~~~
// Example usages
$str = datetime()->relativeTimeStr('2016-10-10');
$str = datetime('Y-m-d');
$str = datetime('Y-m-d', time());
~~~~~

## Arguments

- string $format Optional date format
- string|int $value Optional date to format

## Return value

WireDateTime|string|int
