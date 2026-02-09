# $tfa->autoEnableSupported(?User $user = null): bool

Source: `wire/core/Tfa.php`

Does this TFA module support automatic enable?

Automatic enable means a TFA module can be enabled for a user without their input.
This can be supported by a module like TfaEmail when/if we already have the user’s email,
but cannot be supported by a module like TfaTotp which requires manual setup by user.

Modules that support auto-enable must implement this method to return true. Modules
that do not support it can ignore this method, as the default returns false.

## Usage

~~~~~
// basic usage
$bool = $tfa->autoEnableSupported();

// usage with all arguments
$bool = $tfa->autoEnableSupported(?User $user = null);
~~~~~

## Arguments

- `$user` (optional) `User|null` Specify user to also confirm it is supported for given user. Omit to test if the module supports it in general.

## Return value

- `bool`

## Since

3.0.160
