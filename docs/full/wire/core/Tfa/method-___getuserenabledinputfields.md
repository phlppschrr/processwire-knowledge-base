# $tfa->___getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings)

Source: `wire/core/Tfa.php`

Get fields for when user already has TFA enabled

This method does not need to be implemented by TFA modules unless they want to add something to it.

## Usage

~~~~~
// basic usage
$result = $tfa->___getUserEnabledInputfields($user, $fieldset, $settings);

// usage with all arguments
$result = $tfa->___getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings);
~~~~~

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array`
