# $tfa->autoEnableUser(User $user, array $settings = array())

Source: `wire/core/Tfa.php`

Auto-enable this TFA module for given $user

Automatic enable means a TFA module can be enabled for a user without their input.

This method throws WireException for all error conditions, so you may want to call the
`autoEnableSupported($user)` method first.

## Arguments

- User $user User to auto-enable this Tfa module for.
- array $settings This argument can be omitted in public API usage, but should be specified by Tfa modules in parent::autoEnableForUser() call, containing any needed settings.

## Throws

- WireException on all error conditions

## Meta

- @since 3.0.160
