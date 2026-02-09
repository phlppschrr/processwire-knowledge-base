# ModulesFlags

Source: `wire/core/ModulesFlags.php`

Inherits: `ModulesClass`

## Summary

ProcessWire Modules: Flags

Common methods:
- [`moduleFlags()`](method-moduleflags.md)
- [`getFlags()`](method-getflags.md)
- [`hasFlag()`](method-hasflag.md)
- [`setFlags()`](method-setflags.md)
- [`setFlag()`](method-setflag.md)

## Methods
- [`moduleFlags(int $moduleID = null, int $setValue = null): array|mixed|null`](method-moduleflags.md) Get or set flags for module by module ID
- [`getFlags(int|string|Module $id): int|false`](method-getflags.md) Get flags for the given module
- [`updateModuleFlags(int $moduleID, array $info)`](method-updatemoduleflags.md) Update module flags if any happen to differ from what's in the given moduleInfo
