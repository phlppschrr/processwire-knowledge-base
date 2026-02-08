# $tfa->startUser(User $user, array $settings): bool

Source: `wire/core/Tfa.php`

Start two-factor authentication for User

Modules must implement this method unless they do not need to generate or send
authentication codes to the user. Below are details on how to implement this
method:

A. For modules that generate and validate their own authentication codes:
   1. Generate an authentication code for user
   2. Save the code to session
   3. Send the code to the user via whatever TFA channel is used
   4. Call parent::startUser($user)
   5. Return true (if no errors)

B. For modules that use an external service to generate, send and validate codes:
   1. Call on the external service to generate and the code to user
   2. Call parent::startUser($user)
   3. Return true (if no errors)

C. Modules that do not generate or send codes, but only validate them (i.e. TOTP):
   You can omit implementation, leaving just the built-in one below.
   But if you do implement it, make sure you call the parent::startUser($user).

## Arguments

- `$user` `User`
- `$settings` `array` Settings configured by user

## Return value

bool True on success, false on fail
