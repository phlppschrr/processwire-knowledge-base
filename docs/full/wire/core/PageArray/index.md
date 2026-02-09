# PageArray

Source: `wire/core/PageArray.php`

Inherits: `PaginatedArray`
Implements: `WirePaginatable`


Groups:
Group: [other](group-other.md)

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

Methods:
Method: [__construct()](method-__construct.md)
Method: [add()](method-add.md)
Method: [getSelectors()](method-getselectors.md)
Method: [filterData()](method-filterdata.md)
Method: [getPage()](method-getpage.md)
Method: [findOnePage()](method-findonepage.md)
Method: [getPageByName()](method-getpagebyname.md)
Method: [getPageByID()](method-getpagebyid.md)
Method: [filterDataSelectors()](method-filterdataselectors.md)
Method: [getItemPropertyValue()](method-getitempropertyvalue.md)
Method: [__toString()](method-__tostring.md)
Method: [__debugInfo()](method-__debuginfo.md)
Method: [trackAdd()](method-trackadd.md)
Method: [trackRemove()](method-trackremove.md)
