# $process->uninstallPage(): int

Source: `wire/core/Process.php`

Uninstall (trash) dedicated pages for this Process module

If there is more than one page using this Process, it will trash them all.

To be called by the Process module's ___uninstall() method.

## Usage

~~~~~
// basic usage
$int = $process->uninstallPage();
~~~~~

## Hookable

- Hookable method name: `uninstallPage`
- Implementation: `___uninstallPage`
- Hook with: `$process->uninstallPage()`

## Return value

- `int` Number of pages trashed
