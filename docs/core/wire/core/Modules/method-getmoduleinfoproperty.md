# $modules->getModuleInfoProperty($class, $property, array $options = array()): mixed|null

Source: `wire/core/Modules.php`

Get just a single property of module info

## Usage

~~~~~
// basic usage
$result = $modules->getModuleInfoProperty($class, $property);

// usage with all arguments
$result = $modules->getModuleInfoProperty($class, $property, array $options = array());
~~~~~

## Arguments

- `$class` `Module|string` Module instance or module name
- `$property` `string` Name of property to get
- `$options` (optional) `array` Additional options (see getModuleInfo method for options)

## Return value

- `mixed|null` Returns value of property or null if not found

## Since

3.0.107
