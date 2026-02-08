# $processModuleInstall->downloadModule($url, $destinationDir = '', $type = 'download'): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Given a URL to a ZIP file, download it, unzip it, and move to /site/modules/[ModuleName]

## Arguments

- `$url` `string` Download URL
- `$destinationDir` (optional) `string` Optional destination path for files (omit to auto-determine)
- `$type` (optional) `string` Specify type of 'download' or 'directory'

## Return value

bool|string Returns destinationDir on success, false on failure.
