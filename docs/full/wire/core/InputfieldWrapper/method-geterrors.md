# InputfieldWrapper::getErrors()

Source: `wire/core/InputfieldWrapper.php`

Return an array of errors that occurred on any of the children during input processing.

Should only be called after `InputfieldWrapper::processInput()`.


@param bool $clear Specify true to clear out the errors (default=false).

@return array Array of error strings
