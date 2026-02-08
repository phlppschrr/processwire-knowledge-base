# $processPageSearchLive->addResult($group, $title, $url = '', array $data = array()): true

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Add a custom search result

This is used to add search results if you hooked the findCustom() method.
See code example in findCustom() method above.

## Arguments

- string $group Group name for this search result
- string $title Title/name of this search result (text that gets clicked on )
- string $url URL to this search result
- array $data Array of additional data

## Return value

true

## Meta

- @since 3.0.240
