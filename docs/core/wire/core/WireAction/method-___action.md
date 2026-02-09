# $wireAction->action($item): bool

Source: `wire/core/WireAction.php`

Perform the action on the given item

## Usage

~~~~~
// basic usage
$bool = $wireAction->action($item);
~~~~~

## Hookable

- Hookable method name: `action`
- Implementation: `___action`
- Hook with: `$wireAction->action()`

## Hooking Before

~~~~~
$this->addHookBefore('WireAction::action', function(HookEvent $event) {
  $wireAction = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireAction::action', function(HookEvent $event) {
  $wireAction = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Wire` Item to operate upon

## Return value

- `bool` True if the item was successfully operated upon, false if not.
