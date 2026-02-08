# ProcessModuleInstall::unzipModule()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Unzip the module file to tempDir and then copy to destination directory

@param string $zipFile File to unzip

@param string $destinationDir Directory to copy completed files into. Optionally omit to determine automatically.

@return bool|string Returns destinationDir on success, false on failure

@throws WireException
