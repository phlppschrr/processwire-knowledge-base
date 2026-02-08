# $process->upgrade($fromVersion, $toVersion)

Source: `wire/core/Process.php`

Called when module version changes

See the `Module` interface and the `upgrade` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->upgrade($fromVersion, $toVersion);
~~~~~

## Hookable

- Hookable method name: `upgrade`
- Implementation: `___upgrade`
- Hook with: `$process->upgrade()`

## Arguments

- `$fromVersion` `int|string` Previous version
- `$toVersion` `int|string` New version

## Exceptions

- `WireException` if upgrade fails
