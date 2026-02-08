# $session->___isValidSession($userID): bool

Source: `wire/core/Session.php`

Checks if the session is valid based on a challenge cookie and fingerprint

These items may be disabled at the config level, in which case this method always returns true

## Arguments

- `$userID` `int`

## Return value

bool
