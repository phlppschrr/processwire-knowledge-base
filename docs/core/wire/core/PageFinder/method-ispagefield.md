# PageFinder::isPageField()

Source: `wire/core/PageFinder.php`

Does the given field or fieldName resolve to a field that uses Page or PageArray values?

@param string|Field $fieldName Field name or object

@param bool $literal Specify true to only allow types that literally use FieldtypePage::getMatchQuery()

@return Field|bool|string Returns Field object or boolean true (children|parent) if valid Page field, or boolean false if not
