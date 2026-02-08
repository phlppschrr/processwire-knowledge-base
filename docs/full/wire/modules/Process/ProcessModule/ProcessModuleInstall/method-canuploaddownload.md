# $processModuleInstall->canUploadDownload($notify = true, $type = ''): bool

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Check that the system supports direct upload and download of modules

This primarily checks that needed dirs are writable and ZipArchive is available.

## Arguments

- `$notify` (optional) `bool` Specify true to make it queue the relevant reason/error message if upload/download not supported. (default=false)
- `$type` (optional) `string` One of 'upload' or 'download' or omit for general check

## Return value

bool
