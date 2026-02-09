# $wireShutdown->fatalError($error)

Source: `wire/core/WireShutdown.php`

Hook called when fatal error received by shutdown()

## Usage

~~~~~
// basic usage
$result = $wireShutdown->fatalError($error);
~~~~~

## Hookable

- Hookable method name: `fatalError`
- Implementation: `___fatalError`
- Hook with: `$wireShutdown->fatalError()`

## Hooking Before

~~~~~
$this->addHookBefore('WireShutdown::fatalError', function(HookEvent $event) {
  $wireShutdown = $event->object;

  // Get arguments
  $error = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $error);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireShutdown::fatalError', function(HookEvent $event) {
  $wireShutdown = $event->object;

  // Get arguments
  $error = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$error` `array`

## Since

3.0.173
