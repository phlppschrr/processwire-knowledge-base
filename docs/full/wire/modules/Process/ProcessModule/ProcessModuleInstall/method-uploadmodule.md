# ProcessModuleInstall::uploadModule()

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Process a module upload

@param string $inputName Optionally specify the name of the $_FILES input to look for (default=upload_module)

@param string $destinationDir Optionally specify destination path for completed unzipped files

@return bool|string Returns destinationDir on success, false on failure.
