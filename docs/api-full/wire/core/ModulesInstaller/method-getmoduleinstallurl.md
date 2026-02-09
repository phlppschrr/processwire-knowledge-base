# $modulesInstaller->getModuleInstallUrl($className): string

Source: `wire/core/ModulesInstaller.php`

Get URL where an administrator can install given module name

If module is already installed, it returns the URL to edit the module.

## Usage

~~~~~
// basic usage
$string = $modulesInstaller->getModuleInstallUrl($className);
~~~~~

## Arguments

- `$className` `string`

## Return value

- `string`
