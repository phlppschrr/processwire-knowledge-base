# ModulesLoader

Source: `wire/core/ModulesLoader.php`

Inherits: `ModulesClass`

ProcessWire Modules: Loader

Methods:
- [`initModule(Module $module, array $options = array()): bool`](method-initmodule.md)
- [`readyModule(Module $module): bool`](method-readymodule.md)
- [`triggerConditionalAutoload(): array`](method-triggerconditionalautoload.md)
- [`loadModulesTable()`](method-loadmodulestable.md)
- [`loadPath(string $path)`](method-loadpath.md)
- [`loadModule(string $basepath, string $pathname, array &$requires, array &$installed): string`](method-loadmodule.md)
- [`preloadModules(string $path)`](method-preloadmodules.md)
- [`loaded()`](method-loaded.md)
- [`getAutoloadOrders(): array`](method-getautoloadorders.md)
