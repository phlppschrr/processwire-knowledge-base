# $fieldtype->deleteTemplateField(Template $template, Field $field): bool

Source: `wire/core/Fieldtype.php`

Delete the given Field from all pages using the given template, without loading those pages.

ProcessWire will use this method rather than deletePageField in cases where the quantity of items
to delete is high (above 200 at time this was written). However, if your individual Fieldtype
defines it's own ___deletePageField method (separate from the one above) then it'll still get used.

This was added so that mass deletions can happen without loading every page, which may not be feasible
when dealing with thousands of pages.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->deleteTemplateField($template, $field);

// usage with all arguments
$bool = $fieldtype->deleteTemplateField(Template $template, Field $field);
~~~~~

## Hookable

- Hookable method name: `deleteTemplateField`
- Implementation: `___deleteTemplateField`
- Hook with: `$fieldtype->deleteTemplateField()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::deleteTemplateField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $template);
  $event->arguments(1, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::deleteTemplateField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $template = $event->arguments(0);
  $field = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$template` `Template`
- `$field` `Field`

## Return value

- `bool`
