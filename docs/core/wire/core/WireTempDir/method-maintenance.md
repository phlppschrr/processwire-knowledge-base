# $wireTempDir->maintenance(): bool

Source: `wire/core/WireTempDir.php`

Perform maintenance by cleaning up old temporary directories

Note: This is done automatically if any temporary directories are created during the request.

## Usage

~~~~~
// basic usage
$bool = $wireTempDir->maintenance();
~~~~~

## Return value

- `bool`

## Exceptions

- `WireException`

## Since

3.0.175
