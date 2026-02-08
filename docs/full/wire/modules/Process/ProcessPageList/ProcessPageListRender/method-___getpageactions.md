# $processPageListRender->___getPageActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListRender->___getPageActions($page);

// usage with all arguments
$array = $processPageListRender->___getPageActions(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url
