# SessionCSRF::hasValidToken()

Source: `wire/core/SessionCSRF.php`

Returns true if the current POST request contains a valid CSRF token, false if not


@param int|string|null $id Optional unique ID for this token, but required if checking a single use token.

@param bool|null Reset after checking? Or omit (null) for auto (which resets if single-use token, and not otherwise).

@return bool
