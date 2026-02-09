# $wireSaveableItems->find($selectors): WireArray

Source: `wire/core/WireSaveableItems.php`

Find items based on Selectors or selector string

This is a delegation to the WireArray associated with this DAO.
This method assumes that all items are loaded. Desecending classes that don't load all items should
override this to the ___load() method instead.

## Usage

~~~~~
// basic usage
$items = $wireSaveableItems->find($selectors);
~~~~~

## Arguments

- `$selectors` `Selectors|string`

## Return value

- `WireArray`

## Hooking

- Hookable method name: `find`
- Implementation: `___find`
- Hook with: `WireSaveableItems::find`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::find', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $selectors = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $selectors);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::find', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $selectors = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
