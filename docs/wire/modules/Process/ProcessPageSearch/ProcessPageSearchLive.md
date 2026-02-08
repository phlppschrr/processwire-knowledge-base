# ProcessPageSearchLive

Source: `wire/modules/Process/ProcessPageSearch/ProcessPageSearchLive.php`

ProcessPageSearch: Live Search (for PW admin)


@todo support searching repeaters

## other

@method renderList(array $items, $prefix = 'pw-search', $class = 'list')

@method renderItem(array $item, $prefix = 'pw-search', $class = 'list')

@method string|array execute($getJSON = true)

@method bool findCustom(array $data)

@method array getDefaultPageSearchFields()

## __construct()

Construct

@param ProcessPageSearch|null $process

@param array $liveSearch

## setSearchTypesOrder()

Set order of search types

@param array $types Names of types, in order

## setNoSearchTypes()

Set types that should be excluded unless specifically asked for

@param array $types Names of types to exclude

## setDefaultOperators()

Set default operators to use for searches (if query does not specify operator)

@param string $singleWordOperator

@param string $multiWordOperator

## init()

Initialize live search

@param array $presets Additional info to populate in liveSearchInfo

@return array Current liveSearchInfo

## ___execute()

Execute live search and return JSON result

@param bool $getJSON Get results as JSON string? Specify false to get array instead.

@return string|array

## executeViewAll()

Render output for landing page to view all items of a particular type

Expects these GET vars to be present:
 - type
 - operator
 - property
 - q

@return string

@throws WireException

## find()

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

@param array $liveSearch

@return array Array of matches

## findPages()

Find pages for live search

@param array $liveSearch

@return array

## useType()

Allow this search type?

@param string $type Type to check

@param string $requestType Type specifically requested by user

@return bool

## findModules()

Find modules matching query

@param array $liveSearch

@param array $modulesInfo

@return array

## convertItemsFormat()

Convert items from native live search format (v2) to v1 format

v1 format is used by ProcessWire admin themes.

@param array $items

@return array

## makeDebugItem()

Make a search result item that displays debugging info

@param array $liveSearch

@return array

## makeHelpItems()

Make a search result item that displays property info

@param array $result Result array returned by a SearchableModule::search() method

@param string $type

@return array

## makeViewAllItem()

Make a search result item that displays a “view all” link

@param array $liveSearch

@param string $type

@param string $group

@param int $total

@param string $url If module provides its own view-all URL

@return array

## ___renderList()

Render “view all” list

@param array $items

@param string $prefix For CSS classes, default is "pw-search"

@param string $class Class name for list, default is "list" which translates to "pw-search-list"

@return string HTML markup

## ___renderItem()

Render an item for the “view all” list

@param array $item

@param string $prefix For CSS classes, default is "pw-search"

@param string $class Class name for item, default is "item" which translates to "pw-search-item"

@return string HTML markup

## ___findCustom()

Hookable method to find custom search results

~~~~
// handle a search of "today" to find pages modified today
$wire->addHook('ProcessPageSearchLive::findCustom', function(HookEvent $event) {
  $data = $event->arguments(0); // array
  $search = $event->object; // ProcesPageSearchLive
  if($data['q'] === 'today') {
    $items = $event->wire()->pages->find("modified>=today, include=unpublished");
    foreach($items as $item) {
       $search->addSearchResult('Pages modified today', $item->title, $item->editUrl);
    }
  }
});
~~~~


@param array $data Data about the search including 'type', 'operator', 'q' (query) and more.

@return bool Optionally return false to stop search, making it use only results returned by this method.

@since 3.0.240

## addResult()

Add a custom search result

This is used to add search results if you hooked the findCustom() method.
See code example in findCustom() method above.


@param string $group Group name for this search result

@param string $title Title/name of this search result (text that gets clicked on )

@param string $url URL to this search result

@param array $data Array of additional data

@since 3.0.240

@return true

## addResults()

Add multiple results at once


@param string $group Group name for these search results

@param array $results Associative array where keys are URLs and values are titles/labels

@since 3.0.240

@return true

## addHelp()

Add help examples for when the help results are displayed

~~~~~
// handle a search of "today" to find pages modified today
$wire->addHook('ProcessPageSearchLive::findCustom', function(HookEvent $event) {
  $data = $event->arguments(0); // array
  $search = $event->object; // ProcesPageSearchLive
  if($data['help']) {
    return $search->addHelp('ID Search Help', [
      // example => description
      'today' => 'Finds pages that have been modified today',
    ]);
  }
  // ...
});
~~~~~


@param string $group Group name for these search results

@param array $examples Examples where keys are example queries and values are descriptions

@return true

@since 3.0.240

## ___getDefaultPageSearchFields()

Get the names of fields that should be used when searching pages

Hook this from /site/templates/admin.php to modify what gets searched.
This overrides the setting specified interactively in the ProcessPageSearch module settings.

~~~~~
$wire->addHookAfter('ProcessPageSearchLive::getDefaultPageSearchFields', function(HookEvent $e) {
  $e->return = [ 'title', 'subtitle', 'categories.title' ];
});
~~~~~


@return array

@since 3.0.242
