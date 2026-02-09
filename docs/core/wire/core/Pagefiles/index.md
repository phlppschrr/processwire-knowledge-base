# Pagefiles

Source: `wire/core/Pagefiles.php`

Inherits: `WireArray`
Implements: `PageFieldValueInterface`


Groups:
Group: [manipulation](group-manipulation.md)
Group: [other](group-other.md)

ProcessWire Pagefiles

Pagefiles is a type of WireArray that contains Pagefile objects. It also acts as the value for multi-file fields in ProcessWire.
The items in a Pagefiles array are `Pagefile` objects, indexed by file basename, i.e. `myfile.pdf`.
Information on most traversal, filtering and manipulation methods can be found in the `WireArray` class that Pagefiles extends.
In the examples below, `$page->files` is an instance of Pagefiles:
~~~~~
// Determining if any files are present
if($page->files->count()) {
  // There are files here
}

// Traversing and outputting links to all files
foreach($page->files as $name => $pagefile) {
  echo "<li><a href='$pagefile->url'>$name: $pagefile->description</a></li>";
}

// Adding new file(s)
$page->files->add('/path/to/file.pdf');
$page->files->add('http://domain.com/photo.png');
$page->save('files');

// Getting file by name
$pagefile = $page->files->getFile('file.pdf');
$pagefile = $page->files['file.pdf']; // alternate

// Getting first and last file
$pagefile = $page->files->first();
$pagefile = $page->files->last();
~~~~~


Typically a Pagefiles object will be associated with a specific field attached to a Page.
There may be multiple instances of Pagefiles attached to a given Page (depending on what fields are in it's fieldgroup).

Methods:
- [`__construct(Page $page)`](method-__construct.md)
- [`__destruct()`](method-__destruct.md)
- [`removeHooks()`](method-removehooks.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`setField(Field $field)`](method-setfield.md)
- [`getPage(): Page`](method-getpage.md)
- [`getField(): Field|null`](method-getfield.md)
- [`__get(int|string $name): bool|mixed|Page|Wire|WireData`](method-__get.md)
- [`add($item): Pagefiles`](method-add.md)
- [`add(Pagefile|string $item): $this`](method-add.md)
- [`delete(Pagefile|string $item): $this`](method-___delete.md) (hookable)
- [`deleteAll(): $this`](method-deleteall.md)
- [`rename(Pagefile $item, string $name): Pagefiles`](method-rename.md)
- [`clone(Pagefile $item, array $options = array()): Pagefile|bool`](method-___clone.md) (hookable)
- [`path(): string`](method-path.md)
- [`url(): string`](method-url.md)
- [`findTag(string|array $tag): Pagefiles`](method-findtag.md)
- [`getTag(string $tag): Pagefile|null`](method-gettag.md)
- [`tags(bool|string|array $value = null): string|array|Pagefiles`](method-tags.md)
- [`getFile(string $name): null|Pagefile`](method-getfile.md)
- [`formatted(bool|null $set = null): bool`](method-formatted.md)
- [`getFieldsPage(): Page`](method-getfieldspage.md)
- [`getFiles(): array`](method-getfiles.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
