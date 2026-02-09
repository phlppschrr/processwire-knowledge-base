# $page->renderField($fieldName, $file = '', $value = null): mixed|string

Source: `wire/core/Page.php`

Render given field using site/templates/fields/ markup file

Shorter aliases of this method include:

- `$page->render('fieldName', $file);`
- `$page->render->fieldName;`
- `$page->_fieldName_;`

This method expects that there is a file in `/site/templates/fields/` to render the field with
one of the following:

- `/site/templates/fields/fieldName.php`
- `/site/templates/fields/fieldName.templateName.php`
- `/site/templates/fields/fieldName/$file.php`
- `/site/templates/fields/$file.php`
- `/site/templates/fields/$file/fieldName.php`
- `/site/templates/fields/$file.fieldName.php`

Note that the examples above showing $file require that the `$file` argument is specified
in the `renderField()` method call.

## Example

~~~~~
// Render output for the 'images' field (assumes you have implemented an output file)
echo $page->renderField('images');
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->renderField($fieldName);

// usage with all arguments
$result = $page->renderField($fieldName, $file = '', $value = null);
~~~~~

## Hookable

- Hookable method name: `renderField`
- Implementation: `___renderField`
- Hook with: `$page->renderField()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::renderField', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);
  $file = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldName);
  $event->arguments(1, $file);
  $event->arguments(2, $value);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::renderField', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $fieldName = $event->arguments(0);
  $file = $event->arguments(1);
  $value = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$fieldName` `string` May be any custom field name or native page property.
- `$file` (optional) `string` Optionally specify file (in site/templates/fields/) to render with (may optionally omit .php extension).
- `$value` (optional) `mixed|null` Optionally specify value to render, otherwise it will be pulled from this page.

## Return value

- `mixed|string` Returns the rendered value of the field

## See Also

- [Page::renderValue()](method-___rendervalue.md)
