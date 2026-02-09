# $fieldgroups->load(WireArray $items, $selectors = null): WireArray

Source: `wire/core/Fieldgroups.php`

Load all the Fieldgroups from the database

The loading is delegated to WireSaveableItems.
After loaded, we check for any 'global' fields and add them to the Fieldgroup, if not already there.

## Usage

~~~~~
// basic usage
$items = $fieldgroups->load($items);

// usage with all arguments
$items = $fieldgroups->load(WireArray $items, $selectors = null);
~~~~~

## Hookable

- Hookable method name: `load`
- Implementation: `___load`
- Hook with: `$fieldgroups->load()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::load', function(HookEvent $event) {
  $fieldgroups = $event->object;

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
$this->addHookAfter('Fieldgroups::load', function(HookEvent $event) {
  $fieldgroups = $event->object;

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
