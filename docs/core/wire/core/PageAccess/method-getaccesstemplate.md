# PageAccess::getAccessTemplate()

Source: `wire/core/PageAccess.php`

Returns the template from which we get our role/access settings from

@param Page $page

@param string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')

@return Template|null Returns null if none
