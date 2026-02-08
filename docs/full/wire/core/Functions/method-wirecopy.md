# Functions::wireCopy()

Source: `wire/core/Functions.php`

Copy all files recursively from one directory to another

This is procedural version of the `$files->copy()` method.


@param string $src Path to copy files from

@param string $dst Path to copy files to. Directory is created if it doesn’t already exist.

@param bool|array Array of options:
	- `recursive` (bool): Whether to copy directories within recursively. (default=true)
	- `allowEmptyDirs` (bool): Copy directories even if they are empty? (default=true)
	- If a boolean is specified for $options, it is assumed to be the 'recursive' option.

@return bool True on success, false on failure.

@see WireFileTools::copy()
