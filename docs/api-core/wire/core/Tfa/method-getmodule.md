# $tfa->getModule(?User $user = null): Tfa|null

Source: `wire/core/Tfa.php`

Get the TFA module for given user or current session

## Usage

~~~~~
// basic usage
$tfa = $tfa->getModule();

// usage with all arguments
$tfa = $tfa->getModule(?User $user = null);
~~~~~

## Arguments

- `$user` (optional) `User|null` Optionally specify user

## Return value

- `Tfa|null`
