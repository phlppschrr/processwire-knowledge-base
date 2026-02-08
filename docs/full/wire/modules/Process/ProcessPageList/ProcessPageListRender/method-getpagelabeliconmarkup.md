# $processPageListRender->getPageLabelIconMarkup(Page $page, &$label): string

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Get page label icon and modify $label to remove existing icon references

## Usage

~~~~~
// basic usage
$string = $processPageListRender->getPageLabelIconMarkup($page, $label);

// usage with all arguments
$string = $processPageListRender->getPageLabelIconMarkup(Page $page, &$label);
~~~~~

## Arguments

- `$page` `Page`
- `$label` `string`

## Return value

- `string`

## Since

3.0.163
