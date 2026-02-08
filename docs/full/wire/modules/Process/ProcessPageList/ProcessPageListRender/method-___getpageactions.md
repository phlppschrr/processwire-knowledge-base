# $processPageListRender->getPageActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListRender->getPageActions($page);

// usage with all arguments
$array = $processPageListRender->getPageActions(Page $page);
~~~~~

## Hookable

- Hookable method name: `getPageActions`
- Implementation: `___getPageActions`
- Hook with: `$processPageListRender->getPageActions()`

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url
