# $templateFile->setFilename($filename): bool

Source: `wire/core/TemplateFile.php`

Sets the template file name, replacing whatever was set in the constructor

## Arguments

- string $filename Full path and filename to the PHP template file

## Return value

bool true on success, false if file doesn't exist

## Throws

- WireException if file doesn't exist (unless throwExceptions is disabled)
