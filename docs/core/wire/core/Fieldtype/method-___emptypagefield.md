# Fieldtype::___emptyPageField()

Source: `wire/core/Fieldtype.php`

Empty out the DB table data for page field, but leave everything else in tact.

In most cases this may be nearly identical to `Fieldtype::deletePageField()`, but would be different
for things like page references where we wouldn't want relational data deleted.


@param Page $page

@param Field $field Field object

@return bool True on success, false on DB delete failure.

@throws WireException
