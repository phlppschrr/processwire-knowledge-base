# $wireMailInterface->send(): int

Source: `wire/core/WireMailInterface.php`

Send the email

## Usage

~~~~~
// basic usage
$int = $wireMailInterface->send();
~~~~~

## Hookable

- Hookable method name: `send`
- Implementation: `___send`
- Hook with: `$wireMailInterface->send()`

## Hooking Before

~~~~~
$this->addHookBefore('WireMailInterface::send', function(HookEvent $event) {
  $wireMailInterface = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireMailInterface::send', function(HookEvent $event) {
  $wireMailInterface = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `int` Returns number of messages sent or 0 on failure
