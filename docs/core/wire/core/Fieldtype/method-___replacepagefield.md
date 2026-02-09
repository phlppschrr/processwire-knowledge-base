# $fieldtype->replacePageField(Page $src, Page $dst, Field $field): bool

Source: `wire/core/Fieldtype.php`

Move this field’s data from one page to another.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->replacePageField($src, $dst, $field);

// usage with all arguments
$bool = $fieldtype->replacePageField(Page $src, Page $dst, Field $field);
~~~~~

## Hookable

- Hookable method name: `replacePageField`
- Implementation: `___replacePageField`
- Hook with: `$fieldtype->replacePageField()`

## Hooking Before

~~~~~
$this->addHookBefore('Fieldtype::replacePageField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $src = $event->arguments(0);
  $dst = $event->arguments(1);
  $field = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $src);
  $event->arguments(1, $dst);
  $event->arguments(2, $field);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fieldtype::replacePageField', function(HookEvent $event) {
  $fieldtype = $event->object;

  // Get arguments
  $src = $event->arguments(0);
  $dst = $event->arguments(1);
  $field = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$src` `Page` Source Page
- `$dst` `Page` Destination Page
- `$field` `Field`

## Return value

- `bool`
