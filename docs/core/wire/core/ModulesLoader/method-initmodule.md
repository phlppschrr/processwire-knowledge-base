# $modulesLoader->initModule(Module $module, array $options = array()): bool

Source: `wire/core/ModulesLoader.php`

Initialize a single module

## Arguments

- Module $module
- array $options - `clearSettings` (bool): When true, module settings will be cleared when appropriate to save space. (default=true) - `configOnly` (bool): When true, module init() method NOT called, but config data still set (default=false) 3.0.169+ - `configData` (array): Extra config data merge with module’s config data (default=[]) 3.0.169+ - `throw` (bool): When true, exceptions will be allowed to pass through. (default=false)

## Return value

bool True on success, false on fail

## Throws

- \Exception Only if the `throw` option is true.
