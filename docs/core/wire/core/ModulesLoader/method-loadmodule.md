# ModulesLoader::loadModule()

Source: `wire/core/ModulesLoader.php`

Load a module into memory (companion to load bootstrap method)

@param string $basepath Base path of modules being processed (path provided to the load method)

@param string $pathname

@param array $requires This method will populate this array with required dependencies (class names) if present.

@param array $installed Array of installed modules info, indexed by module class name

@return string Returns module name (classname)
