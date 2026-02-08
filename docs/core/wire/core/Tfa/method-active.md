# $tfa->active(): bool

Source: `wire/core/Tfa.php`

Returns true if a TFA process is currently active

- This method should be called if $tfa->success() returns false.
- If this method returns true, you should `echo $tfa->render()` which will
  render the auth code form.
- If this method returns false and login/pass submitted, then call `$tfa->start()`,
  or if login not submitted, then render login form.

## Return value

bool
