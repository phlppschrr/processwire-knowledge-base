# $templateFile->setAppendFilename($filename): bool

Source: `wire/core/TemplateFile.php`

Set a file to append to the template file at render time

## Usage

~~~~~
// basic usage
$bool = $templateFile->setAppendFilename($filename);
~~~~~

## Arguments

- `$filename` `string`

## Return value

- `bool` Returns true on success false if file doesn't exist.

## Exceptions

- `WireException` if file doesn't exist (unless throwExceptions is disabled)
