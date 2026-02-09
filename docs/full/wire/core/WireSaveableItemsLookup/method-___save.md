# $wireSaveableItemsLookup->save(Saveable $item): bool

Source: `wire/core/WireSaveableItemsLookup.php`

Save the provided item to database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItemsLookup->save($item);

// usage with all arguments
$bool = $wireSaveableItemsLookup->save(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`

## Return value

- `bool`

## Hooking

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `WireSaveableItemsLookup::save`

### Hooking Before

~~~~~
$this->addHookBefore('WireSaveableItemsLookup::save', function(HookEvent $event) {
  $wireSaveableItemsLookup = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireSaveableItemsLookup::save', function(HookEvent $event) {
  $wireSaveableItemsLookup = $event->object;

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
