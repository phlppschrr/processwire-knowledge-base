# $wireSaveableItems->deleteReady(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be deleted.

Unlike before(delete), when this runs, it has already been confirmed that the item will indeed be deleted.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->deleteReady($item);

// usage with all arguments
$result = $wireSaveableItems->deleteReady(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `$wireSaveableItems->deleteReady()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::deleteReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::deleteReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable`
