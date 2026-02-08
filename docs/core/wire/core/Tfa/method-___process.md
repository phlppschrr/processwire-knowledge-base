# $tfa->___process(): User|bool

Source: `wire/core/Tfa.php`

Process two-factor authentication code input

This method processes the submission of the form containing “tfa_code”.
Note that this method will perform redirects as needed.

## Return value

User|bool Returns logged-in user object on successful code completion, or false on fail
