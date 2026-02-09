# $wireTempDir->classRootPath($createIfNotExists = false, $basePath = ''): string

Source: `wire/core/WireTempDir.php`

Return the class root path for cache files (i.e. /path/to/site/assets/cache/WireTempDir/)

## Usage

~~~~~
// basic usage
$string = $wireTempDir->classRootPath();

// usage with all arguments
$string = $wireTempDir->classRootPath($createIfNotExists = false, $basePath = '');
~~~~~

## Arguments

- `$createIfNotExists` (optional) `bool` Create the directory if it does not exist? (default=false)
- `$basePath` (optional) `string` Path to start from (default=/path/to/site/assets/cache/)

## Return value

- `string`

## Exceptions

- `WireException`

## Since

3.0.175
