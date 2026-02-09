# $wireHooks->getHooks(Wire $object, $method = '', $getHooks = self::getHooksAll): array

Source: `wire/core/WireHooks.php`

Return all hooks associated with $object or method (if specified)

## Usage

~~~~~
// basic usage
$array = $wireHooks->getHooks($object);

// usage with all arguments
$array = $wireHooks->getHooks(Wire $object, $method = '', $getHooks = self::getHooksAll);
~~~~~

## Arguments

- `$object` `Wire`
- `$method` (optional) `string` Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.
- `$getHooks` (optional) `int` Get hooks of type, specify one of the following constants: - WireHooks::getHooksAll returns all hooks [0] (default) - WireHooks::getHooksLocal returns local hooks [1] only - WireHooks::getHooksStatic returns static hooks [2] only

## Return value

- `array`
