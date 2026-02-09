# $functions->wireRmdir($path, $recursive = false): bool

Source: `wire/core/Functions.php`

Remove a directory (optionally recursively)

This is procedural version of the `$files->rmdir()` method. See that method for more options.

## Usage

~~~~~
// basic usage
$bool = $functions->wireRmdir($path);

// usage with all arguments
$bool = $functions->wireRmdir($path, $recursive = false);
~~~~~

## Arguments

- `$path` `string`
- `$recursive` (optional) `bool` If set to true, all files and directories in $path will be recursively removed as well.

## Return value

- `bool`

## See Also

- [WireFileTools::rmdir()](../WireFileTools/method-rmdir.md)
