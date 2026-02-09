# ModulesInfo

Source: `wire/core/ModulesInfo.php`

Inherits: `ModulesClass`

## Summary

ProcessWire Modules: Info

Common methods:
- [`moduleInfoCacheEmpty()`](method-moduleinfocacheempty.md)
- [`moduleInfoCacheHas()`](method-moduleinfocachehas.md)
- [`moduleInfoCache()`](method-moduleinfocache.md)
- [`moduleInfoCacheVerbose()`](method-moduleinfocacheverbose.md)
- [`getModuleInfoExternal()`](method-getmoduleinfoexternal.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`moduleInfoCacheEmpty(): bool`](method-moduleinfocacheempty.md) Is the module info cache empty?
- [`moduleInfoCacheHas(int $moduleID): bool`](method-moduleinfocachehas.md) Does the module info cache have an entry for given module ID?
- [`getModuleInfoExternal(string $moduleName): array`](method-getmoduleinfoexternal.md) Retrieve module info from ModuleName.info.json or ModuleName.info.php
- [`getModuleInfoInternal(Module|string $module, string $namespace = ''): array`](method-getmoduleinfointernal.md) Retrieve module info from internal getModuleInfo function in the class
- [`getModuleInfoSystem(string $moduleName, array $options = array()): array`](method-getmoduleinfosystem.md) Retrieve module info for system properties: PHP or ProcessWire
- [`getModuleInfo(string|Module|int $class, array $options = array()): array`](method-getmoduleinfo.md) Returns an associative array of information for a Module
- [`getModuleInfoAll(array $options = array()): array`](method-getmoduleinfoall.md) Get info arrays for all modules indexed by module name
- [`getModuleInfoVerbose(string|Module|int $class, array $options = array()): array`](method-getmoduleinfoverbose.md) Returns a verbose array of information for a Module
- [`getModuleInfoProperty(Module|string $class, string $property, array $options = array()): mixed|null`](method-getmoduleinfoproperty.md) Get just a single property of module info
- [`extractModuleOperatorVersion(string $require): array`](method-extractmoduleoperatorversion.md) Return array of (`$module`, `$operator`, `$requiredVersion`)
- [`saveModuleInfoCache()`](method-savemoduleinfocache.md) Save the module information cache
- [`clearModuleInfoCache(bool|null $showMessages = false)`](method-clearmoduleinfocache.md) Clear the module information cache
- [`updateModuleVersionsCache()`](method-updatemoduleversionscache.md) Update the cache of queued module version changes
- [`checkModuleVersion(Module $module)`](method-checkmoduleversion.md) Check the module version to make sure it is consistent with our moduleInfo
- [`modulesLastVersions(int|null $id = null): string|null|array`](method-moduleslastversions.md)
- [`moduleVersionChanged(Module $module, int|string $fromVersion, int|string $toVersion)`](method-moduleversionchanged.md) Module version changed
- [`getNamespaces(): array`](method-getnamespaces.md) Get an array of all unique, non-default, non-root module namespaces mapped to directory names

## Constants
- [`moduleInfoCacheName = 'Modules.info'`](const-moduleinfocachename.md)
- [`moduleInfoCacheVerboseName = 'ModulesVerbose.info'`](const-moduleinfocacheverbosename.md)
- [`moduleInfoCacheUninstalledName = 'ModulesUninstalled.info'`](const-moduleinfocacheuninstalledname.md)
- [`moduleLastVersionsCacheName = 'ModulesVersions.info'`](const-modulelastversionscachename.md)
- [`defaultNamespace = "\\ProcessWire\\"`](const-defaultnamespace.md)
