# $modules->getModuleEditUrl($className, $collapseInfo = true): string

Source: `wire/core/Modules.php`

Return the URL where the module can be edited, configured or uninstalled

If module is not installed, it returns URL to install the module.

## Usage

~~~~~
// basic usage
$string = $modules->getModuleEditUrl($className);

// usage with all arguments
$string = $modules->getModuleEditUrl($className, $collapseInfo = true);
~~~~~

## Arguments

- `$className` `string|Module`
- `$collapseInfo` (optional) `bool`

## Return value

- `string`
