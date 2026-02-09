# $wireLog->prune($name, $days): int

Source: `wire/core/WireLog.php`

Prune log file to contain only entries from last [n] days

## Usage

~~~~~
// basic usage
$int = $wireLog->prune($name, $days);
~~~~~

## Arguments

- `$name` `string` Name of log file, excluding path and extension.
- `$days` `int` Number of days

## Return value

- `int` Number of items in newly pruned log file or boolean false on failure

## Exceptions

- `WireException`
