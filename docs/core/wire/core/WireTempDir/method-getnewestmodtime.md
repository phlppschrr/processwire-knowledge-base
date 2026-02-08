# $wireTempDir->getNewestModTime($path, $maxDepth = 5): int

Source: `wire/core/WireTempDir.php`

Get the newest modification time of a file in $path, recursively

## Usage

~~~~~
// basic usage
$int = $wireTempDir->getNewestModTime($path);

// usage with all arguments
$int = $wireTempDir->getNewestModTime($path, $maxDepth = 5);
~~~~~

## Arguments

- `$path` `string` Path to start from
- `$maxDepth` (optional) `int`

## Return value

- `int`
