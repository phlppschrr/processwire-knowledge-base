# $tfa->saveUserSettings(User $user, array $settings): bool

Source: `wire/core/Tfa.php`

Save TFA data for given user to user_tfa field

## Usage

~~~~~
// basic usage
$bool = $tfa->saveUserSettings($user, $settings);

// usage with all arguments
$bool = $tfa->saveUserSettings(User $user, array $settings);
~~~~~

## Arguments

- `$user` `User`
- `$settings` `array`

## Return value

- `bool`

## Exceptions

- `WireException`
