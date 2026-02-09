# $wireSaveableItems->renamed(Saveable $item, $oldName, $newName)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been renamed.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->renamed($item, $oldName, $newName);

// usage with all arguments
$result = $wireSaveableItems->renamed(Saveable $item, $oldName, $newName);
~~~~~

## Arguments

- `$item` `Saveable`
- `$oldName` `string`
- `$newName` `string`

## Hooking

- Hookable method name: `renamed`
- Implementation: `___renamed`
- Hook with: `WireSaveableItems::renamed`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::renamed', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $oldName = $event->arguments(1);
  $newName = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $oldName);
  $event->arguments(2, $newName);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::renamed', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $oldName = $event->arguments(1);
  $newName = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
