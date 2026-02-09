# $session->allowLoginAttempt($name): bool

Source: `wire/core/Session.php`

Allow login attempt for given name at all?

This method does nothing and is purely for hooks to modify return value.

## Usage

~~~~~
// basic usage
$bool = $session->allowLoginAttempt($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `bool`

## Hooking

- Hookable method name: `allowLoginAttempt`
- Implementation: `___allowLoginAttempt`
- Hook with: `Session::allowLoginAttempt`

### Hooking Before

~~~~~
$this->addHookBefore('Session::allowLoginAttempt', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Session::allowLoginAttempt', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
