# ModulesLoader

Source: `wire/core/ModulesLoader.php`

ProcessWire Modules: Loader

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## initModule()

Initialize a single module

@param Module $module

@param array $options
 - `clearSettings` (bool): When true, module settings will be cleared when appropriate to save space. (default=true)
 - `configOnly` (bool): When true, module init() method NOT called, but config data still set (default=false) 3.0.169+
 - `configData` (array): Extra config data merge with module’s config data (default=[]) 3.0.169+
 - `throw` (bool): When true, exceptions will be allowed to pass through. (default=false)

@return bool True on success, false on fail

@throws \Exception Only if the `throw` option is true.

## readyModule()

Call ready for a single module

@param Module $module

@return bool

## triggerConditionalAutoload()

Init conditional autoload modules, if conditions allow

@return array of skipped module names

## loadModulesTable()

Retrieve the installed module info as stored in the database

## loadPath()

Given a disk path to the modules, determine all installed modules and keep track of all uninstalled (installable) modules.

@param string $path

## loadModule()

Load a module into memory (companion to load bootstrap method)

@param string $basepath Base path of modules being processed (path provided to the load method)

@param string $pathname

@param array $requires This method will populate this array with required dependencies (class names) if present.

@param array $installed Array of installed modules info, indexed by module class name

@return string Returns module name (classname)

## preloadModules()

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

@param string $path

@since 3.0.173

## loaded()

Called by Modules class when init has finished

## getAutoloadOrders()

Get the autoload orders

@return array Array of [ moduleName (string => order (int) ]
