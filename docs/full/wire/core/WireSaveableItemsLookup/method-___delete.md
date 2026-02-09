# $wireSaveableItemsLookup->delete(Saveable $item): bool

Source: `wire/core/WireSaveableItemsLookup.php`

Delete the provided item from the database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItemsLookup->delete($item);

// usage with all arguments
$bool = $wireSaveableItemsLookup->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$wireSaveableItemsLookup->delete()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItemsLookup::delete', function(HookEvent $event) {
  $wireSaveableItemsLookup = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItemsLookup::delete', function(HookEvent $event) {
  $wireSaveableItemsLookup = $event->object;

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

## Return value

- `bool`
