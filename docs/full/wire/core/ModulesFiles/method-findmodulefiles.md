# ModulesFiles::findModuleFiles()

Source: `wire/core/ModulesFiles.php`

Find new module files in the given $path

If $readCache is true, this will perform the find from the cache

@param string $path Path to the modules

@param bool $readCache Optional. If set to true, then this method will attempt to read modules from the cache.

@param int $level For internal recursive use.

@return array Array of module files
