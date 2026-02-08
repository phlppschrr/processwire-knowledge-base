# $modulesInfo->extractModuleOperatorVersion($require): array

Source: `wire/core/ModulesInfo.php`

Return array of ($module, $operator, $requiredVersion)

$version will be 0 and $operator blank if there are no requirements.

## Arguments

- string $require Module class name with operator and version string

## Return value

array of array($moduleClass, $operator, $version)
