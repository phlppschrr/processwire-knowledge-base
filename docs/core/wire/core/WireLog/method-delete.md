# $wireLog->delete($name): bool

Source: `wire/core/WireLog.php`

Delete a log file

## Usage

~~~~~
// basic usage
$bool = $wireLog->delete($name);
~~~~~

## Arguments

- `$name` `string` Name of log, excluding path and extension.

## Return value

- `bool` True on success, false on failure.
