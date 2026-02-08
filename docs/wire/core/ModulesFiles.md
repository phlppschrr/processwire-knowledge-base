# ModulesFiles

Source: `wire/core/ModulesFiles.php`

ProcessWire Modules: Files

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## moduleFileExt()

Get or set module file extension type (1 or 2)

@param string $class Module class name

@param int $setValue 1 for '.module' or 2 for '.module.php', or omit to get current value

@return int

## findModuleFiles()

Find new module files in the given $path

If $readCache is true, this will perform the find from the cache

@param string $path Path to the modules

@param bool $readCache Optional. If set to true, then this method will attempt to read modules from the cache.

@param int $level For internal recursive use.

@return array Array of module files

## getModuleFile()

Get the path + filename (or optionally URL) for module

@param string|Module $class Module class name or object instance

@param array|bool $options Options to modify default behavior:
	- `getURL` (bool): Specify true if you want to get the URL rather than file path (default=false).
	- `fast` (bool): Specify true to omit file_exists() checks (default=false).
 - `guess` (bool): Manufacture/guess a module location if one cannot be found (default=false) 3.0.170+
	- Note: If you specify a boolean for the $options argument, it is assumed to be the $getURL property.

@return bool|string Returns string of module file, or false on failure.

## includeModuleFile()

Include the given filename

@param string $file

@param string $moduleName

@return bool

## compile()

Compile and return the given file for module, if allowed to do so

@param Module|string $moduleName

@param string $file Optionally specify the module filename as an optimization

@param string|null $namespace Optionally specify namespace as an optimization

@return string|bool

## getModuleLanguageFiles()

Get module language translation files

@param Module|string $module

@return array Array of translation files including full path, indexed by basename without extension

@since 3.0.181

## setConfigPaths()

Setup entries in config->urls and config->paths for the given module

@param string $moduleName

@param string $path
