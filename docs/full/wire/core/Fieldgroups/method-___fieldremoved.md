# $fieldgroups->fieldRemoved(Fieldgroup $fieldgroup, Field $field)

Source: `wire/core/Fieldgroups.php`

Hook called when field has been removed from fieldgroup

## Usage

~~~~~
// basic usage
$result = $fieldgroups->fieldRemoved($fieldgroup, $field);

// usage with all arguments
$result = $fieldgroups->fieldRemoved(Fieldgroup $fieldgroup, Field $field);
~~~~~

## Hookable

- Hookable method name: `fieldRemoved`
- Implementation: `___fieldRemoved`
- Hook with: `$fieldgroups->fieldRemoved()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::fieldRemoved', function(HookEvent $event) {
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
$this->addHookAfter('Fieldgroups::fieldRemoved', function(HookEvent $event) {
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
