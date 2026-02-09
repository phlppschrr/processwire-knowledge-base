# $modules->saveConfig($class, $data, $value = null): bool

Source: `wire/core/Modules.php`

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.


3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

## Example

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

## Usage

~~~~~
// basic usage
$bool = $modules->saveConfig($class, $data);

// usage with all arguments
$bool = $modules->saveConfig($class, $data, $value = null);
~~~~~

## Arguments

- `$class` `string|Module` Module or module name
- `$data` `array|string` Associative array of configuration data, or name of property you want to save.
- `$value` (optional) `mixed|null` If you specified a property in previous arg, the value for the property.

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `saveConfig`
- Implementation: `___saveConfig`
- Hook with: `Modules::saveConfig`

### Hooking Before

~~~~~
$this->addHookBefore('Modules::saveConfig', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);
  $data = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $class);
  $event->arguments(1, $data);
  $event->arguments(2, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Modules::saveConfig', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);
  $data = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`

## See Also

- [Modules::getConfig()](method-getconfig.md)

## Since

3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
