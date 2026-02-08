# FunctionsWireAPI::wireDatetime()

Source: `wire/core/FunctionsWireAPI.php`

Access the $datetime API variable as a function

~~~~~
// Example usages
$str = datetime()->relativeTimeStr('2016-10-10');
$str = datetime('Y-m-d');
$str = datetime('Y-m-d', time());
~~~~~

@param string $format Optional date format

@param string|int $value Optional date to format

@return WireDateTime|string|int
