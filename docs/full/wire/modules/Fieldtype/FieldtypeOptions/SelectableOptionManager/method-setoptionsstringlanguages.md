# SelectableOptionManager::setOptionsStringLanguages()

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Set options string, but for each language

@param Field $field

@param array $values Array of ($languageID => string), one for each language

@param bool $allowDelete Allow removed lines in the string to result in deleted options?
	If false, no options will be affected but you can call the getRemovedOptionIDs() method
	to retrieve them for confirmation.

@throws WireException
