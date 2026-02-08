# $session->isValidSession($userID): bool

Source: `wire/core/Session.php`

Checks if the session is valid based on a challenge cookie and fingerprint

These items may be disabled at the config level, in which case this method always returns true

## Usage

~~~~~
// basic usage
$bool = $session->isValidSession($userID);
~~~~~

## Hookable

- Hookable method name: `isValidSession`
- Implementation: `___isValidSession`
- Hook with: `$session->isValidSession()`

## Arguments

- `$userID` `int`

## Return value

- `bool`
