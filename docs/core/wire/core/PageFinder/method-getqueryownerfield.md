# PageFinder::getQueryOwnerField()

Source: `wire/core/PageFinder.php`

Process an owner back reference selector for PageTable, Page and Repeater fields

@param string $fieldName Field name in "fieldName__owner" format

@param array $data Data as provided to getQueryUnknownField method

@return bool True if $fieldName was processed, false if not

@throws PageFinderSyntaxException
