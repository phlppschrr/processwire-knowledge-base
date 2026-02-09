# ModulesLoader

Source: `wire/core/ModulesLoader.php`

Inherits: `ModulesClass`

ProcessWire Modules: Loader

Methods:
- [`initModule(Module $module, array $options = array()): bool`](method-initmodule.md) Initialize a single module
- [`readyModule(Module $module): bool`](method-readymodule.md) Call ready for a single module
- [`triggerConditionalAutoload(): array`](method-triggerconditionalautoload.md) Init conditional autoload modules, if conditions allow
- [`loadModulesTable()`](method-loadmodulestable.md) Retrieve the installed module info as stored in the database
- [`loadPath(string $path)`](method-loadpath.md) Given a disk path to the modules, determine all installed modules and keep track of all uninstalled (installable) modules.
- [`loadModule(string $basepath, string $pathname, array &$requires, array &$installed): string`](method-loadmodule.md) Load a module into memory (companion to load bootstrap method)
- [`preloadModules(string $path)`](method-preloadmodules.md) Include site preload modules
- [`loaded()`](method-loaded.md) Called by Modules class when init has finished
- [`getAutoloadOrders(): array`](method-getautoloadorders.md) Get the autoload orders
