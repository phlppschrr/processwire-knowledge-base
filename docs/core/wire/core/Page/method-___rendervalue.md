# $page->renderValue($value, $file = ''): mixed|string

Source: `wire/core/Page.php`

Render given value using /site/templates/fields/ markup file

See the documentation for the `Page::renderField()` method for information about the `$file` argument.

## Example

~~~~~
// Render a value using site/templates/fields/my-images.php custom output template
$images = $page->images;
echo $page->renderValue($images, 'my-images');
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->renderValue($value);

// usage with all arguments
$result = $page->renderValue($value, $file = '');
~~~~~

## Hookable

- Hookable method name: `renderValue`
- Implementation: `___renderValue`
- Hook with: `$page->renderValue()`

## Arguments

- `$value` `mixed` Value to render
- `$file` (optional) `string` Optionally specify file (in site/templates/fields/) to render with (may omit .php extension)

## Return value

- `mixed|string` Returns rendered value
