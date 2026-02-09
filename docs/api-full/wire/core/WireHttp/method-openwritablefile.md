# $wireHttp->openWritableFile($toFile, $fp = false): resource

Source: `wire/core/WireHttp.php`

Open a new file for writing (for download methods)

## Usage

~~~~~
// basic usage
$result = $wireHttp->openWritableFile($toFile);

// usage with all arguments
$result = $wireHttp->openWritableFile($toFile, $fp = false);
~~~~~

## Arguments

- `$toFile` `string`
- `$fp` (optional) `resource|false`

## Return value

- `resource`

## Exceptions

- `WireException`

## Since

3.0.222
