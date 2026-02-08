# FileValidatorModule::isValid()

Source: `wire/core/FileValidatorModule.php`

Is the given file valid?

FileValidator modules should not implement this method, as it only serves as a front-end to isValid()
for logging purposes.

@param string $filename

@return bool|int Returns TRUE if valid, FALSE if not, or integer 1 if valid as a result of sanitization.
