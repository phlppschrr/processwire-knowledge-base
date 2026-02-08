# $tfa->___getUserSettingsInputfields(User $user, InputfieldWrapper $fieldset, $settings)

Source: `wire/core/Tfa.php`

Get fields needed for a user to configure and confirm TFA from their user profile

This method should be implemented by each TFA module. It is only used when the user has selected
a TFA type and submitted form, but has not yet configured the TFA type.

## Arguments

- User $user
- InputfieldWrapper $fieldset
- array $settings
