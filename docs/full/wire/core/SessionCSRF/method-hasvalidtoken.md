# $sessionCSRF->hasValidToken($id = '', $reset = null): bool

Source: `wire/core/SessionCSRF.php`

Returns true if the current POST request contains a valid CSRF token, false if not

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token, but required if checking a single use token.
- bool|null Reset after checking? Or omit (null) for auto (which resets if single-use token, and not otherwise).

## Return value

bool
