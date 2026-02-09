# $fieldtype->loadPageFieldFilter(Page $page, Field $field, $selector): mixed|null

Source: `wire/core/Fieldtype.php`

Load the given page field from the database table and return a *filtered* value.

This is the same as `Fieldtype::loadPageField()` but enables a selector to be
provided which can filter the returned value.

As far as core Fieldtypes go, this one is only applicable to FieldtypeMulti derived types.

## Usage

~~~~~
// basic usage
$result = $fieldtype->loadPageFieldFilter($page, $field, $selector);

// usage with all arguments
$result = $fieldtype->loadPageFieldFilter(Page $page, Field $field, $selector);
~~~~~

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.
- `$selector` `Selectors|string|array`

## Return value

- `mixed|null`

## Hooking

- Hookable method name: `loadPageFieldFilter`
- Implementation: `___loadPageFieldFilter`
- Hook with: `Fieldtype::loadPageFieldFilter`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::loadPageFieldFilter', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $selector = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $field);
  $event->arguments(2, $selector);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldtype::loadPageFieldFilter', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $field = $event->arguments(1);
  $selector = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
