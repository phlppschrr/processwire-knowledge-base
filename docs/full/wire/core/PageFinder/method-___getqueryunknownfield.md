# PageFinder::___getQueryUnknownField()

Source: `wire/core/PageFinder.php`

Hook called when an unknown field is found in the selector

By default, PW will throw a PageFinderSyntaxException but that behavior can be overridden by
hooking this method and making it return true rather than false. It may also choose to
map it to a Field by returning a Field object. If it returns integer 1 then it indicates the
fieldName mapped to an API variable. If this method returns false, then it signals the getQuery()
method that it was unable to map it to anything and should be considered a fail.

@param string $fieldName

@param array $data Array of data containing the following in it:
 - `subfield` (string): First subfield
 - `subfields` (string): All subfields separated by period (i.e. subfield.tertiaryfield)
 - `fields` (array): Array of all other field names being processed in this selector.
 - `query` (DatabaseQuerySelect): Database query select object
 - `selector` (Selector): Selector that contains this field
 - `selectors` (Selectors): All the selectors

@return bool|Field|int

@throws PageFinderSyntaxException
