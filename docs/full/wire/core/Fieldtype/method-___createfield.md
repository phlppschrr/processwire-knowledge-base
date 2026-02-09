# $fieldtype->createField(Field $field): bool

Source: `wire/core/Fieldtype.php`

Create a new field table in the database.

This method should execute the SQL query necessary to create $field->table
It should throw a WireException if failure occurs.
Most Fieldtype modules use this built-in implementation.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->createField($field);

// usage with all arguments
$bool = $fieldtype->createField(Field $field);
~~~~~

## Hookable

- Hookable method name: `createField`
- Implementation: `___createField`
- Hook with: `$fieldtype->createField()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::createField', function(HookEvent $event) {
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
$this->addHookAfter('Fieldtype::createField', function(HookEvent $event) {
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

- `$field` `Field`

## Return value

- `bool`

## Exceptions

- `WireException`
