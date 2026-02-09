# $wireTempDir->init($name = '', $basePath = ''): string

Source: `wire/core/WireTempDir.php`

Initialize temporary directory

This method should only be called once per instance of this class. If you specified a $name argument
in the constructor, then you should not call this method because it will have already been called.

## Usage

~~~~~
// basic usage
$string = $wireTempDir->init();

// usage with all arguments
$string = $wireTempDir->init($name = '', $basePath = '');
~~~~~

## Arguments

- `$name` (optional) `string|object` Recommend providing the object that is using the temp dir, but can also be any string
- `$basePath` (optional) `string` Base path where temp dirs should be created. Omit to use default (recommended).

## Return value

- `string` Returns the root of the temporary directory. Use the get() method to get a dir for use.

## Exceptions

- `WireException` if given a $root that doesn't exist
