# $tfa->getUserCodeHash(User $user, $code): string

Source: `wire/core/Tfa.php`

Get internal hash of given code for user

This is used to identify and invalidate a previously used authentication code,

## Usage

~~~~~
// basic usage
$string = $tfa->getUserCodeHash($user, $code);

// usage with all arguments
$string = $tfa->getUserCodeHash(User $user, $code);
~~~~~

## Arguments

- `$user` `User`
- `$code` `string`

## Return value

- `string`

## Since

3.0.160
