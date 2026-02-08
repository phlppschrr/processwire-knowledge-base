# $processModuleInstall->determineDestinationDir(array $files, $modulePath = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Given a list of files from a module (and their temp dir) return the recommended directory name for it to live in

i.e. /site/modules/[ModuleDir]/

## Arguments

- `$files` `array` Files found in the module's ZIP file
- `$modulePath` (optional) `string` Path where module will live

## Return value

bool|string Returns false if no module files found. Otherwise returns string with module path.
