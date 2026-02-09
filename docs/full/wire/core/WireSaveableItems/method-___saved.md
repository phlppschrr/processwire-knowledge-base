# $wireSaveableItems->saved(Saveable $item, array $changes = array())

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been saved.

Unlike after(save), when this runs, it has already been confirmed that the item has been saved (no need to error check).

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->saved($item);

// usage with all arguments
$result = $wireSaveableItems->saved(Saveable $item, array $changes = array());
~~~~~

## Hookable

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `$wireSaveableItems->saved()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::saved', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $changes = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $changes);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::saved', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $changes = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable`
- `$changes` (optional) `array`
