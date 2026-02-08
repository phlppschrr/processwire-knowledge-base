# Inputfield::getErrors()

Source: `wire/core/Inputfield.php`

Return array of strings containing errors that occurred during input processing

Note that this is different from `Wire::errors()` in that it retrieves errors from the session
rather than just the current run.


@param bool $clear Optionally clear the errors after getting them (Default=false).

@return array
