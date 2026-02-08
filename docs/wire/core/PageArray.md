# PageArray

Source: `wire/core/PageArray.php`

ProcessWire PageArray

PageArray provides an array-like means for storing PageReferences and is utilized throughout ProcessWire.

PageArray is a paginated type of WireArray that holds multiple Page objects.
**Please see the `WireArray` and `PaginatedArray` types for available methods**, as they are not
repeated here, except where PageArray has modified or extended those types in some manner.
The PageArray type is functionally identical to WireArray and PaginatedArray except that it is focused
specifically on managing Page objects.

PageArray is returned by all API methods in ProcessWire that can return more than one page at once.
`$pages->find()` and `$page->children()` are common examples that return PageArray.

You can create a new PageArray using any of the methods below:
~~~~~
// the most common way to create a new PageArray and add a $page to it
$a = new PageArray();
$a->add($page);

// ProcessWire 3.0.123+ can also create PageArray like this:
$a = PageArray(); // create blank
$a = PageArray($page); // create + add one page
$a = PageArray([ $page1, $page2, $page3 ]); // create + add pages
~~~~~

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## other

@property Page|null $first First item

@property Page|null $last Last item

## __construct()

Construct

## add()

Add one or more Page objects to this PageArray.

Please see the `WireArray::add()` method for more details.

~~~~~
// Add one page
$pageArray->add($page);

// Add multiple pages
$pageArray->add($pages->find("template=basic-page"));

// Add page by ID
$pageArray->add(1005);
~~~~~

@param Page|PageArray|int $item Page object, PageArray object, or Page ID.
 - If given a `Page`, the Page will be added.
 - If given a `PageArray`, it will do the same thing as the `WireArray::import()` method and append all the pages.
 - If Page `ID`, the Page identified by that ID will be loaded and added to the PageArray.

@return $this

## getSelectors()

Return the Selectors that led to this PageArray, or null if not set/applicable.

Use this to retrieve the Selectors that were used to find this group of pages,
if dealing with a PageArray that originated from a database operation.

~~~~~
$products = $pages->find("template=product, featured=1, sort=-modified, limit=10");
echo $products->getSelectors(); // outputs the selector above
~~~~~

@param bool $getString Specify true to get selector string rather than Selectors object (default=false) added in 3.0.142

@return Selectors|string|null Returns Selectors object if available, or null if not. Always return string if $getString argument is true.

## filterData()

Filter out Pages that don't match the selector.

This is applicable to and destructive to the WireArray.

@param string|Selectors|array $selectors Selector string to use as the filter.

@param bool|int $not Make this a "not" filter? Use int 1 for "not all". (default is false)

@return PageArray|WireArray reference to current [filtered] PageArray

## getPage()

Like the base get() method but can only return Page objects (whether Page or NullPage)

@param int|string|array $key Provide any of the following:
 - Key of Page to retrieve.
 - A selector string or selector array, to return the first item that matches the selector.
 - A string containing the "name" property of any Page, and the matching Page will be returned.

@return Page|NullPage

@since 3.0.162

@see WireArray::get()

## findOnePage()

Same as find() or findOne() methods, but always returns a Page (whether Page or NullPage)

@param string $selector

@return Page|NullPage

@since 3.0.162

## getPageByName()

Get Page from this PageArray having given name, or return NullPage if not present

@param string $name

@return NullPage|Page

@since 3.0.162

## getPageByID()

Get Page from this PageArray having given ID, or return NullPage if not present

@param int $id

@return NullPage|Page

@since 3.0.162

## filterDataSelectors()

Prepare selectors for filtering

Template method for descending classes to modify selectors if needed

@param Selectors $selectors

## getItemPropertyValue()

Get the value of $property from $item

Used by the WireArray::sort method to retrieve a value from a Wire object.
If output formatting is on, we turn it off to ensure that the sorting
is performed without output formatting.

@param Wire $item

@param string $property

@return mixed

## __toString()

PageArrays always return a string of the Page IDs separated by pipe "|" characters

Pipe charactesr are used for compatibility with Selector OR statements

## __debugInfo()

debugInfo PHP 5.6+ magic method

@return array

## trackAdd()

Track an item added

@param Wire|mixed $item

@param int|string $key

## trackRemove()

Track an item removed

@param Wire|mixed $item

@param int|string $key
