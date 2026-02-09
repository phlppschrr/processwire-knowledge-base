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
- [`__construct(Page $page)`](method-__construct.md) Construct a Pagefiles object
- [`__destruct()`](method-__destruct.md) Destruct and ensure that hooks are removed
- [`removeHooks()`](method-removehooks.md) Remove hooks to the PagefilesManager instance
- [`setPage(Page $page)`](method-setpage.md) Set the Page these files are assigned to
- [`setField(Field $field)`](method-setfield.md) Set the field these files are assigned to
- [`getPage(): Page`](method-getpage.md) Get the page these files are assigned to
- [`getField(): Field|null`](method-getfield.md) Get the field these files are assigned to
- [`__get(int|string $name): bool|mixed|Page|Wire|WireData`](method-__get.md) Get for direct access to properties
- [`add($item): Pagefiles`](method-add.md) Find all Pagefiles matching the given selector string or tag
- [`add(Pagefile|string $item): $this`](method-add.md) Add a new Pagefile item or filename
- [`delete(Pagefile|string $item): $this`](method-___delete.md) (hookable) Delete a pagefile item
- [`deleteAll(): $this`](method-deleteall.md) Delete all files associated with this Pagefiles instance, leaving a blank Pagefiles instance.
- [`rename(Pagefile $item, string $name): Pagefiles`](method-rename.md) Queue a rename of a Pagefile
- [`clone(Pagefile $item, array $options = array()): Pagefile|bool`](method-___clone.md) (hookable) Duplicate the Pagefile and add to this Pagefiles instance
- [`path(): string`](method-path.md) Return the full disk path where files are stored
- [`url(): string`](method-url.md) Returns the web accessible index URL where files are stored
- [`findTag(string|array $tag): Pagefiles`](method-findtag.md) Return all Pagefile objects that have the given tag(s).
- [`getTag(string $tag): Pagefile|null`](method-gettag.md) Return the first Pagefile that matches the given tag or NULL if no match
- [`tags(bool|string|array $value = null): string|array|Pagefiles`](method-tags.md) Get list of tags for all files in this Pagefiles array, or return files matching given tag(s)
- [`getFile(string $name): null|Pagefile`](method-getfile.md) Get the Pagefile having the given basename, or null if not found.
- [`formatted(bool|null $set = null): bool`](method-formatted.md) Get or set formatted state
- [`getFieldsPage(): Page`](method-getfieldspage.md) Get mock/placeholder Page object used for Pagefile custom fields
- [`getFiles(): array`](method-getfiles.md) Get all filenames associated with this Pagefiles object
- [`__debugInfo(): array`](method-__debuginfo.md) Debug info
