# $tfa->sessionReset($redirectURL = ''): false

Source: `wire/core/Tfa.php`

Remove all session variables set for this module

## Usage

~~~~~
// basic usage
$result = $tfa->sessionReset();

// usage with all arguments
$result = $tfa->sessionReset($redirectURL = '');
~~~~~

## Arguments

- `$redirectURL` (optional) `string` Optionally redirect to URL after reset

## Return value

- `false`
