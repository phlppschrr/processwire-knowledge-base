# $wireSaveableItems->cloneReady(Saveable $item, Saveable $copy)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be cloned.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->cloneReady($item, $copy);

// usage with all arguments
$result = $wireSaveableItems->cloneReady(Saveable $item, Saveable $copy);
~~~~~

## Hookable

- Hookable method name: `cloneReady`
- Implementation: `___cloneReady`
- Hook with: `$wireSaveableItems->cloneReady()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::cloneReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $copy = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $copy);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::cloneReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $copy = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable`
- `$copy` `Saveable`
