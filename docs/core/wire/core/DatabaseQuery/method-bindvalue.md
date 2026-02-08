# $databaseQuery->bindValue($key, $value, $type = null): $this

Source: `wire/core/DatabaseQuery.php`

Bind a parameter value

## Usage

~~~~~
// basic usage
$result = $databaseQuery->bindValue($key, $value);

// usage with all arguments
$result = $databaseQuery->bindValue($key, $value, $type = null);
~~~~~

## Arguments

- `$key` `string` Parameter name
- `$value` `mixed` Parameter value
- null|int|string Optionally specify value type: string, int, bool, null or PDO::PARAM_* constant.

## Return value

- `$this`
