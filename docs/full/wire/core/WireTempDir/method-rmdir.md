# $wireTempDir->rmdir($dir, $recursive = false): bool

Source: `wire/core/WireTempDir.php`

Remove a temporary directory

## Usage

~~~~~
// basic usage
$bool = $wireTempDir->rmdir($dir);

// usage with all arguments
$bool = $wireTempDir->rmdir($dir, $recursive = false);
~~~~~

## Arguments

- `$dir` `string`
- `$recursive` (optional) `bool`

## Return value

- `bool`
