# $session->isValidSession($userID): bool

Source: `wire/core/Session.php`

Checks if the session is valid based on a challenge cookie and fingerprint

These items may be disabled at the config level, in which case this method always returns true

## Usage

~~~~~
// basic usage
$bool = $session->isValidSession($userID);
~~~~~

## Hookable

- Hookable method name: `isValidSession`
- Implementation: `___isValidSession`
- Hook with: `$session->isValidSession()`

## Hooking Before

~~~~~
$this->addHookBefore('Session::isValidSession', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $userID = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $userID);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Session::isValidSession', function(HookEvent $event) {
  $session = $event->object;

  // Get arguments
  $userID = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$userID` `int`

## Return value

- `bool`
