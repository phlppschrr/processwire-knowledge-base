# $processPageSearchLive->find(array &$liveSearch): array

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

Perform find of types, pages, modules

Result format that this find method expects from modules it calls the search() method from:

$result = array(
  'title' => 'Title of these items, used as the group label except where overridden item "group" property',
  'url' => 'URL to view all items', // if omitted, one will be provided automatically
  'total' => 999, // non-paginated total quantity (can be omitted if pagination not supported)
  'items' => [
    [
     // required properties
    'title' => 'Title of item',
    'url' => 'URL to view or edit the item',
     // optional properties:
    'id' => 0,
    'name' => 'Name of item',
    'icon' => 'Optional icon name to represent the item, i.e. "gear" or "fa-gear"',
    'group' => 'Optionally group with other items having this group name, overrides $result[title]',
    'status' => int, // if item is a Page, status of page using Page::status* constants
    'summary' => 'Summary or description of item or excerpt of text that matched', // (recommended)
    'subtitle' => 'Secondary title of item', // (recommended)
    'modified' => int, // last modified date of item
    ],
    [ ... ], [ ... ], etc.
  )
);

## Arguments

- `$liveSearch` `array`

## Return value

array Array of matches
