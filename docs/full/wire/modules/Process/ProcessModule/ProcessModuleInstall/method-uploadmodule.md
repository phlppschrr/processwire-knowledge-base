# $processModuleInstall->uploadModule($inputName = 'upload_module', $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Process a module upload

## Arguments

- string $inputName Optionally specify the name of the $_FILES input to look for (default=upload_module)
- string $destinationDir Optionally specify destination path for completed unzipped files

## Return value

bool|string Returns destinationDir on success, false on failure.
