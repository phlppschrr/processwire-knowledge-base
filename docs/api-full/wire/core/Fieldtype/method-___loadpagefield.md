# $fieldtype->loadPageField(Page $page, Field $field): mixed|null

Source: `wire/core/Fieldtype.php`

Load the given page field from the database table and return the value.

- Return NULL if the value is not available.
- Return the value as it exists in the database, without further processing.
- This is intended only to be called by Page objects on an as-needed basis.
- Typically this is only called for fields that don't have 'autojoin' turned on.
- Any actual conversion of the value should be handled by the `Fieldtype::wakeupValue()` method.

## Usage

~~~~~
// basic usage
$result = $fieldtype->loadPageField($page, $field);

// usage with all arguments
$result = $fieldtype->loadPageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.

## Return value

- `mixed|null`

## Hooking

- Hookable method name: `loadPageField`
- Implementation: `___loadPageField`
- Hook with: `Fieldtype::loadPageField`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::loadPageField', function(HookEvent $event) {
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
$this->addHookAfter('Fieldtype::loadPageField', function(HookEvent $event) {
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
