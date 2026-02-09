# $wireFileTools->unlink($filename, $limitPath = false, $throw = false): bool

Source: `wire/core/WireFileTools.php`

Unlink/delete file with additional protections relative to PHP unlink()

- This method requires a full pathname to a file to unlink and does not
  accept any kind of relative path traversal.

- This method will be limited to unlink files only in /site/assets/ if you
  specify `true` for the `$limitPath` option (recommended).

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->unlink($filename);

// usage with all arguments
$bool = $wireFileTools->unlink($filename, $limitPath = false, $throw = false);
~~~~~

## Arguments

- `$filename` `string`
- `$limitPath` (optional) `string|bool` Limit only to files within some starting path? (default=false) - Boolean true to limit unlink operations to somewhere within /site/assets/ (only known always writable path). - Boolean false to disable to security feature. (default) - An alternative path (string) that represents the starting path (full disk path) to limit deletions to. - An array with multiple of the above string option.
- `$throw` (optional) `bool` Throw exception on error?

## Return value

- `bool` True on success, false on fail

## Exceptions

- `WireException` If file is not allowed to be removed or unlink fails

## Since

3.0.118
