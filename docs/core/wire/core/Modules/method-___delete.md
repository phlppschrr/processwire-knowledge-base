# $modules->___delete($class): bool

Source: `wire/core/Modules.php`

Delete the given module, physically removing its files

## Usage

~~~~~
// basic usage
$bool = $modules->___delete($class);
~~~~~

## Arguments

- `$class` `string` Module name (class name)

## Return value

- `bool`

## Exceptions

- `WireException` If module can't be deleted, exception will be thrown containing reason.
