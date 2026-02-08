# $processPageListRender->___getPageLabel(Page $page, array $options = array()): string

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Return the Page's label text, whether that originates from the Page's name, headline, title, etc.

## Usage

~~~~~
// basic usage
$string = $processPageListRender->___getPageLabel($page);

// usage with all arguments
$string = $processPageListRender->___getPageLabel(Page $page, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `noTags` (bool): If true, HTML will be excluded [other than for icon] in returned text value (default=false) - `noIcon` (bool): If true, icon markup will be excluded from returned value (default=false)

## Return value

- `string`
