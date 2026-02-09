# $session->loginFailure($name, $reason)

Source: `wire/core/Session.php`

Login failure method for hooks

## Usage

~~~~~
// basic usage
$result = $session->loginFailure($name, $reason);
~~~~~

## Hookable

- Hookable method name: `loginFailure`
- Implementation: `___loginFailure`
- Hook with: `$session->loginFailure()`

## Hooking Before

~~~~~
$this->addHookBefore('Session::loginFailure', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $reason = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $reason);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Session::loginFailure', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $reason = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$name` `string` Attempted login name
- `$reason` `string` Reason for login failure
