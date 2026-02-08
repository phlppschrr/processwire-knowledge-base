# $processPageListActions->getActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListActions->getActions($page);

// usage with all arguments
$array = $processPageListActions->getActions(Page $page);
~~~~~

## Hookable

- Hookable method name: `getActions`
- Implementation: `___getActions`
- Hook with: `$processPageListActions->getActions()`

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url
