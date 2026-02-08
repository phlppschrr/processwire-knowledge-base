# $processModuleInstall->uploadModule($inputName = 'upload_module', $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Process a module upload

## Usage

~~~~~
// basic usage
$bool = $processModuleInstall->uploadModule();

// usage with all arguments
$bool = $processModuleInstall->uploadModule($inputName = 'upload_module', $destinationDir = '');
~~~~~

## Arguments

- `$inputName` (optional) `string` Optionally specify the name of the $_FILES input to look for (default=upload_module)
- `$destinationDir` (optional) `string` Optionally specify destination path for completed unzipped files

## Return value

- `bool|string` Returns destinationDir on success, false on failure.
