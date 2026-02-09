# $wireSaveableItems->save(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Save the provided item to database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->save($item);

// usage with all arguments
$bool = $wireSaveableItems->save(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable` The item to save

## Return value

- `bool` Returns true on success, false on failure

## Hooking

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `WireSaveableItems::save`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItems::save', function(HookEvent $event) {
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
$this->addHookAfter('WireSaveableItems::save', function(HookEvent $event) {
  $wireSaveableItems = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`
