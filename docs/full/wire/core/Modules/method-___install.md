# $modules->___install($class, $options = array()): null|Module

Source: `wire/core/Modules.php`

Install the given module name

## Usage

~~~~~
// basic usage
$modules->___install($class);

// usage with all arguments
$modules->___install($class, $options = array());
~~~~~

## Arguments

- `$class` `string` Module name (class name)
- `$options` (optional) `array|bool` Optional associative array that can contain any of the following: - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true) - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true) - `force` (boolean): Force installation, even if dependencies can't be met.

## Return value

- `null|Module` Returns null if unable to install, or ready-to-use Module object if successfully installed.

## Exceptions

- `WireException`
