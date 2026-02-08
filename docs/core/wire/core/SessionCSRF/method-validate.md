# SessionCSRF::validate()

Source: `wire/core/SessionCSRF.php`

Throws an exception if the token is invalid


@param int|string|null $id Optional unique ID for this token

@throws WireCSRFException if token not valid

@return bool Always returns true or throws exception
