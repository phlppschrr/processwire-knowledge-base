# ModulesFiles

Source: `wire/core/ModulesFiles.php`

Inherits: `ModulesClass`

ProcessWire Modules: Files

Methods:
- [`moduleFileExt(string $class, int $setValue = null): int`](method-modulefileext.md) Get or set module file extension type (1 or 2)
- [`findModuleFiles(string $path, bool $readCache = false, int $level = 0): array`](method-findmodulefiles.md) Find new module files in the given $path
- [`getModuleFile(string|Module $class, array|bool $options = array()): bool|string`](method-getmodulefile.md) Get the path + filename (or optionally URL) for module
- [`includeModuleFile(string $file, string $moduleName): bool`](method-includemodulefile.md) Include the given filename
- [`compile(Module|string $moduleName, string $file = '', string|null $namespace = null): string|bool`](method-compile.md) Compile and return the given file for module, if allowed to do so
- [`getModuleLanguageFiles(Module|string $module): array`](method-getmodulelanguagefiles.md) Get module language translation files
- [`setConfigPaths(string $moduleName, string $path)`](method-setconfigpaths.md) Setup entries in config->urls and config->paths for the given module
