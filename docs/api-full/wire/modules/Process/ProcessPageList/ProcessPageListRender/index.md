# ProcessPageListRender

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Inherits: `Wire`

## Summary

Base class for Page List rendering

Common methods:
- [`wired()`](method-wired.md)
- [`setOption()`](method-setoption.md)
- [`getOption()`](method-getoption.md)
- [`setStart()`](method-setstart.md)
- [`setLimit()`](method-setlimit.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`__construct(Page $page, PageArray $children)`](method-__construct.md) Construct
- [`wired()`](method-wired.md) Wired to ProcessWire instance
- [`setOption(string $key, mixed $value): $this`](method-setoption.md) Set option
- [`getOption(string $key): mixed|null`](method-getoption.md) Get option
- [`setStart(int $n)`](method-setstart.md) Set pagination start
- [`setLimit(int $n)`](method-setlimit.md) Set pagination limit
- [`setLabel(string $key, string $value)`](method-setlabel.md) Set action label by name
- [`setUseTrash(bool $useTrash)`](method-setusetrash.md) Set whether to use trash
- [`setPageLabelField(string $pageLabelField)`](method-setpagelabelfield.md) Set the default page label field/format
- [`setHidePages(array $hidePages, array $hidePagesNot)`](method-sethidepages.md) Set when pages should be hidden in page list
- [`setQtyType(string $qtyType)`](method-setqtytype.md) Set the quantity type
- [`actions(): null|ProcessPageListActions`](method-actions.md) Get the ProcessPageListActions instance
- [`getPageActions(Page $page): array`](method-___getpageactions.md) (hookable) Get an array of available Page actions, indexed by $label => $url
- [`getPageLabel(Page $page, array $options = array()): string`](method-___getpagelabel.md) (hookable) Return the Page's label text, whether that originates from the Page's name, headline, title, etc.
- [`getPageLabelIconMarkup(Page $page, string &$label): string`](method-getpagelabeliconmarkup.md) Get page label icon and modify $label to remove existing icon references
- [`getPageLabelDelimited(Page $page, string $label, array $options): string`](method-getpagelabeldelimited.md) Get page label when label format is space delimited
- [`renderChild(Page $page): array`](method-renderchild.md) Render child item in page list
- [`render(): string|array`](method-render.md) Render page list
- [`getRenderName(): string`](method-getrendername.md) Get the name of this renderer (i.e. 'JSON')
- [`getMoreURL(): string`](method-getmoreurl.md) Get URL to view more
- [`getChildren(): PageArray`](method-getchildren.md) Get children pages
- [`getUseTrash(): bool`](method-getusetrash.md) Get whether or not to use trash
- [`getNumChildren(Page $page, string|int|bool|null $selector = null): int`](method-___getnumchildren.md) (hookable) Hook this method if you want to manipulate the numChildren count for pages
- [`numChildren(Page $page, string|int|bool|null $selector = null): int`](method-numchildren.md) Return number of children for page
