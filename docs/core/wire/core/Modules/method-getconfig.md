# $modules->getConfig($class, $property = ''): array|string|int|float

Source: `wire/core/Modules.php`

Given a module name, return an associative array of configuration data for it

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);

// Getting just one property 'apiKey' from module config data


3.0.16 Changed from more verbose name `getModuleConfigData()`, which can still be used.

## Arguments

- string|Module $class
- string $property Optionally just get value for a specific property (omit to get all config)

## Return value

array|string|int|float Module configuration data, returns array unless a specific $property was requested

## See also

- [Modules::saveConfig()](method-___saveconfig.md)

## Meta

- @apiKey = $modules->getConfig('HelloWorld', 'apiKey'); ~~~~~~
- @since 3.0.16 Use method getModuleConfigData() with same arguments for prior versions (can also be used on any version).
