# $modulesInstaller->install($class, $options = array()): null|Module

Source: `wire/core/ModulesInstaller.php`

Install the given module name

## Arguments

- string $class Module name (class name)
- array|bool $options Optional associative array that can contain any of the following: - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true) - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true) - `force` (boolean): Force installation, even if dependencies can't be met.

## Return value

null|Module Returns null if unable to install, or ready-to-use Module object if successfully installed.

## Throws

- WireException
