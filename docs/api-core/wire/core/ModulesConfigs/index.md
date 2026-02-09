# ModulesConfigs

Source: `wire/core/ModulesConfigs.php`

Inherits: `ModulesClass`

## Summary

ProcessWire Modules: Configs

Common methods:
- [`configData()`](method-configdata.md)
- [`getModuleEditUrl()`](method-getmoduleediturl.md)
- [`getConfig()`](method-getconfig.md)
- [`isConfigurable()`](method-isconfigurable.md)
- [`isConfigable()`](method-isconfigable.md)

## Methods
- [`getModuleEditUrl(string|Module $className, bool $collapseInfo = true): string`](method-getmoduleediturl.md) Return the URL where the module can be edited, configured or uninstalled
- [`getConfig(string|Module $class, string $property = ''): array|string|int|float`](method-getconfig.md) Given a module name, return an associative array of configuration data for it
- [`isConfigurable(Module|string $class, bool $useCache = true): bool|string|int`](method-isconfigurable.md) Is the given module interactively configurable?
- [`isConfigable(string|Module $class, bool $useCache = true): bool|int|string`](method-isconfigable.md) Indicates whether module accepts config settings, whether interactively or API only
- [`setModuleConfigData(Module $module, array|null $data = null, array|null $extraData = null): bool`](method-setmoduleconfigdata.md) Populate configuration data to a ConfigurableModule
- [`saveConfig(string|Module $class, array|string $data, mixed|null $value = null): bool`](method-saveconfig.md) Save provided configuration data for the given module
