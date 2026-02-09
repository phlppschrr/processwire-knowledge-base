# $wireDatabasePDO->getTime($getTimestamp = false): string|int

Source: `wire/core/WireDatabasePDO.php`

Get current date/time ISO-8601 string or UNIX timestamp according to database

## Usage

~~~~~
// basic usage
$string = $wireDatabasePDO->getTime();

// usage with all arguments
$string = $wireDatabasePDO->getTime($getTimestamp = false);
~~~~~

## Arguments

- `$getTimestamp` (optional) `bool` Get unix timestamp rather than ISO-8601 string? (default=false)

## Return value

- `string|int`

## Since

3.0.183
