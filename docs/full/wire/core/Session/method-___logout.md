# $session->___logout($startNew = true): $this

Source: `wire/core/Session.php`

Logout the current user, and clear all session variables

~~~~~
// logout user when "?logout=1" in URL query string
if($input->get('logout')) {
  $session->logout();
	 // good to redirect somewhere else after a login or logout
  $session->redirect('/');
}
~~~~~

## Arguments

- bool $startNew Start a new session after logout? (default=true)

## Return value

$this

## Throws

- WireException if session is disabled
