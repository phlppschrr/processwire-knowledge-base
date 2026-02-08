# $process->___upgrade($fromVersion, $toVersion)

Source: `wire/core/Process.php`

Called when module version changes

See the `Module` interface and the `upgrade` method there for more details.

## Arguments

- int|string $fromVersion Previous version
- int|string $toVersion New version

## Throws

- WireException if upgrade fails
