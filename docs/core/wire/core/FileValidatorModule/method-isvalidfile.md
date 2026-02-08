# FileValidatorModule::isValidFile()

Source: `wire/core/FileValidatorModule.php`

Is the given file valid? (this is the method modules should implement)

This method should return:
	- boolean TRUE if file is valid
	- boolean FALSE if file is not valid
	- integer 1 if file is valid as a result of sanitization performed by this method (if supported by module)

If the file can be made valid by sanitization, this method may also choose to do that (perhaps if configured
to do so) and return integer 1 after doing so.

If method wants to explain why the file is not valid, it should call $this->error('reason why not valid').

@param string $filename Full path and filename to the file

@return bool|int
