# $fieldtype->deletePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given Field from the given Page.

Must delete entries from field's database table that belong to the Page.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->deletePageField($page, $field);

// usage with all arguments
$bool = $fieldtype->deletePageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field` Field object

## Return value

- `bool` True on success, false on DB delete failure.

## Hooking

- Hookable method name: `deletePageField`
- Implementation: `___deletePageField`
- Hook with: `Fieldtype::deletePageField`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::deletePageField', function(HookEvent $event) {
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

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::deletePageField', function(HookEvent $event) {
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

## Exceptions

- `WireException`
