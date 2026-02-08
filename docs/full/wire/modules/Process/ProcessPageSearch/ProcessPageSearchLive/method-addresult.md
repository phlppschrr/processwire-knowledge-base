# ProcessPageSearchLive::addResult()

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Add a custom search result

This is used to add search results if you hooked the findCustom() method.
See code example in findCustom() method above.


@param string $group Group name for this search result

@param string $title Title/name of this search result (text that gets clicked on )

@param string $url URL to this search result

@param array $data Array of additional data

@since 3.0.240

@return true
