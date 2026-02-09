# Pagefile

Source: `wire/core/Pagefile.php`

Inherits: `WireData`
Implements: `WireArrayItem`


Groups:
Group: [date-time](group-date-time.md)
Group: [other](group-other.md)
Group: [tags](group-tags.md)

ProcessWire Pagefile

Represents a single file item attached to a page, typically via a File Fieldtype.
Pagefile objects are contained by a `Pagefiles` object.

Methods:
- [`__construct(Pagefiles $pagefiles, string $filename)`](method-__construct.md)
- [`install(string $filename)`](method-___install.md) (hookable)
- [`filedata(string|array|false|null $key = '', null|string|array|int|float $value = null): Pagefile|Pageimage|array|string|int|float|bool|null`](method-filedata.md)
- [`setDescription(string|array $value, ?Page $language = null): $this`](method-setdescription.md)
- [`description($language = null, null|string $value = null): string|array`](method-description.md)
- [`getNext(): Pagefile|null`](method-getnext.md)
- [`getPrev(): Pagefile|null`](method-getprev.md)
- [`url(): string`](method-url.md)
- [`url(): string`](method-___url.md) (hookable)
- [`httpUrl(): string`](method-___httpurl.md) (hookable)
- [`filename(): string`](method-filename.md)
- [`filename()`](method-___filename.md) (hookable)
- [`basename(bool $ext = true): string`](method-basename.md)
- [`uploadName(): string`](method-uploadname.md)
- [`tags(bool|string|array $value = null): string|array`](method-tags.md)
- [`hasTag(string $tag): bool|string`](method-hastag.md)
- [`addTag(string|array $tag): $this`](method-addtag.md)
- [`removeTag(string $tag): $this`](method-removetag.md)
- [`filemtime(bool $reset = false): int`](method-filemtime.md)
- [`filesize(bool $reset = false): int`](method-filesize.md)
- [`filesizeStr(): string`](method-filesizestr.md)
- [`ext(): string`](method-ext.md)
- [`__toString(): string`](method-__tostring.md)
- [`hash(): string`](method-hash.md)
- [`rename(string $basename): string|bool`](method-rename.md)
- [`isNew(bool|null $set = null): bool`](method-isnew.md)
- [`save(): bool`](method-save.md)
- [`getFiles(): array`](method-getfiles.md)
- [`hidden(bool|null $set = null)`](method-hidden.md)
- [`__isset(string $key): bool`](method-__isset.md)
- [`__debugInfo(): array`](method-__debuginfo.md)

Constants:
- [`createdTemp`](const-createdtemp.md)
