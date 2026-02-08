# $wireFileTools->getNamespace($file, $fileIsContents = false): string

Source: `wire/core/WireFileTools.php`

Get the namespace used in the given .php or .module file

## Usage

~~~~~
// basic usage
$string = $wireFileTools->getNamespace($file);

// usage with all arguments
$string = $wireFileTools->getNamespace($file, $fileIsContents = false);
~~~~~

## Arguments

- `$file` `string` File name or file data (if file data, specify true for 2nd argument)
- `$fileIsContents` (optional) `bool` Specify true if the given $file is actually the contents of the file, rather than file name.

## Return value

- `string` Actual found namespace or "\" (root namespace) if none found
