# $processPageListActions->___getActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListActions->___getActions($page);

// usage with all arguments
$array = $processPageListActions->___getActions(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url
