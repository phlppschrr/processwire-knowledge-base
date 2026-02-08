# $wireLog->prune($name, $days): int

Source: `wire/core/WireLog.php`

Prune log file to contain only entries from last [n] days

## Arguments

- string $name Name of log file, excluding path and extension.
- int $days Number of days

## Return value

int Number of items in newly pruned log file or boolean false on failure

## Throws

- WireException
