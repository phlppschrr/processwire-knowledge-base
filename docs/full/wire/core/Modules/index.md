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
- [`__construct(string $path)`](method-__construct.md)
- [`isValidItem($item)`](method-isvaliditem.md)
- [`get($key)`](method-get.md)
- [`get(string|int $key): Module|_Module|null`](method-get.md)
- [`getModule(string|int $key, array $options = array()): Module|_Module|null|string`](method-getmodule.md)
- [`findByPrefix($prefix, $load = false)`](method-findbyprefix.md)
- [`findByPrefix(string $prefix, bool|int $load = false): array`](method-findbyprefix.md)
- [`findByInfo(string|array $selector, bool|int $load = false): array`](method-findbyinfo.md)
- [`getInstallable()`](method-getinstallable.md)
- [`isInstalled(string $class): bool`](method-isinstalled.md)
- [`install(string $class, array|bool $options = array()): null|Module`](method-___install.md) (hookable)
- [`delete(string $class): bool`](method-___delete.md) (hookable)
- [`uninstall(string $class): bool`](method-___uninstall.md) (hookable)
- [`getFlags($class)`](method-getflags.md)
- [`moduleInfoCache($moduleID = null, $property = '', $verbose = false)`](method-moduleinfocache.md)
- [`getModuleID(string|int|Module $class): int`](method-getmoduleid.md)
- [`getModuleInfo(string|Module|int $class, array $options = array()): array`](method-getmoduleinfo.md)
- [`getModuleInfoVerbose(string|Module|int $class, array $options = array()): array`](method-getmoduleinfoverbose.md)
- [`getModuleInfoProperty(Module|string $class, string $property, array $options = array()): mixed|null`](method-getmoduleinfoproperty.md)
- [`getConfig($class, $property = '')`](method-getconfig.md)
- [`getConfig(string|Module $class, string $property = ''): array|string|int|float`](method-getconfig.md)
- [`saveConfig(string|Module $class, array|string $data, mixed|null $value = null): bool`](method-___saveconfig.md) (hookable)
- [`isConfigurable(Module|string $class, bool $useCache = true): bool|string|int`](method-isconfigurable.md)
- [`getModuleEditUrl(string|Module $className, bool $collapseInfo = true): string`](method-getmoduleediturl.md)
- [`getModuleInstallUrl(string $className): string`](method-getmoduleinstallurl.md)
- [`isSingular($module)`](method-issingular.md)
- [`refresh(bool $showMessages = false)`](method-___refresh.md) (hookable)
- [`getRequiredBy($class, $uninstalled = false, $installs = false)`](method-getrequiredby.md)
- [`setSubstitute($moduleName, $substituteName = null)`](method-setsubstitute.md)
- [`getModuleFile($class, $options = array())`](method-getmodulefile.md)
- [`getModuleFile(string|Module $class, array|bool $options = array()): bool|string`](method-getmodulefile.md)
- [`getModuleLanguageFiles(Module|string $module): array`](method-getmodulelanguagefiles.md)
- [`__invoke($key)`](method-__invoke.md)
- [`__invoke(string $key): Module|null`](method-__invoke.md)
- [`memcache($name, $setValue = null)`](method-memcache.md)
- [`memcache(string $name, mixed $setValue = null): bool|array|mixed|null`](method-memcache.md)
- [`__get(string $name): mixed`](method-__get.md)

Constants:
- [`flagsSingular`](const-flagssingular.md)
- [`flagsAutoload`](const-flagsautoload.md)
- [`flagsDuplicate`](const-flagsduplicate.md)
- [`flagsConditional`](const-flagsconditional.md)
- [`flagsDisabled`](const-flagsdisabled.md)
- [`flagsNoUserConfig`](const-flagsnouserconfig.md)
- [`flagsNoFile`](const-flagsnofile.md)
- [`flagsSystemCache`](const-flagssystemcache.md)
