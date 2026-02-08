# $pageFinder->getQueryOwnerField($fieldName, array $data): bool

Source: `wire/core/PageFinder.php`

Process an owner back reference selector for PageTable, Page and Repeater fields

## Usage

~~~~~
// basic usage
$bool = $pageFinder->getQueryOwnerField($fieldName, $data);

// usage with all arguments
$bool = $pageFinder->getQueryOwnerField($fieldName, array $data);
~~~~~

## Arguments

- `$fieldName` `string` Field name in "fieldName__owner" format
- `$data` `array` Data as provided to getQueryUnknownField method

## Return value

- `bool` True if $fieldName was processed, false if not

## Exceptions

- `PageFinderSyntaxException`
