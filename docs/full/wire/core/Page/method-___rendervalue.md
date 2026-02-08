# Page::___renderValue()

Source: `wire/core/Page.php`

Render given value using /site/templates/fields/ markup file

See the documentation for the `Page::renderField()` method for information about the `$file` argument.

~~~~~
// Render a value using site/templates/fields/my-images.php custom output template
$images = $page->images;
echo $page->renderValue($images, 'my-images');
~~~~~


@param mixed $value Value to render

@param string $file Optionally specify file (in site/templates/fields/) to render with (may omit .php extension)

@return mixed|string Returns rendered value
