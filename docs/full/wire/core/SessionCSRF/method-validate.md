# $sessionCSRF->validate($id = ''): bool

Source: `wire/core/SessionCSRF.php`

Throws an exception if the token is invalid

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

bool Always returns true or throws exception

## Throws

- WireCSRFException if token not valid
