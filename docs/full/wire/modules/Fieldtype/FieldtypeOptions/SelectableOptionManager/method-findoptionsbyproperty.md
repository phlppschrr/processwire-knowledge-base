# SelectableOptionManager::findOptionsByProperty()

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Perform a partial match on title of options

@param Field $field

@param string $property Either 'title' or 'value'. May also be blank (to imply 'either') if operator is '=' or
    '!='

@param string $operator

@param string $value Value to find

@return SelectableOptionArray
