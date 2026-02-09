# $wireTempDir->createName($prefix = ''): string

Source: `wire/core/WireTempDir.php`

Create a randomized name for runtime temp dir

## Usage

~~~~~
// basic usage
$string = $wireTempDir->createName();

// usage with all arguments
$string = $wireTempDir->createName($prefix = '');
~~~~~

## Arguments

- `$prefix` (optional) `string` Optional prefix for name

## Return value

- `string`
