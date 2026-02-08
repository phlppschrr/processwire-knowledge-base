# Page::getAccessParent()

Source: `wire/core/Page.php`

Returns the page from which role/access settings are inherited from


@param string $type Optionally specify one of 'view', 'edit', 'add', or 'create' (default='view')

@return Page|NullPage Returns NullPage if none found
