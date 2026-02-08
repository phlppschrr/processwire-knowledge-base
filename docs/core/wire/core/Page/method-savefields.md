# Page::saveFields()

Source: `wire/core/Page.php`

Save only the given named fields for this page

@param array|string $fields Array of field name(s) or string (CSV or space separated)

@param array $options See Pages::save() documentation for options.

@return array Names of fields that were saved

@throws WireException on database error

@see Page::save()

@since 3.0.242
