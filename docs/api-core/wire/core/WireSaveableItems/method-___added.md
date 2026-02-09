# $wireSaveableItems->added(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after a new item has been added.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->added($item);

// usage with all arguments
$result = $wireSaveableItems->added(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`

## Hooking

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `WireSaveableItems::added`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::added', function(HookEvent $event) {
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
$this->addHookAfter('WireSaveableItems::added', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
