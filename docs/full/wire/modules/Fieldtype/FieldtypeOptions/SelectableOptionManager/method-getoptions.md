# SelectableOptionManager::getOptions()

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Return array of current options for $field

Returned array is indexed by "id$option_id" associative, which is used
as a way to identify existing options vs. new options

@param Field $field

@param array $filters Any of array(property => array) where property is 'id', 'title' or 'value'.

@return SelectableOptionArray|SelectableOption[]

@throws WireException
