# $processPageListActions->processAction(Page $page, $action): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Process action

## Usage

~~~~~
// basic usage
$array = $processPageListActions->processAction($page, $action);

// usage with all arguments
$array = $processPageListActions->processAction(Page $page, $action);
~~~~~

## Hookable

- Hookable method name: `processAction`
- Implementation: `___processAction`
- Hook with: `$processPageListActions->processAction()`

## Arguments

- `$page` `Page`
- `$action` `string`

## Return value

- `array`

## Exceptions

- `WireException`
