# $session->loginSuccess(User $user)

Source: `wire/core/Session.php`

Login success method for hooks

## Usage

~~~~~
// basic usage
$result = $session->loginSuccess($user);

// usage with all arguments
$result = $session->loginSuccess(User $user);
~~~~~

## Arguments

- `$user` `User`

## Hooking

- Hookable method name: `loginSuccess`
- Implementation: `___loginSuccess`
- Hook with: `Session::loginSuccess`

### Hooking Before

~~~~~
$this->addHookBefore('Session::loginSuccess', function(HookEvent $event) {
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
$this->addHookAfter('Session::loginSuccess', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $user = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
