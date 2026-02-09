# $wireSaveableItems->delete(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Delete the provided item from the database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->delete($item);

// usage with all arguments
$bool = $wireSaveableItems->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$wireSaveableItems->delete()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::delete', function(HookEvent $event) {
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
$this->addHookAfter('WireSaveableItems::delete', function(HookEvent $event) {
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

- `$item` `Saveable` Item to save

## Return value

- `bool` Returns true on success, false on failure

## Exceptions

- `WireException`
