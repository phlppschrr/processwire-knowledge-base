# $pagesAccess->updateTemplate(Template $template)

Source: `wire/core/PagesAccess.php`

Update the pages_access table for the given Template

To be called when a `$template->useRoles` property has changed.

## Usage

~~~~~
// basic usage
$result = $pagesAccess->updateTemplate($template);

// usage with all arguments
$result = $pagesAccess->updateTemplate(Template $template);
~~~~~

## Hookable

- Hookable method name: `updateTemplate`
- Implementation: `___updateTemplate`
- Hook with: `$pagesAccess->updateTemplate()`

## Arguments

- `$template` `Template`
