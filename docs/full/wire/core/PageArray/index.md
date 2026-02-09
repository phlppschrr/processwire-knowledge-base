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
- [`__construct()`](method-__construct.md)
- [`add(Page|PageArray|int $item): $this`](method-add.md)
- [`getSelectors(bool $getString = false): Selectors|string|null`](method-getselectors.md)
- [`filterData(string|Selectors|array $selectors, bool|int $not = false): PageArray|WireArray`](method-filterdata.md)
- [`getPage(int|string|array $key): Page|NullPage`](method-getpage.md)
- [`findOnePage(string $selector): Page|NullPage`](method-findonepage.md)
- [`getPageByName(string $name): NullPage|Page`](method-getpagebyname.md)
- [`getPageByID(int $id): NullPage|Page`](method-getpagebyid.md)
- [`filterDataSelectors(Selectors $selectors)`](method-filterdataselectors.md)
- [`getItemPropertyValue(Wire $item, string $property): mixed`](method-getitempropertyvalue.md)
- [`__toString()`](method-__tostring.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md)
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md)
