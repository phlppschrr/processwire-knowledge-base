# $wireDataDB->save($name, $value, $recursive = false): bool

Source: `wire/core/WireDataDB.php`

Save a value

## Usage

~~~~~
// basic usage
$bool = $wireDataDB->save($name, $value);

// usage with all arguments
$bool = $wireDataDB->save($name, $value, $recursive = false);
~~~~~

## Arguments

- `$name` `string`
- `$value` `mixed`
- `$recursive` (optional) `bool`

## Return value

- `bool`

## Exceptions

- `WireException`
