# $wireDatabaseBackup->sanitizeFilename($filename): string

Source: `wire/core/WireDatabaseBackup.php`

For filename: Normalizes slashes and ensures it starts with a path

## Usage

~~~~~
// basic usage
$string = $wireDatabaseBackup->sanitizeFilename($filename);
~~~~~

## Arguments

- $filename

## Return value

- `string`

## Exceptions

- `\Exception` if path has not yet been set
