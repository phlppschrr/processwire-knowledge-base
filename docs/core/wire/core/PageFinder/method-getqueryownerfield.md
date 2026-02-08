# $pageFinder->getQueryOwnerField($fieldName, array $data): bool

Source: `wire/core/PageFinder.php`

Process an owner back reference selector for PageTable, Page and Repeater fields

## Arguments

- `$fieldName` `string` Field name in "fieldName__owner" format
- `$data` `array` Data as provided to getQueryUnknownField method

## Return value

bool True if $fieldName was processed, false if not

## Throws

- PageFinderSyntaxException
