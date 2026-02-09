# $tfa->getUserSettings(User $user): array

Source: `wire/core/Tfa.php`

Get TFA data for given user from user_tfa field

## Usage

~~~~~
// basic usage
$array = $tfa->getUserSettings($user);

// usage with all arguments
$array = $tfa->getUserSettings(User $user);
~~~~~

## Arguments

- `$user` `User`

## Return value

- `array`

## Exceptions

- `WireException`
