# $functions->wireTempDir($name, $options = array()): WireTempDir

Source: `wire/core/Functions.php`

Return a new temporary directory/path ready to use for files

- The directory will be automatically removed after a set period of time (default=120s).
- This is a procedural version of the `$files->tempDir()` method.

~~~~~
$td = wireTempDir('hello-world');
$path = (string) $td; // or use $td->get();
file_put_contents($path . 'some-file.txt', 'Hello world');
~~~~~

## Arguments

- Object|string $name Provide the object that needs the temp dir, or name your own string
- array|int $options Options array to modify default behavior: - `maxAge` (integer): Maximum age of temp dir files in seconds (default=120) - `basePath` (string): Base path where temp dirs should be created. Omit to use default (recommended). - Note: if you specify an integer for $options, then 'maxAge' is assumed.

## Return value

WireTempDir If you typecast return value to a string, it is the temp dir path (with trailing slash).

## See also

- [WireFileTools::tempDir()](../WireFileTools/method-tempdir.md)
- WireTempDir
