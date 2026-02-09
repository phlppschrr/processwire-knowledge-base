# $wireSaveableItems->deleted(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been deleted.

Unlike after(delete), it has already been confirmed that the item was indeed deleted.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->deleted($item);

// usage with all arguments
$result = $wireSaveableItems->deleted(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`

## Hooking

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `WireSaveableItems::deleted`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::deleted', function(HookEvent $event) {
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
$this->addHookAfter('WireSaveableItems::deleted', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
