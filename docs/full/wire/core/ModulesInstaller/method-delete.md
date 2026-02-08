# $modulesInstaller->delete($class): bool

Source: `wire/core/ModulesInstaller.php`

Delete the given module, physically removing its files

## Arguments

- `$class` `string` Module name (class name)

## Return value

bool

## Throws

- WireException If module can't be deleted, exception will be thrown containing reason.
