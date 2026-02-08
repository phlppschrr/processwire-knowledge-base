# Modules::___saveConfig()

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

@param string|Module $class Module or module name

@param array|string $data Associative array of configuration data, or name of property you want to save.

@param mixed|null $value If you specified a property in previous arg, the value for the property.

@return bool True on success, false on failure

@throws WireException

@see Modules::getConfig()

@since 3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
