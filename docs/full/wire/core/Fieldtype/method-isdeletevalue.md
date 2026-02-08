# Fieldtype::isDeleteValue()

Source: `wire/core/Fieldtype.php`

Is given value one that should cause the DB row(s) to be deleted rather than saved?

Not applicable to Fieldtypes that override the savePageField() method with their own
implementation, unless they also use this method.

@param Page $page

@param Field $field

@param mixed $value

@return bool

@since 3.0.150
