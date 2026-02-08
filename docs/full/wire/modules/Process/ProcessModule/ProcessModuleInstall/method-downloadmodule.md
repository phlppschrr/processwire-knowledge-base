# ProcessModuleInstall::downloadModule()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Given a URL to a ZIP file, download it, unzip it, and move to /site/modules/[ModuleName]

@param string $url Download URL

@param string $destinationDir Optional destination path for files (omit to auto-determine)

@param string $type Specify type of 'download' or 'directory'

@return bool|string Returns destinationDir on success, false on failure.
