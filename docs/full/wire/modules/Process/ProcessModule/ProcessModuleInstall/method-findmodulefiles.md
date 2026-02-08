# ProcessModuleInstall::findModuleFiles()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Find all module files, recursively in Path

@param string $path Omit to use the default (/site/modules/)

@param int $maxLevel Max depth to pursue module files in (recursion level)

@return array of module classname => full pathname to module file
