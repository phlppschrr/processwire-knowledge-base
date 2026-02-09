# $functions->wireCopy($src, $dst, $options = array()): bool

Source: `wire/core/Functions.php`

Copy all files recursively from one directory to another

This is procedural version of the `$files->copy()` method.

## Usage

~~~~~
// basic usage
$bool = $functions->wireCopy($src, $dst);

// usage with all arguments
$bool = $functions->wireCopy($src, $dst, $options = array());
~~~~~

## Arguments

- `$src` `string` Path to copy files from
- `$dst` `string` Path to copy files to. Directory is created if it doesn’t already exist.
- bool|array Array of options: - `recursive` (bool): Whether to copy directories within recursively. (default=true) - `allowEmptyDirs` (bool): Copy directories even if they are empty? (default=true) - If a boolean is specified for $options, it is assumed to be the 'recursive' option.

## Return value

- `bool` True on success, false on failure.

## See Also

- [WireFileTools::copy()](../WireFileTools/method-copy.md)
