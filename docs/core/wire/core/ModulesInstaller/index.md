# ModulesInstaller

Source: `wire/core/ModulesInstaller.php`

Inherits: `ModulesClass`

ProcessWire Modules: Installer

Methods:
- [`install(string $class, array|bool $options = array()): null|Module`](method-install.md) Install the given module name
- [`delete(string $class): bool`](method-delete.md) Delete the given module, physically removing its files
- [`uninstall(string $class): bool`](method-uninstall.md) Uninstall the given module name
- [`getModuleInstallUrl(string $className): string`](method-getmoduleinstallurl.md) Get URL where an administrator can install given module name
