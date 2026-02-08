# $processModuleInstall->findModuleFiles($path = '', $maxLevel = 4): array

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Find all module files, recursively in Path

## Arguments

- string $path Omit to use the default (/site/modules/)
- int $maxLevel Max depth to pursue module files in (recursion level)

## Return value

array of module classname => full pathname to module file
