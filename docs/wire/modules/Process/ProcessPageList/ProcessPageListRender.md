# ProcessPageListRender

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Base class for Page List rendering

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method array getPageActions(Page $page)

@method string getPageLabel(Page $page, array $options = array())

@method int getNumChildren(Page $page, $selector = null) For hooks only, do not call directly

## __construct()

Construct

@param Page $page

@param PageArray $children

## wired()

Wired to ProcessWire instance

## setOption()

Set option

@param string $key

@param mixed $value

@return $this

## getOption()

Get option

@param string $key

@return mixed|null

## setStart()

Set pagination start

@param int $n

## setLimit()

Set pagination limit

@param int $n

## setLabel()

Set action label by name

@param string $key

@param string $value

## setUseTrash()

Set whether to use trash

@param bool $useTrash

## setPageLabelField()

Set the default page label field/format

@param string $pageLabelField

## setHidePages()

Set when pages should be hidden in page list

@param array $hidePages IDs of pages that should be hidden

@param array $hidePagesNot Do not hide pages when state matches one or more of 'debug', 'advanced', 'superuser'

## setQtyType()

Set the quantity type

@param string $qtyType

## actions()

Get the ProcessPageListActions instance

@return null|ProcessPageListActions

## ___getPageActions()

Get an array of available Page actions, indexed by $label => $url

@param Page $page

@return array of $label => $url

## ___getPageLabel()

Return the Page's label text, whether that originates from the Page's name, headline, title, etc.

@param Page $page

@param array $options
 - `noTags` (bool): If true, HTML will be excluded [other than for icon] in returned text value (default=false)
 - `noIcon` (bool): If true, icon markup will be excluded from returned value (default=false)

@return string

## getPageLabelIconMarkup()

Get page label icon and modify $label to remove existing icon references

@param Page $page

@param string $label

@return string

@since 3.0.163

## getPageLabelDelimited()

Get page label when label format is space delimited

@param Page $page

@param string $label

@param array $options

@return string

@since 3.0.163

## renderChild()

Render child item in page list

@param Page $page

@return array

## render()

Render page list

@return string|array

## getRenderName()

Get the name of this renderer (i.e. 'JSON')

@return string

## getMoreURL()

Get URL to view more

@return string

## getChildren()

Get children pages

@return PageArray

## getUseTrash()

Get whether or not to use trash

@return bool

## ___getNumChildren()

Hook this method if you want to manipulate the numChildren count for pages

~~~~~
$wire->addHookAfter('ProcessPageListRender::getNumChildren', function($event) {
  $page = $event->arguments(0);
  $selector = $event->arguments(1);
  $event->return = $page->numChildren($selector); // your implementation here
});
~~~~~

See Page::numChildren() for details on arguments


@param Page $page

@param string|int|bool|null $selector

@return int

## numChildren()

Return number of children for page

@param Page $page

@param string|int|bool|null $selector

@return int
