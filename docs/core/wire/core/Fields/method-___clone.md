# $fields->clone(Saveable $item, $name = ''): Field

Source: `wire/core/Fields.php`

Create and return a cloned copy of the given Field

## Usage

~~~~~
// basic usage
$field = $fields->clone($item);

// usage with all arguments
$field = $fields->clone(Saveable $item, $name = '');
~~~~~

## Hookable

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `$fields->clone()`

## Hooking Before

~~~~~
$this->addHookBefore('Fields::clone', function(HookEvent $event) {
  $fields = $event->object;

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
$this->addHookAfter('Fields::clone', function(HookEvent $event) {
  $fields = $event->object;

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

- `$item` `Field` Field to clone
- `$name` (optional) `string` Optionally specify name for new cloned item

## Return value

- `Field` $item Returns the new clone on success, or false on failure
