# $modulesLoader->preloadModules($path)

Source: `wire/core/ModulesLoader.php`

Include site preload modules

Preload modules load before all other modules, including core modules. In order
for a module to be a preload module, it must meet the following conditions:

- Module info `autoload` value is integer of 10000 or greater, i.e. `[ 'autoload' => 10000 ]`
- Module info `singular` value must be non-empty, i.e. `[ 'singular' => true ]`
- Module file is located in: /site/modules/ModuleName/ModuleName.module.php
- Module cannot load any other modules at least until ready() method called.
- Module cannot have any `requires` dependencies to any other modules.

Please note the above is specifically stating that the module must be in its
own “site/ModuleName/” directory and have the “.module.php” extension. Using
just the “.module” extension is not supported for preload modules.

## Usage

~~~~~
// basic usage
$result = $modulesLoader->preloadModules($path);
~~~~~

## Arguments

- `$path` `string`

## Since

3.0.173
