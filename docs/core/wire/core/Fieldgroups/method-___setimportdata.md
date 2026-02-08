# Fieldgroups::___setImportData()

Source: `wire/core/Fieldgroups.php`

Given an export data array, import it back to the class and return what happened

Changes are not committed until the item is saved

@param Fieldgroup $fieldgroup

@param array $data

@return array Returns array(
	[property_name] => array(
		'old' => 'old value',	// old value, always a string
		'new' => 'new value',	// new value, always a string
		'error' => 'error message or blank if no error'
	)

@throws WireException if given invalid data
