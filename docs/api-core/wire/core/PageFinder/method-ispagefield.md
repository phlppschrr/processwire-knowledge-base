# $pageFinder->isPageField($fieldName, $literal = false): Field|bool|string

Source: `wire/core/PageFinder.php`

Does the given field or fieldName resolve to a field that uses Page or PageArray values?

## Usage

~~~~~
// basic usage
$field = $pageFinder->isPageField($fieldName);

// usage with all arguments
$field = $pageFinder->isPageField($fieldName, $literal = false);
~~~~~

## Arguments

- `$fieldName` `string|Field` Field name or object
- `$literal` (optional) `bool` Specify true to only allow types that literally use FieldtypePage::getMatchQuery()

## Return value

- `Field|bool|string` Returns Field object or boolean true (children|parent) if valid Page field, or boolean false if not
