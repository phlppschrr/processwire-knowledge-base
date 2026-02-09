# $wireSaveableItems->clone(Saveable $item, $name = ''): bool|Saveable

Source: `wire/core/WireSaveableItems.php`

Create and return a cloned copy of this item

If no name is specified and the new item uses a 'name' field, it will contain a number at the end to make it unique

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->clone($item);

// usage with all arguments
$bool = $wireSaveableItems->clone(Saveable $item, $name = '');
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$wireSaveableItems->clone()`

## Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::clone', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $name);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireSaveableItems::clone', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable` Item to clone
- `$name` (optional) `string` Optionally specify new name

## Return value

- `bool|Saveable` $item Returns the new clone on success, or false on failure
