# $processPageSearchLive->addResult($group, $title, $url = '', array $data = array()): true

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Add a custom search result

This is used to add search results if you hooked the findCustom() method.
See code example in findCustom() method above.

## Arguments

- `$group` `string` Group name for this search result
- `$title` `string` Title/name of this search result (text that gets clicked on )
- `$url` (optional) `string` URL to this search result
- `$data` (optional) `array` Array of additional data

## Return value

true

## Since

3.0.240
