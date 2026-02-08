# $pagesEditor->add($template, $parent, $name = '', array $values = array()): Page

Source: `wire/core/PagesEditor.php`

Add a new page using the given template to the given parent

If no name is specified one will be assigned based on the current timestamp.

## Arguments

- string|Template $template Template name or Template object
- string|int|Page $parent Parent path, ID or Page object
- string $name Optional name or title of page. If none provided, one will be automatically assigned based on microtime stamp. If you want to specify a different name and title then specify the $name argument, and $values['title'].
- array $values Field values to assign to page (optional). If $name is omitted, this may also be 3rd param.

## Return value

Page Returned page has output formatting off.

## Throws

- WireException When some criteria prevents the page from being saved.
