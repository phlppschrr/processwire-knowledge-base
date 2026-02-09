# ProcessPageListRender

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Base class for Page List rendering

Methods:
- [`__construct(Page $page, PageArray $children)`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`setOption(string $key, mixed $value): $this`](method-setoption.md)
- [`getOption(string $key): mixed|null`](method-getoption.md)
- [`setStart(int $n)`](method-setstart.md)
- [`setLimit(int $n)`](method-setlimit.md)
- [`setLabel(string $key, string $value)`](method-setlabel.md)
- [`setUseTrash(bool $useTrash)`](method-setusetrash.md)
- [`setPageLabelField(string $pageLabelField)`](method-setpagelabelfield.md)
- [`setHidePages(array $hidePages, array $hidePagesNot)`](method-sethidepages.md)
- [`setQtyType(string $qtyType)`](method-setqtytype.md)
- [`actions(): null|ProcessPageListActions`](method-actions.md)
- [`getPageActions(Page $page): array`](method-___getpageactions.md) (hookable)
- [`getPageLabel(Page $page, array $options = array()): string`](method-___getpagelabel.md) (hookable)
- [`getPageLabelIconMarkup(Page $page, string &$label): string`](method-getpagelabeliconmarkup.md)
- [`getPageLabelDelimited(Page $page, string $label, array $options): string`](method-getpagelabeldelimited.md)
- [`renderChild(Page $page): array`](method-renderchild.md)
- [`render(): string|array`](method-render.md)
- [`getRenderName(): string`](method-getrendername.md)
- [`getMoreURL(): string`](method-getmoreurl.md)
- [`getChildren(): PageArray`](method-getchildren.md)
- [`getUseTrash(): bool`](method-getusetrash.md)
- [`getNumChildren(Page $page, string|int|bool|null $selector = null): int`](method-___getnumchildren.md) (hookable)
- [`numChildren(Page $page, string|int|bool|null $selector = null): int`](method-numchildren.md)
