# $wireSaveableItems->load(WireArray $items, $selectors = null): WireArray

Source: `wire/core/WireSaveableItems.php`

Load items from the database table and return them in the same type class that getAll() returns

A selector string or Selectors may be provided so that this can be used as a find() by descending classes that don't load all items at once.

## Usage

~~~~~
// basic usage
$items = $wireSaveableItems->load($items);

// usage with all arguments
$items = $wireSaveableItems->load(WireArray $items, $selectors = null);
~~~~~

## Hookable

- Hookable method name: `load`
- Implementation: `___load`
- Hook with: `$wireSaveableItems->load()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::load', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $items = $event->arguments(0);
  $selectors = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $items);
  $event->arguments(1, $selectors);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::load', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $items = $event->arguments(0);
  $selectors = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$items` `WireArray`
- `$selectors` (optional) `Selectors|string|null` Selectors or a selector string to find, or NULL to load all.

## Return value

- `WireArray` Returns the same type as specified in the getAll() method.
