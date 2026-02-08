# ProcessModuleInstall::getTempDir()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Returns a temporary directory (path) for use by this object

@return string|bool Returns false if you specified $create=false, and the dir doesn't exist

@throws WireException If can't create temporary dir
