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

## Arguments

- `$startNew` (optional) `bool` Start a new session after logout? (default=true)

## Return value

- `$this`

## Hooking

- Hookable method name: `logout`
- Implementation: `___logout`
- Hook with: `Session::logout`

### Hooking Before

~~~~~
$this->addHookBefore('Session::logout', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $startNew = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $startNew);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Session::logout', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $startNew = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if session is disabled
