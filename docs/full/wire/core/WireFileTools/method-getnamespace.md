# WireFileTools::getNamespace()

Source: `wire/core/WireFileTools.php`

Get the namespace used in the given .php or .module file


@param string $file File name or file data (if file data, specify true for 2nd argument)

@param bool $fileIsContents Specify true if the given $file is actually the contents of the file, rather than file name.

@return string Actual found namespace or "\" (root namespace) if none found
