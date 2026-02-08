# $process->___upgrade($fromVersion, $toVersion)

Source: `wire/core/Process.php`

Called when module version changes

See the `Module` interface and the `upgrade` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->___upgrade($fromVersion, $toVersion);
~~~~~

## Arguments

- `$fromVersion` `int|string` Previous version
- `$toVersion` `int|string` New version

## Exceptions

- `WireException` if upgrade fails
