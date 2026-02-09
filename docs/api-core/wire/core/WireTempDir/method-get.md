# $wireTempDir->get($id = ''): string

Source: `wire/core/WireTempDir.php`

Returns a temporary directory (path)

## Usage

~~~~~
// basic usage
$string = $wireTempDir->get();

// usage with all arguments
$string = $wireTempDir->get($id = '');
~~~~~

## Arguments

- `$id` (optional) `string` Optional identifier to use (default=autogenerate)

## Return value

- `string` Returns path

## Exceptions

- `WireException` If can't create temporary dir
