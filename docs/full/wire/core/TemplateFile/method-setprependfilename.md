# $templateFile->setPrependFilename($filename): bool

Source: `wire/core/TemplateFile.php`

Set a file to prepend to the template file at render time

## Usage

~~~~~
// basic usage
$bool = $templateFile->setPrependFilename($filename);
~~~~~

## Arguments

- `$filename` `string`

## Return value

- `bool` Returns true on success, false if file doesn't exist.

## Exceptions

- `WireException` if file doesn't exist (unless throwExceptions is disabled)
