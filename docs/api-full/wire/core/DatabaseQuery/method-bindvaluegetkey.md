# $databaseQuery->bindValueGetKey($value, $type = null): string

Source: `wire/core/DatabaseQuery.php`

Bind value and get unique key that refers to it in one step

## Usage

~~~~~
// basic usage
$string = $databaseQuery->bindValueGetKey($value);

// usage with all arguments
$string = $databaseQuery->bindValueGetKey($value, $type = null);
~~~~~

## Arguments

- `$value` `string|int|float`
- `$type` (optional) `null|int|string`

## Return value

- `string`

## Since

3.0.157
