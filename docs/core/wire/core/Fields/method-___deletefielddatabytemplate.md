# $fields->deleteFieldDataByTemplate(Field $field, Template $template): bool

Source: `wire/core/Fields.php`

Physically delete all field data (from the database) used by pages of a given template

This is for internal API use only. This method is intended only to be called by
Fieldtype::deleteTemplateField

If you need to remove a field from a Fieldgroup, use Fieldgroup::remove(), and this
method will be call automatically at the appropriate time when save the fieldgroup.

## Usage

~~~~~
// basic usage
$bool = $fields->deleteFieldDataByTemplate($field, $template);

// usage with all arguments
$bool = $fields->deleteFieldDataByTemplate(Field $field, Template $template);
~~~~~

## Hookable

- Hookable method name: `deleteFieldDataByTemplate`
- Implementation: `___deleteFieldDataByTemplate`
- Hook with: `$fields->deleteFieldDataByTemplate()`

## Hooking Before

~~~~~
$this->addHookBefore('Fields::deleteFieldDataByTemplate', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $template = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
  $event->arguments(1, $template);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fields::deleteFieldDataByTemplate', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $template = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$field` `Field`
- `$template` `Template`

## Return value

- `bool` Whether or not it was successful

## Exceptions

- `WireException` when given a situation where deletion is not allowed
