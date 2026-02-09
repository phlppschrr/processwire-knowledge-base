# $fieldtype->cloneField(Field $field): Field

Source: `wire/core/Fieldtype.php`

Return a cloned copy of $field

## Usage

~~~~~
// basic usage
$field = $fieldtype->cloneField($field);

// usage with all arguments
$field = $fieldtype->cloneField(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `Field` cloned copy

## Hooking

- Hookable method name: `cloneField`
- Implementation: `___cloneField`
- Hook with: `Fieldtype::cloneField`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::cloneField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::cloneField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $field = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
