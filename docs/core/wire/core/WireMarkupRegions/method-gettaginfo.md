# $wireMarkupRegions->getTagInfo($tag): array

Source: `wire/core/WireMarkupRegions.php`

Given HTML tag like “<div id='foo' class='bar baz'>” return associative array of info about it

Returned info includes:
 - `name` (string): Tag name
 - `id` (string): Value of id attribute
 - `pwid` (string): PW region ID from 'pw-id' or 'data-pw-id', or if not present, then same as 'id'
 - `action` (string): Action for this region, without “pw-” prefix.
 - `actionTarget` (string): Target id for the action, if applicable.
 - `actionType` (string): "class" if action specified as class name, "attr" if specified as a pw- or data-pw attribute.
 - `classes` (array): Array of class names (from class attribute).
 - `attrs` (array): Associative array of all attributes, all values are strings.
 - `attrStr` (string): All attributes in a string
 - `tag` (string): The entire tag as given
 - `close` (string): The HTML string that would close this tag

## Arguments

- string $tag Must be a tag in format “<tag attrs>”

## Return value

array
