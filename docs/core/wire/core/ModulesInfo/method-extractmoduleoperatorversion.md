# ModulesInfo::extractModuleOperatorVersion()

Source: `wire/core/ModulesInfo.php`

Return array of ($module, $operator, $requiredVersion)

$version will be 0 and $operator blank if there are no requirements.

@param string $require Module class name with operator and version string

@return array of array($moduleClass, $operator, $version)
