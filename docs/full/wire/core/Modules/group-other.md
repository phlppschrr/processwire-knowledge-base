# Modules: other

Source: `wire/core/Modules.php`

@method void refresh($showMessages = false) Refresh the cache that stores module files by recreating it

@method null|Module install($class, $options = array())

@method bool|int delete($class)

@method bool uninstall($class)

@method bool saveConfig($class, $data, $value = null)

@property-read array $installableFiles

@property-read string $coreModulesDir

@property-read string $coreModulesPath

@property-read string $siteModulesPath

@property-read array $moduleIDs

@property-read array $moduleNames

@property-read ModulesInfo $info

@property-read ModulesLoader $loader

@property-read ModulesFlags $flags

@property-read ModulesFiles $files

@property-read ModulesInstaller $installer

@property-read ModulesConfigs $configs

@property-read bool $refreshing
