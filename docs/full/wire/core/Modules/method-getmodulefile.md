# Modules::getModuleFile()

Source: `wire/core/Modules.php`

Get the path + filename (or optionally URL) for this module

@param string|Module $class Module class name or object instance

@param array|bool $options Options to modify default behavior:
	- `getURL` (bool): Specify true if you want to get the URL rather than file path (default=false).
	- `fast` (bool): Specify true to omit file_exists() checks (default=false).
 - `guess` (bool): Manufacture/guess a module location if one cannot be found (default=false) 3.0.170+
	- Note: If you specify a boolean for the $options argument, it is assumed to be the $getURL property.

@return bool|string Returns string of module file, or false on failure.
