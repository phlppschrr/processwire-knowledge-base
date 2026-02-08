# $modulesInfo->checkModuleVersion(Module $module)

Source: `wire/core/ModulesInfo.php`

Check the module version to make sure it is consistent with our moduleInfo

When not consistent, this triggers the moduleVersionChanged hook, which in turn
triggers the $module->___upgrade($fromVersion, $toVersion) method.

## Arguments

- Module $module
