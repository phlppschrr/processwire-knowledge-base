# $wireHooks->getHooks(Wire $object, $method = '', $getHooks = self::getHooksAll): array

Source: `wire/core/WireHooks.php`

Return all hooks associated with $object or method (if specified)

## Arguments

- Wire $object
- string $method Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.
- int $getHooks Get hooks of type, specify one of the following constants: - WireHooks::getHooksAll returns all hooks [0] (default) - WireHooks::getHooksLocal returns local hooks [1] only - WireHooks::getHooksStatic returns static hooks [2] only

## Return value

array
