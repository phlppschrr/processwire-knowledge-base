# Fields::___deleteFieldDataByTemplate()

Source: `wire/core/Fields.php`

Physically delete all field data (from the database) used by pages of a given template

This is for internal API use only. This method is intended only to be called by
Fieldtype::deleteTemplateField

If you need to remove a field from a Fieldgroup, use Fieldgroup::remove(), and this
method will be call automatically at the appropriate time when save the fieldgroup.


@param Field $field

@param Template $template

@return bool Whether or not it was successful

@throws WireException when given a situation where deletion is not allowed
