# $processModuleInstall->unzipModule($zipFile, $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Unzip the module file to tempDir and then copy to destination directory

## Usage

~~~~~
// basic usage
$bool = $processModuleInstall->unzipModule($zipFile);

// usage with all arguments
$bool = $processModuleInstall->unzipModule($zipFile, $destinationDir = '');
~~~~~

## Arguments

- `$zipFile` `string` File to unzip
- `$destinationDir` (optional) `string` Directory to copy completed files into. Optionally omit to determine automatically.

## Return value

- `bool|string` Returns destinationDir on success, false on failure

## Exceptions

- `WireException`
