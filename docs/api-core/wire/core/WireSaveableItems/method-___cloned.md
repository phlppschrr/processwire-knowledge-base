# $wireSaveableItems->cloned(Saveable $item, Saveable $copy)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been cloned.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->cloned($item, $copy);

// usage with all arguments
$result = $wireSaveableItems->cloned(Saveable $item, Saveable $copy);
~~~~~

## Arguments

- `$item` `Saveable`
- `$copy` `Saveable`

## Hooking

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `WireSaveableItems::cloned`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::cloned', function(HookEvent $event) {
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

### Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::cloned', function(HookEvent $event) {
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
