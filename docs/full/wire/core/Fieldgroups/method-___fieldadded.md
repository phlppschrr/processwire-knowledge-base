# $fieldgroups->fieldAdded(Fieldgroup $fieldgroup, Field $field)

Source: `wire/core/Fieldgroups.php`

Hook called when field has been added to fieldgroup

## Usage

~~~~~
// basic usage
$result = $fieldgroups->fieldAdded($fieldgroup, $field);

// usage with all arguments
$result = $fieldgroups->fieldAdded(Fieldgroup $fieldgroup, Field $field);
~~~~~

## Hookable

- Hookable method name: `fieldAdded`
- Implementation: `___fieldAdded`
- Hook with: `$fieldgroups->fieldAdded()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::fieldAdded', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldgroup);
  $event->arguments(1, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::fieldAdded', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$fieldgroup` `Fieldgroup`
- `$field` `Field`

## Since

3.0.193
