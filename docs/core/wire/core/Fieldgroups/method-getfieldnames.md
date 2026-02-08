# Fieldgroups::getFieldNames()

Source: `wire/core/Fieldgroups.php`

Get all field names used by given fieldgroup

Use this when you want to identify the field names (or IDs) without loading the fieldgroup or fields in it.

@param string|int|Fieldgroup $fieldgroup Fieldgroup name, ID or object

@return array Returned array of field names indexed by field ID

@since 3.0.194
