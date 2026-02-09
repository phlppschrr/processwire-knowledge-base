# $fieldgroups->saveContext(Fieldgroup $fieldgroup): int

Source: `wire/core/Fieldgroups.php`

Save contexts for all fields in the given fieldgroup

## Usage

~~~~~
// basic usage
$int = $fieldgroups->saveContext($fieldgroup);

// usage with all arguments
$int = $fieldgroups->saveContext(Fieldgroup $fieldgroup);
~~~~~

## Arguments

- `$fieldgroup` `Fieldgroup`

## Return value

- `int` Number of field contexts saved

## Hooking

- Hookable method name: `saveContext`
- Implementation: `___saveContext`
- Hook with: `Fieldgroups::saveContext`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::saveContext', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldgroup);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::saveContext', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
