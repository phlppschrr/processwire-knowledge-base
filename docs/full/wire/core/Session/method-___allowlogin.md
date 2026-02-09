# $session->allowLogin($name, $user = null): bool

Source: `wire/core/Session.php`

Allow the user $name to login? Provided for use by hooks.

## Usage

~~~~~
// basic usage
$bool = $session->allowLogin($name);

// usage with all arguments
$bool = $session->allowLogin($name, $user = null);
~~~~~

## Hookable

- Hookable method name: `allowLogin`
- Implementation: `___allowLogin`
- Hook with: `$session->allowLogin()`

## Hooking Before

~~~~~
$this->addHookBefore('Session::allowLogin', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $user);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Session::allowLogin', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$name` `string` User login name
- `$user` (optional) `User|null` User object

## Return value

- `bool` True if allowed to login, false if not (hooks may modify this)
