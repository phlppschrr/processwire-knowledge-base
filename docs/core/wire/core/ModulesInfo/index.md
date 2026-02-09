# ModulesInfo

Source: `wire/core/ModulesInfo.php`

Inherits: `ModulesClass`


Groups:
Group: [other](group-other.md)

ProcessWire Modules: Info

Methods:
- [`moduleInfoCacheEmpty(): bool`](method-moduleinfocacheempty.md)
- [`moduleInfoCacheHas(int $moduleID): bool`](method-moduleinfocachehas.md)
- [`getModuleInfoExternal(string $moduleName): array`](method-getmoduleinfoexternal.md)
- [`getModuleInfoInternal(Module|string $module, string $namespace = ''): array`](method-getmoduleinfointernal.md)
- [`getModuleInfoSystem(string $moduleName, array $options = array()): array`](method-getmoduleinfosystem.md)
- [`getModuleInfo(string|Module|int $class, array $options = array()): array`](method-getmoduleinfo.md)
- [`getModuleInfoAll(array $options = array()): array`](method-getmoduleinfoall.md)
- [`getModuleInfoVerbose(string|Module|int $class, array $options = array()): array`](method-getmoduleinfoverbose.md)
- [`getModuleInfoProperty(Module|string $class, string $property, array $options = array()): mixed|null`](method-getmoduleinfoproperty.md)
- [`extractModuleOperatorVersion(string $require): array`](method-extractmoduleoperatorversion.md)
- [`saveModuleInfoCache()`](method-savemoduleinfocache.md)
- [`clearModuleInfoCache(bool|null $showMessages = false)`](method-clearmoduleinfocache.md)
- [`updateModuleVersionsCache()`](method-updatemoduleversionscache.md)
- [`checkModuleVersion(Module $module)`](method-checkmoduleversion.md)
- [`modulesLastVersions(int|null $id = null): string|null|array`](method-moduleslastversions.md)
- [`moduleVersionChanged(Module $module, int|string $fromVersion, int|string $toVersion)`](method-moduleversionchanged.md)
- [`getNamespaces(): array`](method-getnamespaces.md)

Constants:
- [`moduleInfoCacheName`](const-moduleinfocachename.md)
- [`moduleInfoCacheVerboseName`](const-moduleinfocacheverbosename.md)
- [`moduleInfoCacheUninstalledName`](const-moduleinfocacheuninstalledname.md)
- [`moduleLastVersionsCacheName`](const-modulelastversionscachename.md)
- [`defaultNamespace`](const-defaultnamespace.md)
