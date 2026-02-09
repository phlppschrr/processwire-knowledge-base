# $fieldgroups->delete(Saveable $item): bool

Source: `wire/core/Fieldgroups.php`

Delete the given fieldgroup from the database

Also deletes the references in fieldgroups_fields table

## Usage

~~~~~
// basic usage
$bool = $fieldgroups->delete($item);

// usage with all arguments
$bool = $fieldgroups->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$fieldgroups->delete()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::delete', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::delete', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$item` `Saveable|Fieldgroup`

## Return value

- `bool`

## Exceptions

- `WireException`
