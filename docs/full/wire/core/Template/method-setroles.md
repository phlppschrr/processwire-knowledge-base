# $template->setRoles($value, $type = 'view')

Source: `wire/core/Template.php`

Set roles for this template

## Arguments

- array|PageArray $value Role objects or array or Role IDs.
- string $type Specify one of the following: - `view` (default) - `edit` - `create` - `add` - Or a `Permission` object of `page-view` or `page-edit`
