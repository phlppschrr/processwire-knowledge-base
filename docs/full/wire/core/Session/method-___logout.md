# $session->logout($startNew = true): $this

Source: `wire/core/Session.php`

Logout the current user, and clear all session variables

## Example

~~~~~
// logout user when "?logout=1" in URL query string
if($input->get('logout')) {
  $session->logout();
	 // good to redirect somewhere else after a login or logout
  $session->redirect('/');
}
~~~~~

## Usage

~~~~~
// basic usage
$result = $session->logout();

// usage with all arguments
$result = $session->logout($startNew = true);
~~~~~

## Hookable

- Hookable method name: `logout`
- Implementation: `___logout`
- Hook with: `$session->logout()`

## Arguments

- `$startNew` (optional) `bool` Start a new session after logout? (default=true)

## Return value

- `$this`

## Exceptions

- `WireException` if session is disabled
