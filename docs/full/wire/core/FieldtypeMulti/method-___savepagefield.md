# $fieldtypeMulti->savePageField(Page $page, Field $field): bool

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, Save the given Field from the given Page to the database

Because the number of values may have changed, this method plays it safe and deletes all the old values
and reinserts them as new.

## Usage

~~~~~
// basic usage
$bool = $fieldtypeMulti->savePageField($page, $field);

// usage with all arguments
$bool = $fieldtypeMulti->savePageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Return value

- `bool`

## Hooking

- Hookable method name: `savePageField`
- Implementation: `___savePageField`
- Hook with: `FieldtypeMulti::savePageField`

### Hooking Before

~~~~~
$this->addHookBefore('FieldtypeMulti::savePageField', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FieldtypeMulti::savePageField', function(HookEvent $event) {
  $fieldtypeMulti = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `\PDOException|WireException|WireDatabaseQueryException` on failure
