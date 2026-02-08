# Template::hasRole()

Source: `wire/core/Template.php`

Does this template have the given Role?


@param string|Role|Page $role Name of Role or Role object.

@param string|Permission Specify one of the following:
 - `view` (default)
 - `edit`
 - `create`
 - `add`
 - Or a `Permission` object of `page-view` or `page-edit`

@return bool True if template has the role, false if not
