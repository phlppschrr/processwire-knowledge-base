# $functions->wireClassImplements($className, $autoload = true): array

Source: `wire/core/Functions.php`

Get an array of all the interfaces that the given class implements

- ProcessWire namespace aware version of PHP’s class_implements() function.
- Return value has array keys as class name with namespace and array values as class name without namespace.

## Usage

~~~~~
// basic usage
$array = $functions->wireClassImplements($className);

// usage with all arguments
$array = $functions->wireClassImplements($className, $autoload = true);
~~~~~

## Arguments

- `$className` `string|object`
- `$autoload` (optional) `bool`

## Return value

- `array`
