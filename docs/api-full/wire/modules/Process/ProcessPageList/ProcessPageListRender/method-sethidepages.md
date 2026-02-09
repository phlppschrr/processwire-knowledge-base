# $processPageListRender->setHidePages($hidePages, $hidePagesNot)

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Set when pages should be hidden in page list

## Usage

~~~~~
// basic usage
$result = $processPageListRender->setHidePages($hidePages, $hidePagesNot);
~~~~~

## Arguments

- `$hidePages` `array` IDs of pages that should be hidden
- `$hidePagesNot` `array` Do not hide pages when state matches one or more of 'debug', 'advanced', 'superuser'
