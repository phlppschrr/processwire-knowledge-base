# $session->authenticate(User $user, $pass): bool

Source: `wire/core/Session.php`

Return true or false whether the user authenticated with the supplied password

## Usage

~~~~~
// basic usage
$bool = $session->authenticate($user, $pass);

// usage with all arguments
$bool = $session->authenticate(User $user, $pass);
~~~~~

## Arguments

- `$user` `User` User attempting to login
- `$pass` `string` Password they are attempting to login with

## Return value

- `bool`

## Hooking

- Hookable method name: `authenticate`
- Implementation: `___authenticate`
- Hook with: `Session::authenticate`

### Hooking Before

~~~~~
$this->addHookBefore('Session::authenticate', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $pass = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $user);
  $event->arguments(1, $pass);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Session::authenticate', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $user = $event->arguments(0);
  $pass = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
