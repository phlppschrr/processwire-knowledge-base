# $session->init()

Source: `wire/core/Session.php`

Start the session

Provided here in any case anything wants to hook in before session_start()
is called to provide an alternate save handler.

## Usage

~~~~~
// basic usage
$result = $session->init();
~~~~~

## Hookable

- Hookable method name: `init`
- Implementation: `___init`
- Hook with: `$session->init()`

## Hooking Before

~~~~~
$this->addHookBefore('Session::init', function(HookEvent $event) {
  $session = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Session::init', function(HookEvent $event) {
  $session = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
