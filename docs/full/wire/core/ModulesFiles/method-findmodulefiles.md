# $modulesFiles->findModuleFiles($path, $readCache = false, $level = 0): array

Source: `wire/core/ModulesFiles.php`

Find new module files in the given $path

If $readCache is true, this will perform the find from the cache

## Arguments

- string $path Path to the modules
- bool $readCache Optional. If set to true, then this method will attempt to read modules from the cache.
- int $level For internal recursive use.

## Return value

array Array of module files
