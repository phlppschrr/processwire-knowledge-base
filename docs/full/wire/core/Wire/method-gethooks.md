# $wire->getHooks($method = '', $type = 0): array

Source: `wire/core/Wire.php`

Return all hooks associated with this class instance or method (if specified)

## Usage

~~~~~
// basic usage
$array = $wire->getHooks();

// usage with all arguments
$array = $wire->getHooks($method = '', $type = 0);
~~~~~

## Arguments

- `$method` (optional) `string` Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.
- `$type` (optional) `int` Type of hooks to return, specify one of the following constants (from the WireHooks class): - `WireHooks::getHooksAll` returns all hooks (default). - `WireHooks::getHooksLocal` returns local hooks only. - `WireHooks::getHooksStatic` returns static hooks only.

## Return value

- `array`
