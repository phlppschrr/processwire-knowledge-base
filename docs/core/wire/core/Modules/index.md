# Modules

Source: `wire/core/Modules.php`

Inherits: `WireArray`


Groups:
Group: [other](group-other.md)

ProcessWire Modules

Loads and manages all runtime modules for ProcessWire


Loads and manages all modules in ProcessWire.
The `$modules` API variable is most commonly used for getting individual modules to use their API.
~~~~~
// Getting a module by name
$m = $modules->get('MarkupPagerNav');

// Getting a module by name (alternate)
$m = $modules->MarkupPagerNav;
~~~~~


Note that when iterating, find(), or calling any other method that returns module(s), excepting get(), a ModulePlaceholder may be
returned rather than a real Module. ModulePlaceholders are used in instances when the module may or may not be needed at runtime
in order to save resources. As a result, anything iterating through these Modules should check to make sure it's not a ModulePlaceholder
before using it. If it's a ModulePlaceholder, then the real Module can be instantiated/retrieved by $modules->get($className).

Methods:
- [`__construct(string $path)`](method-__construct.md) Construct the Modules
- [`get(string|int $key): Module|_Module|null`](method-get.md) Get the requested Module
- [`getModule(string|int $key, array $options = array()): Module|_Module|null|string`](method-getmodule.md) Get the requested Module (with options)
- [`findByPrefix(string $prefix, bool|int $load = false): array`](method-findbyprefix.md) Find modules matching the given prefix (i.e. “Inputfield”)
- [`findByInfo(string|array $selector, bool|int $load = false): array`](method-findbyinfo.md) Find modules by matching a property or properties in their module info
- [`isInstalled(string $class): bool`](method-isinstalled.md) Is the given module name installed?
- [`install(string $class, array|bool $options = array()): null|Module`](method-___install.md) (hookable) Install the given module name
- [`delete(string $class): bool`](method-___delete.md) (hookable) Delete the given module, physically removing its files
- [`uninstall(string $class): bool`](method-___uninstall.md) (hookable) Uninstall the given module name
- [`getModuleID(string|int|Module $class): int`](method-getmoduleid.md) Returns the database ID of a given module class, or 0 if not found
- [`getModuleInfo(string|Module|int $class, array $options = array()): array`](method-getmoduleinfo.md) Returns an associative array of information for a Module
- [`getModuleInfoVerbose(string|Module|int $class, array $options = array()): array`](method-getmoduleinfoverbose.md) Returns a verbose array of information for a Module
- [`getModuleInfoProperty(Module|string $class, string $property, array $options = array()): mixed|null`](method-getmoduleinfoproperty.md) Get just a single property of module info
- [`getConfig(string|Module $class, string $property = ''): array|string|int|float`](method-getconfig.md) Given a module name, return an associative array of configuration data for it
- [`saveConfig(string|Module $class, array|string $data, mixed|null $value = null): bool`](method-___saveconfig.md) (hookable) Save provided configuration data for the given module
- [`isConfigurable(Module|string $class, bool $useCache = true): bool|string|int`](method-isconfigurable.md) Is the given module interactively configurable?
- [`getModuleEditUrl(string|Module $className, bool $collapseInfo = true): string`](method-getmoduleediturl.md) Return the URL where the module can be edited, configured or uninstalled
- [`getModuleInstallUrl(string $className): string`](method-getmoduleinstallurl.md) Get URL where an administrator can install given module name
- [`refresh(bool $showMessages = false)`](method-___refresh.md) (hookable) Refresh the modules cache
- [`getModuleFile(string|Module $class, array|bool $options = array()): bool|string`](method-getmodulefile.md) Get the path + filename (or optionally URL) for this module
- [`getModuleLanguageFiles(Module|string $module): array`](method-getmodulelanguagefiles.md) Get module language translation files
- [`__invoke(string $key): Module|null`](method-__invoke.md) Enables use of $modules('ModuleName')
- [`memcache(string $name, mixed $setValue = null): bool|array|mixed|null`](method-memcache.md) Set a runtime memory cache
- [`__get(string $name): mixed`](method-__get.md) Direct read-only properties

Constants:
- [`flagsSingular`](const-flagssingular.md)
- [`flagsAutoload`](const-flagsautoload.md)
- [`flagsDuplicate`](const-flagsduplicate.md)
- [`flagsConditional`](const-flagsconditional.md)
- [`flagsDisabled`](const-flagsdisabled.md)
- [`flagsNoUserConfig`](const-flagsnouserconfig.md)
- [`flagsNoFile`](const-flagsnofile.md)
- [`flagsSystemCache`](const-flagssystemcache.md)
