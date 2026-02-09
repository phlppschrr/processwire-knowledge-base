# $template->hasRole($role, $type = 'view'): bool

Source: `wire/core/Template.php`

Does this template have the given Role?

## Usage

~~~~~
// basic usage
$bool = $template->hasRole($role);

// usage with all arguments
$bool = $template->hasRole($role, $type = 'view');
~~~~~

## Arguments

- `$role` `string|Role|Page` Name of Role or Role object.
- string|Permission Specify one of the following: - `view` (default) - `edit` - `create` - `add` - Or a `Permission` object of `page-view` or `page-edit`

## Return value

- `bool` True if template has the role, false if not
