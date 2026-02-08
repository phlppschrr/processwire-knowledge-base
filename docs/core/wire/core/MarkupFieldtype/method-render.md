# $markupFieldtype->render($property = ''): string

Source: `wire/core/MarkupFieldtype.php`

Render markup for the field or for the property from field

## Usage

~~~~~
// basic usage
$string = $markupFieldtype->render();

// usage with all arguments
$string = $markupFieldtype->render($property = '');
~~~~~

## Arguments

- `$property` (optional) `string` Optional property (for object or array field values)

## Return value

- `string`
