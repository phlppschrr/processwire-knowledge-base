# $template->getRoles($type = 'view'): PageArray

Source: `wire/core/Template.php`

Get the role pages that are part of this template

- This method returns a blank PageArray if roles haven’t yet been loaded into the template.
- If the roles have previously been loaded as an array, then this method converts that array
  to a PageArray and returns it.
- If you make changes to returned roles, make sure to set it back to the template again with setRoles().
  It’s preferable to make changes with addRole() and removeRole() methods instead.

## Usage

~~~~~
// basic usage
$items = $template->getRoles();

// usage with all arguments
$items = $template->getRoles($type = 'view');
~~~~~

## Arguments

- `$type` (optional) `string` Default is 'view', but you may also specify 'edit', 'create' or 'add' to retrieve those.

## Return value

- `PageArray` of Role objects.

## Exceptions

- `WireException` if given an unknown roles type
