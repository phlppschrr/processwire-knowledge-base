# $modules->___saveConfig($class, $data, $value = null): bool

Source: `wire/core/Modules.php`

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving all module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);

// Getting a single configuration property
$value = $modules->getConfig('HelloWorld', 'some_property');

// Saving a single configuration property
$modules->saveConfig('HelloWorld', 'some_property', 'New Value');
~~~~~~

3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

## Arguments

- `$class` `string|Module` Module or module name
- `$data` `array|string` Associative array of configuration data, or name of property you want to save.
- `$value` (optional) `mixed|null` If you specified a property in previous arg, the value for the property.

## Return value

bool True on success, false on failure

## Throws

- WireException

## See also

- [Modules::getConfig()](method-getconfig.md)

## Since

3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
