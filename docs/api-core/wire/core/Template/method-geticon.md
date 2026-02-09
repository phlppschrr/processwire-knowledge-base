# $template->getIcon($prefix = false): string

Source: `wire/core/Template.php`

Return the icon name used by this template

## Usage

~~~~~
// basic usage
$string = $template->getIcon();

// usage with all arguments
$string = $template->getIcon($prefix = false);
~~~~~

## Arguments

- `$prefix` (optional) `bool` Specify true if you want the icon prefix (icon- or fa-) to be included (default=false).

## Return value

- `string` Returns a font-awesome icon name
