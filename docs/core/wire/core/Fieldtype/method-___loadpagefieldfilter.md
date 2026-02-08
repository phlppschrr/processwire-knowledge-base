# Fieldtype::___loadPageFieldFilter()

Source: `wire/core/Fieldtype.php`

Load the given page field from the database table and return a *filtered* value.

This is the same as `Fieldtype::loadPageField()` but enables a selector to be
provided which can filter the returned value.

As far as core Fieldtypes go, this one is only applicable to FieldtypeMulti derived types.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@param Selectors|string|array $selector

@return mixed|null
