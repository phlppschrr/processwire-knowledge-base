# $wireAction->executeMultiple($items): int

Source: `wire/core/WireAction.php`

Execute the action for multiple items at once

## Usage

~~~~~
// basic usage
$int = $wireAction->executeMultiple($items);
~~~~~

## Arguments

- `$items` `array|WireArray` Items to operate upon

## Return value

- `int` Returns quantity of items successfully operated upon

## Hooking

- Hookable method name: `executeMultiple`
- Implementation: `___executeMultiple`
- Hook with: `WireAction::executeMultiple`

### Hooking Before

~~~~~
$this->addHookBefore('WireAction::executeMultiple', function(HookEvent $event) {
  $wireAction = $event->object;

  // Get arguments
  $items = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $items);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireAction::executeMultiple', function(HookEvent $event) {
  $wireAction = $event->object;

  // Get arguments
  $items = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` when it receives an unexpected type for $items
