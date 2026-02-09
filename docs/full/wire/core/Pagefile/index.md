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
- [`__construct(Pagefiles $pagefiles, string $filename)`](method-__construct.md) Construct a new Pagefile
- [`install(string $filename)`](method-___install.md) (hookable) Install this Pagefile
- [`filedata(string|array|false|null $key = '', null|string|array|int|float $value = null): Pagefile|Pageimage|array|string|int|float|bool|null`](method-filedata.md) Get or set filedata
- [`setDescription(string|array $value, ?Page $language = null): $this`](method-setdescription.md) Set a description, optionally parsing JSON language-specific descriptions to separate properties
- [`description($language = null, null|string $value = null): string|array`](method-description.md) Get or set the file’s description (with multi-language support).
- [`getNext(): Pagefile|null`](method-getnext.md) Return the next sibling Pagefile in the parent Pagefiles, or NULL if at the end.
- [`getPrev(): Pagefile|null`](method-getprev.md) Return the previous sibling Pagefile in the parent Pagefiles, or NULL if at the beginning.
- [`url(): string`](method-url.md) Return the web accessible URL to this Pagefile.
- [`url(): string`](method-___url.md) (hookable) Hookable version of url() method
- [`httpUrl(): string`](method-___httpurl.md) (hookable) Return the web accessible URL (with scheme and hostname) to this Pagefile.
- [`filename(): string`](method-filename.md) Returns the full disk path name filename to the Pagefile.
- [`filename()`](method-___filename.md) (hookable) Hookable version of filename() method
- [`basename(bool $ext = true): string`](method-basename.md) Returns the basename of this Pagefile (name and extension, without disk path).
- [`uploadName(): string`](method-uploadname.md) Original and unsanitized filename at the time it was uploaded
- [`tags(bool|string|array $value = null): string|array`](method-tags.md) Get or set the "tags" property, when in use.
- [`hasTag(string $tag): bool|string`](method-hastag.md) Does this file have the given tag(s)?
- [`addTag(string|array $tag): $this`](method-addtag.md) Add the given tag to this file’s tags (if not already present)
- [`removeTag(string $tag): $this`](method-removetag.md) Remove the given tag from this file’s tags (if present)
- [`filemtime(bool $reset = false): int`](method-filemtime.md) Get last modified time of file
- [`filesize(bool $reset = false): int`](method-filesize.md) Returns the filesize in number of bytes.
- [`filesizeStr(): string`](method-filesizestr.md) Returns the filesize in a formatted, output-ready string (i.e. "123 kB")
- [`ext(): string`](method-ext.md) Returns the file’s extension - "pdf", "jpg", etc.
- [`__toString(): string`](method-__tostring.md) When dereferenced as a string, a Pagefile returns its basename
- [`hash(): string`](method-hash.md) Return a unique MD5 hash representing this Pagefile.
- [`rename(string $basename): string|bool`](method-rename.md) Rename this file
- [`isNew(bool|null $set = null): bool`](method-isnew.md) Get or set “new” status of the Pagefile
- [`save(): bool`](method-save.md) Save this Pagefile independently of the Page it lives on
- [`getFiles(): array`](method-getfiles.md) Get all filenames associated with this file
- [`hidden(bool|null $set = null)`](method-hidden.md) Get or set hidden state of this file
- [`__isset(string $key): bool`](method-__isset.md) Ensures that isset() and empty() work for dynamic class properties
- [`__debugInfo(): array`](method-__debuginfo.md) Debug info

Constants:
- [`createdTemp = 10`](const-createdtemp.md)
