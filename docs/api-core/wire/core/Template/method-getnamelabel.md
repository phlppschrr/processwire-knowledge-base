# $template->getNameLabel($language = null): string

Source: `wire/core/Template.php`

Return the overriden "page name" label, or blank if not overridden

## Usage

~~~~~
// basic usage
$string = $template->getNameLabel();

// usage with all arguments
$string = $template->getNameLabel($language = null);
~~~~~

## Arguments

- `$language` (optional) `Language|null`

## Return value

- `string`
