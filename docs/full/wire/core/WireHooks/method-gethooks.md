# WireHooks::getHooks()

Source: `wire/core/WireHooks.php`

Return all hooks associated with $object or method (if specified)

@param Wire $object

@param string $method Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.

@param int $getHooks Get hooks of type, specify one of the following constants:
	- WireHooks::getHooksAll returns all hooks [0] (default)
	- WireHooks::getHooksLocal returns local hooks [1] only
	- WireHooks::getHooksStatic returns static hooks [2] only

@return array
