# Session::___logout()

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


@param bool $startNew Start a new session after logout? (default=true)

@return $this

@throws WireException if session is disabled
