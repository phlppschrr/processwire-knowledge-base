# $modules->getModuleInstallUrl($className): string

Source: `wire/core/Modules.php`

Get URL where an administrator can install given module name

If module is already installed, it returns the URL to edit the module.

## Usage

~~~~~
// basic usage
$string = $modules->getModuleInstallUrl($className);
~~~~~

## Arguments

- `$className` `string`

## Return value

- `string`

## Since

3.0.216
