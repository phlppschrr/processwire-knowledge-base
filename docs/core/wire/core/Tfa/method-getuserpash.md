# Tfa::getUserPash()

Source: `wire/core/Tfa.php`

Get internal user pass hash

This is used to represent a user + pass hash in a temporary session value.
It helps to identify if a user’s password changed between the time they
authenticated and the time they submitted the authentication code. While
it seems extremely unlikely, I think we have to cover this, just in case.

@param User $user

@return string

@since 3.0.160
