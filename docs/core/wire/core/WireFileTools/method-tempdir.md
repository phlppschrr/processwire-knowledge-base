# $wireFileTools->tempDir($name = '', $options = array()): WireTempDir

Source: `wire/core/WireFileTools.php`

Return a new temporary directory/path ready to use for files

- The temporary directory will be automatically removed at the end of the request.
- Temporary directories are not http accessible.
- If you call this with the same non-empty `$name` argument more than once in the
  same request, the same `WireTempDir` instance will be returned.


~~~~~
$tempDir = $files->tempDir();
$path = $tempDir->get();
file_put_contents($path . 'some-file.txt', 'Hello world');
~~~~~

## Arguments

- `$name` (optional) `Object|string` Any one of the following: (default='') - Omit this argument for auto-generated name, 3.0.178+ - Name/word that you specify using fieldName format, i.e. [_a-zA-Z0-9]. - Object instance that needs the temp dir.
- `$options` (optional) `array|int` Deprecated argument. Call `WireTempDir` methods if you need more options.

## Return value

WireTempDir Returns a WireTempDir instance. If you typecast return value to a string, it is the temp dir path (with trailing slash).

## See also

- WireTempDir
