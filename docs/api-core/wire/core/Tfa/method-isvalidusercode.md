# $tfa->isValidUserCode(User $user, $code, array $settings): bool|int

Source: `wire/core/Tfa.php`

Return true if code is valid or false if not

Modules MUST implement this method.

## Usage

~~~~~
// basic usage
$bool = $tfa->isValidUserCode($user, $code, $settings);

// usage with all arguments
$bool = $tfa->isValidUserCode(User $user, $code, array $settings);
~~~~~

## Arguments

- `$user` `User`
- `$code` `string|int`
- `$settings` `array` User configured TFA settings

## Return value

- `bool|int` Returns true if valid, false if not, or optionally integer 0 if code was valid but is now expired

## Exceptions

- `WireException`
