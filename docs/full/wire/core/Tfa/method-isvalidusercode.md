# $tfa->isValidUserCode(User $user, $code, array $settings): bool|int

Source: `wire/core/Tfa.php`

Return true if code is valid or false if not

Modules MUST implement this method.

## Arguments

- User $user
- string|int $code
- array $settings User configured TFA settings

## Return value

bool|int Returns true if valid, false if not, or optionally integer 0 if code was valid but is now expired

## Throws

- WireException
