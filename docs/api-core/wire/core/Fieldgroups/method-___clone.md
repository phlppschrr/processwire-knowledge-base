# $fieldgroups->clone(Saveable $item, $name = ''): Fieldgroup|false

Source: `wire/core/Fieldgroups.php`

Create and return a cloned copy of this item

If the new item uses a 'name' field, it will contain a number at the end to make it unique

## Usage

~~~~~
// basic usage
$fieldgroup = $fieldgroups->clone($item);

// usage with all arguments
$fieldgroup = $fieldgroups->clone(Saveable $item, $name = '');
~~~~~

## Arguments

- `$item` `Saveable` Item to clone
- `$name` (optional) `string`

## Return value

- `Fieldgroup|false` $item Returns the new clone on success, or false on failure

## Hooking

- Hookable method name: `clone`
- Implementation: `___clone`
- Hook with: `Fieldgroups::clone`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::clone', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
  $event->arguments(1, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::clone', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $item = $event->arguments(0);
  $name = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
