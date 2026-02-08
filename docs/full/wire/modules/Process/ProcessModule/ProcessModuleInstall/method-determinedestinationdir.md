# ProcessModuleInstall::determineDestinationDir()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Given a list of files from a module (and their temp dir) return the recommended directory name for it to live in

i.e. /site/modules/[ModuleDir]/

@param array $files Files found in the module's ZIP file

@param string $modulePath Path where module will live

@return bool|string Returns false if no module files found. Otherwise returns string with module path.
