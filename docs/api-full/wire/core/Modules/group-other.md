# Modules: other

Source: `wire/core/Modules.php`

- [`refresh($showMessages = false): void`](method-___refresh.md) Refresh the cache that stores module files by recreating it
- [`install($class, $options = array()): null|Module`](method-___install.md)
- [`delete($class): bool|int`](method-___delete.md)
- [`uninstall($class): bool`](method-___uninstall.md)
- [`saveConfig($class, $data, $value = null): bool`](method-___saveconfig.md)
- `$installableFiles: array`
- `$coreModulesDir: string`
- `$coreModulesPath: string`
- `$siteModulesPath: string`
- `$moduleIDs: array`
- `$moduleNames: array`
- `$info: ModulesInfo`
- `$loader: ModulesLoader`
- `$flags: ModulesFlags`
- `$files: ModulesFiles`
- `$installer: ModulesInstaller`
- `$configs: ModulesConfigs`
- `$refreshing: bool`
