# $page->getHelperInstance($className): object|PageComparison|PageAccess|PageTraversal|PageValues

Source: `wire/core/Page.php`

Return a Page helper class instance that’s common among all Page (and derived) objects in this ProcessWire instance

## Usage

~~~~~
// basic usage
$result = $page->getHelperInstance($className);
~~~~~

## Arguments

- `$className` `string`

## Return value

- `object|PageComparison|PageAccess|PageTraversal|PageValues`
