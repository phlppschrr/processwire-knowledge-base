# $functions->wireMkdir($path, $recursive = false, $chmod = null): bool

Source: `wire/core/Functions.php`

Create a directory (optionally recursively) that is writable to ProcessWire and uses the $config chmod settings

This is procedural version of the `$files->mkdir()` method.

## Usage

~~~~~
// basic usage
$bool = $functions->wireMkdir($path);

// usage with all arguments
$bool = $functions->wireMkdir($path, $recursive = false, $chmod = null);
~~~~~

## Arguments

- `$path` `string`
- `$recursive` (optional) `bool` If set to true, all directories will be created as needed to reach the end.
- `$chmod` (optional) `string` Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755" If omitted, then ProcessWire’s $config->chmodDir setting is used instead.

## Return value

- `bool`

## See Also

- [WireFileTools::mkdir()](../WireFileTools/method-mkdir.md)
