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
- [`__construct()`](method-__construct.md) Construct
- [`add(Page|PageArray|int $item): $this`](method-add.md) Add one or more Page objects to this PageArray.
- [`getSelectors(bool $getString = false): Selectors|string|null`](method-getselectors.md) Return the Selectors that led to this PageArray, or null if not set/applicable.
- [`filterData(string|Selectors|array $selectors, bool|int $not = false): PageArray|WireArray`](method-filterdata.md) Filter out Pages that don't match the selector.
- [`getPage(int|string|array $key): Page|NullPage`](method-getpage.md) Like the base get() method but can only return Page objects (whether Page or NullPage)
- [`findOnePage(string $selector): Page|NullPage`](method-findonepage.md) Same as find() or findOne() methods, but always returns a Page (whether Page or NullPage)
- [`getPageByName(string $name): NullPage|Page`](method-getpagebyname.md) Get Page from this PageArray having given name, or return NullPage if not present
- [`getPageByID(int $id): NullPage|Page`](method-getpagebyid.md) Get Page from this PageArray having given ID, or return NullPage if not present
- [`filterDataSelectors(Selectors $selectors)`](method-filterdataselectors.md) Prepare selectors for filtering
- [`getItemPropertyValue(Wire $item, string $property): mixed`](method-getitempropertyvalue.md) Get the value of $property from $item
- [`__toString()`](method-__tostring.md) PageArrays always return a string of the Page IDs separated by pipe "|" characters
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md) Track an item added
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md) Track an item removed
