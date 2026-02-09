# $fields->delete(Saveable $item): bool

Source: `wire/core/Fields.php`

Delete a Field from the database

This method will throw a WireException if you attempt to delete a field that is currently in use (i.e. assigned to one or more fieldgroups).

## Usage

~~~~~
// basic usage
$bool = $fields->delete($item);

// usage with all arguments
$bool = $fields->delete(Saveable $item);
~~~~~

## Arguments

- `$item` `Field` Field to delete

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Fields::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Fields::delete', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fields::delete', function(HookEvent $event) {
  $fields = $event->object;

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
