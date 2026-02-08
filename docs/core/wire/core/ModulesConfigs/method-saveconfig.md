# $modulesConfigs->saveConfig($class, $data, $value = null): bool

Source: `wire/core/ModulesConfigs.php`

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);
~~~~~~

3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

## Arguments

- string|Module $class Module or module name
- array|string $data Associative array of configuration data, or name of property you want to save.
- mixed|null $value If you specified a property in previous arg, the value for the property.

## Return value

bool True on success, false on failure

## Throws

- WireException

## See also

- [Modules::getConfig()](../Modules/method-getconfig.md)

## Meta

- @since 3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
