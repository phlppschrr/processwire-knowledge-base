# $fieldtype->savePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Save the given field from given page to the database.

Possible template method: If overridden, it is likely not necessary to call this parent method.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->savePageField($page, $field);

// usage with all arguments
$bool = $fieldtype->savePageField(Page $page, Field $field);
~~~~~

## Hookable

- Hookable method name: `savePageField`
- Implementation: `___savePageField`
- Hook with: `$fieldtype->savePageField()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::savePageField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::savePageField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.

## Return value

- `bool` True on success, false on DB save failure.

## Exceptions

- `WireException|\PDOException|WireDatabaseException`
