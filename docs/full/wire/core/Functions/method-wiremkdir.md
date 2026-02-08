# Functions::wireMkdir()

Source: `wire/core/Functions.php`

Create a directory (optionally recursively) that is writable to ProcessWire and uses the $config chmod settings

This is procedural version of the `$files->mkdir()` method.


@param string $path

@param bool $recursive If set to true, all directories will be created as needed to reach the end.

@param string $chmod Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755"
	If omitted, then ProcessWire’s $config->chmodDir setting is used instead.

@return bool

@see WireFileTools::mkdir()
