# $tfa->getDefaultUserSettings(User $user): array

Source: `wire/core/Tfa.php`

Get default/blank user settings

Descending modules should implement this method.

## Usage

~~~~~
// basic usage
$array = $tfa->getDefaultUserSettings($user);

// usage with all arguments
$array = $tfa->getDefaultUserSettings(User $user);
~~~~~

## Arguments

- `$user` `User`

## Return value

- `array`
