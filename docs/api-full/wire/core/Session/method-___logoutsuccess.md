# $session->logoutSuccess(User $user)

Source: `wire/core/Session.php`

Logout success method for hooks

## Usage

~~~~~
// basic usage
$result = $session->logoutSuccess($user);

// usage with all arguments
$result = $session->logoutSuccess(User $user);
~~~~~

## Arguments

- `$user` `User` User that logged in

## Hooking

- Hookable method name: `logoutSuccess`
- Implementation: `___logoutSuccess`
- Hook with: `Session::logoutSuccess`

### Hooking Before

~~~~~
$this->addHookBefore('Session::logoutSuccess', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $user = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $user);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Session::logoutSuccess', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $user = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
