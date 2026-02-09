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
Method: [__construct()](method-__construct.md)
Method: [__destruct()](method-__destruct.md)
Method: [removeHooks()](method-removehooks.md)
Method: [setPage()](method-setpage.md)
Method: [setField()](method-setfield.md)
Method: [getPage()](method-getpage.md)
Method: [getField()](method-getfield.md)
Method: [__get()](method-__get.md)
Method: [add()](method-add.md)
Method: [add()](method-add.md)
Method: [delete()](method-___delete.md) (hookable)
Method: [deleteAll()](method-deleteall.md)
Method: [rename()](method-rename.md)
Method: [clone()](method-___clone.md) (hookable)
Method: [path()](method-path.md)
Method: [url()](method-url.md)
Method: [findTag()](method-findtag.md)
Method: [getTag()](method-gettag.md)
Method: [tags()](method-tags.md)
Method: [getFile()](method-getfile.md)
Method: [formatted()](method-formatted.md)
Method: [getFieldsPage()](method-getfieldspage.md)
Method: [getFiles()](method-getfiles.md)
Method: [__debugInfo()](method-__debuginfo.md)
