# $pagesAccess->___updateTemplate(Template $template)

Source: `wire/core/PagesAccess.php`

Update the pages_access table for the given Template

To be called when a `$template->useRoles` property has changed.

## Usage

~~~~~
// basic usage
$result = $pagesAccess->___updateTemplate($template);

// usage with all arguments
$result = $pagesAccess->___updateTemplate(Template $template);
~~~~~

## Arguments

- `$template` `Template`
