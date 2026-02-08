# $processModuleInstall->findModuleFiles($path = '', $maxLevel = 4): array

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Find all module files, recursively in Path

## Arguments

- `$path` (optional) `string` Omit to use the default (/site/modules/)
- `$maxLevel` (optional) `int` Max depth to pursue module files in (recursion level)

## Return value

array of module classname => full pathname to module file
