# $processModuleInstall->unzipModule($zipFile, $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Unzip the module file to tempDir and then copy to destination directory

## Arguments

- string $zipFile File to unzip
- string $destinationDir Directory to copy completed files into. Optionally omit to determine automatically.

## Return value

bool|string Returns destinationDir on success, false on failure

## Throws

- WireException
