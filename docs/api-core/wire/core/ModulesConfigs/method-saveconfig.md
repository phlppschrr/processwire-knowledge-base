# $modulesConfigs->saveConfig($class, $data, $value = null): bool

Source: `wire/core/ModulesConfigs.php`

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.


3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

## Example

~~~~~~
// Getting, modifying and saving module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);
~~~~~~

## Usage

~~~~~
// basic usage
$bool = $modulesConfigs->saveConfig($class, $data);

// usage with all arguments
$bool = $modulesConfigs->saveConfig($class, $data, $value = null);
~~~~~

## Arguments

- `$class` `string|Module` Module or module name
- `$data` `array|string` Associative array of configuration data, or name of property you want to save.
- `$value` (optional) `mixed|null` If you specified a property in previous arg, the value for the property.

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`

## See Also

- [Modules::getConfig()](../Modules/method-getconfig.md)

## Since

3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
