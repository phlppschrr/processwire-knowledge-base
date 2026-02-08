# $process->uninstall()

Source: `wire/core/Process.php`

Uninstall this Process

Note that the Modules class handles removal of any Permissions that the Process may have installed.

See the `Module` interface and the `uninstall` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->uninstall();
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$process->uninstall()`
