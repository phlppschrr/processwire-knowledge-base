# $tfa->uninstall()

Source: `wire/core/Tfa.php`

Uninstall

Please note: Tfa modules with their own uninstall method must also call parent::___uninstall()

## Usage

~~~~~
// basic usage
$result = $tfa->uninstall();
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$tfa->uninstall()`
