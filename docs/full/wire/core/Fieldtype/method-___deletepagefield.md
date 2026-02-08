# Fieldtype::___deletePageField()

Source: `wire/core/Fieldtype.php`

Delete the given Field from the given Page.

Must delete entries from field's database table that belong to the Page.


@param Page $page

@param Field $field Field object

@return bool True on success, false on DB delete failure.

@throws WireException
