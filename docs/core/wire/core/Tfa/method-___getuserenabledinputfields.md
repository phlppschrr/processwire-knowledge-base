# $tfa->getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings)

Source: `wire/core/Tfa.php`

Get fields for when user already has TFA enabled

This method does not need to be implemented by TFA modules unless they want to add something to it.

## Usage

~~~~~
// basic usage
$result = $tfa->getUserEnabledInputfields($user, $fieldset, $settings);

// usage with all arguments
$result = $tfa->getUserEnabledInputfields(User $user, InputfieldWrapper $fieldset, $settings);
~~~~~

## Hookable

- Hookable method name: `getUserEnabledInputfields`
- Implementation: `___getUserEnabledInputfields`
- Hook with: `$tfa->getUserEnabledInputfields()`

## Arguments

- `$user` `User`
- `$fieldset` `InputfieldWrapper`
- `$settings` `array`
