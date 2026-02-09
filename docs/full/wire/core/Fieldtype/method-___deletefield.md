# $fieldtype->deleteField(Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given field, which implies: drop the table used by the field.

This should only be called by the `Fields` class since `fieldgroups_fields` lookup entries must be
deleted before this method is called.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->deleteField($field);

// usage with all arguments
$bool = $fieldtype->deleteField(Field $field);
~~~~~

## Hookable

- Hookable method name: `deleteField`
- Implementation: `___deleteField`
- Hook with: `$fieldtype->deleteField()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::deleteField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::deleteField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$field` `Field` Field object

## Return value

- `bool` True on success, false on DB delete failure.
