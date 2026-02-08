# FieldtypeRepeaterPorter

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Export and Import tools for FieldtypeRepeater

## exportConfigData()

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.


@param Field $field

@param array $data

@return array

## importConfigData()

Convert an array of exported data to a format that will be understood internally

This is the opposite of the exportConfigData() method.
Most modules can use the default implementation provided here.


@param Field $field

@param array $data

@var array $errors Errors populated to this array

@return array Data as given and modified as needed. Also included is $data[errors], an associative array
	indexed by property name containing errors that occurred during import of config data.

## exportValue()

Export repeater value

@param Page $page

@param Field $field

@param RepeaterPageArray $value

@param array $options
 - `minimal` (bool): Export a minimal array of just fields and values indexed by repeater page name (default=false)

@return array

## importValue()

Import repeater value previously exported by exportValue()

@param Page $page

@param Field $field

@param array $value

@param array $options

@return bool|PageArray

@throws WireException
