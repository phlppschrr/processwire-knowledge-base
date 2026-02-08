# $functions->wireUnzipFile($file, $dst, array $options = []): array

Source: `wire/core/Functions.php`

Unzips the given ZIP file to the destination directory

This is procedural version of the `$files->unzip()` method. See that method for more details.

## Arguments

- `$file` `string` ZIP file to extract
- `$dst` `string` Directory where files should be unzipped into. Directory is created if it doesn’t exist.
- `$options` (optional) `array` See `WireFileTools::unzip()` for options.

## Return value

array Returns an array of filenames (excluding $dst) that were unzipped.

## Throws

- WireException All error conditions result in WireException being thrown.

## See also

- [WireFileTools::unzip()](../WireFileTools/method-unzip.md)
