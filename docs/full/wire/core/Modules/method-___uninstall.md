# $modules->uninstall($class): bool

Source: `wire/core/Modules.php`

Uninstall the given module name

## Usage

~~~~~
// basic usage
$bool = $modules->uninstall($class);
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$modules->uninstall()`

## Arguments

- `$class` `string` Module name (class name)

## Return value

- `bool`

## Exceptions

- `WireException`
