# $functions->wireUnzipFile($file, $dst, array $options = []): array

Source: `wire/core/Functions.php`

Unzips the given ZIP file to the destination directory

This is procedural version of the `$files->unzip()` method. See that method for more details.

## Usage

~~~~~
// basic usage
$array = $functions->wireUnzipFile($file, $dst);

// usage with all arguments
$array = $functions->wireUnzipFile($file, $dst, array $options = []);
~~~~~

## Arguments

- `$file` `string` ZIP file to extract
- `$dst` `string` Directory where files should be unzipped into. Directory is created if it doesn’t exist.
- `$options` (optional) `array` See `WireFileTools::unzip()` for options.

## Return value

- `array` Returns an array of filenames (excluding $dst) that were unzipped.

## Exceptions

- `WireException` All error conditions result in WireException being thrown.

## See Also

- [WireFileTools::unzip()](../WireFileTools/method-unzip.md)
