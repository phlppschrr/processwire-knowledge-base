# $tfa->getSessionKey($reset = false): string

Source: `wire/core/Tfa.php`

Get a unique key that can be used in the “tfa” GET variable used by this module

## Usage

~~~~~
// basic usage
$string = $tfa->getSessionKey();

// usage with all arguments
$string = $tfa->getSessionKey($reset = false);
~~~~~

## Arguments

- `$reset` (optional) `bool` Reset to new key?

## Return value

- `string`
