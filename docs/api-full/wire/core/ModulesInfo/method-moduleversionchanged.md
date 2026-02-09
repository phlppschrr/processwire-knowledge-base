# $modulesInfo->moduleVersionChanged(Module $module, $fromVersion, $toVersion)

Source: `wire/core/ModulesInfo.php`

Module version changed

This calls the module's ___upgrade($fromVersion, $toVersion) method.

## Usage

~~~~~
// basic usage
$result = $modulesInfo->moduleVersionChanged($module, $fromVersion, $toVersion);

// usage with all arguments
$result = $modulesInfo->moduleVersionChanged(Module $module, $fromVersion, $toVersion);
~~~~~

## Arguments

- `$module` `Module|_Module`
- `$fromVersion` `int|string`
- `$toVersion` `int|string`
