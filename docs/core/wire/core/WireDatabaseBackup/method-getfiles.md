# $wireDatabaseBackup->getFiles($getObjects = false): array|\SplFileInfo[]

Source: `wire/core/WireDatabaseBackup.php`

Return array of all backup files

To get additional info on any of them, call getFileInfo($basename) method

## Usage

~~~~~
// basic usage
$array = $wireDatabaseBackup->getFiles();

// usage with all arguments
$array = $wireDatabaseBackup->getFiles($getObjects = false);
~~~~~

## Arguments

- `$getObjects` (optional) `bool` Get SplFileInfo objects rather than basenames? (3.0.214+)

## Return value

- `array|\SplFileInfo[]` Array of strings (basenames), or array of SplFileInfo objects (when requested)
