# Wire::getHooks()

Source: `wire/core/Wire.php`

Return all hooks associated with this class instance or method (if specified)


@param string $method Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.

@param int $type Type of hooks to return, specify one of the following constants (from the WireHooks class):
	- `WireHooks::getHooksAll` returns all hooks (default).
	- `WireHooks::getHooksLocal` returns local hooks only.
	- `WireHooks::getHooksStatic` returns static hooks only.

@return array
