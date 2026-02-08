# Modules::findByInfo()

Source: `wire/core/Modules.php`

Find modules by matching a property or properties in their module info

@param string|array $selector Specify one of the following:
 - Selector string to match module info.
 - Array of [ 'property' => 'value' ] to match in module info (this is not a selector array).
 - Name of property that will match module if not empty in module info.

@param bool|int $load Specify one of the following:
 - Boolean true to return array of instantiated modules.
 - Boolean false to return array of module names (default).
 - Integer 1 to return array of module info for each matching module.
 - Integer 2 to return array of verbose module info for each matching module.

@return array Array of modules, module names or module info arrays, indexed by module name.
