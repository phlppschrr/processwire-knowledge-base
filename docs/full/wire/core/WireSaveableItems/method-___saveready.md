# $wireSaveableItems->saveReady(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be saved.

Unlike before(save), when this runs, it has already been confirmed that the item will indeed be saved.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->saveReady($item);

// usage with all arguments
$result = $wireSaveableItems->saveReady(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`

## Hooking

- Hookable method name: `saveReady`
- Implementation: `___saveReady`
- Hook with: `WireSaveableItems::saveReady`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::saveReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::saveReady', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
