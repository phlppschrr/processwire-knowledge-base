# $modulesInstaller->delete($class): bool

Source: `wire/core/ModulesInstaller.php`

Delete the given module, physically removing its files

## Usage

~~~~~
// basic usage
$bool = $modulesInstaller->delete($class);
~~~~~

## Arguments

- `$class` `string` Module name (class name)

## Return value

- `bool`

## Exceptions

- `WireException` If module can't be deleted, exception will be thrown containing reason.
