# FieldtypeRepeaterPorter::importConfigData()

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Convert an array of exported data to a format that will be understood internally

This is the opposite of the exportConfigData() method.
Most modules can use the default implementation provided here.


@param Field $field

@param array $data

@var array $errors Errors populated to this array

@return array Data as given and modified as needed. Also included is $data[errors], an associative array
	indexed by property name containing errors that occurred during import of config data.
