# Tfa::autoEnableUser()

Source: `wire/core/Tfa.php`

Auto-enable this TFA module for given $user

Automatic enable means a TFA module can be enabled for a user without their input.

This method throws WireException for all error conditions, so you may want to call the
`autoEnableSupported($user)` method first.

@param User $user User to auto-enable this Tfa module for.

@param array $settings This argument can be omitted in public API usage, but should be specified
  by Tfa modules in parent::autoEnableForUser() call, containing any needed settings.

@throws WireException on all error conditions

@since 3.0.160
