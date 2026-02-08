# $modulesLoader->loadModule($basepath, $pathname, array &$requires, array &$installed): string

Source: `wire/core/ModulesLoader.php`

Load a module into memory (companion to load bootstrap method)

## Arguments

- `$basepath` `string` Base path of modules being processed (path provided to the load method)
- `$pathname` `string`
- `$requires` `array` This method will populate this array with required dependencies (class names) if present.
- `$installed` `array` Array of installed modules info, indexed by module class name

## Return value

string Returns module name (classname)
