# Pagefiles

Source: `wire/core/Pagefiles.php`

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

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## manipulation

@method Pagefiles delete() delete(Pagefile $file) Removes the file and deletes from disk when page is saved.

@method Pagefile|bool clone(Pagefile $item, array $options = array()) Duplicate a file and return it.

## other

@property string $path Returns the full server disk path where files are stored.

@property string $url Returns the URL where files are stored.

@property Page $page Returns the Page that contains this set of files, same as the getPage() method.

@property Field $field Returns the Field that contains this set of files, same as the getField() method.

## __construct()

Construct a Pagefiles object

@param Page $page The page associated with this Pagefiles instance

## __destruct()

Destruct and ensure that hooks are removed

## removeHooks()

Remove hooks to the PagefilesManager instance

## setPage()

Set the Page these files are assigned to

@param Page $page

## setField()

Set the field these files are assigned to

@param Field $field

## getPage()

Get the page these files are assigned to

@return Page

## getField()

Get the field these files are assigned to

@return Field|null Returns Field, or null if Field has not yet been assigned.

## __get()

Get for direct access to properties

@param int|string $name

@return bool|mixed|Page|Wire|WireData

## add()

Find all Pagefiles matching the given selector string or tag

@param string $selector

@return Pagefiles New instance of Pagefiles

public function find($selector) {
if(!Selectors::stringHasOperator($selector)) {
// if there is no selector operator in the strong, consider it a tag first
$value = $this->findTag($selector);
// if it didn't match any tag, then see if it matches in some other way
if(!count($value)) $value = parent::find($selector);
} else {
// there is an operator so we send it straight to WireArray
$value = parent::find($selector);
}
return $value;
}

## add()

Add a new Pagefile item or filename

If give a filename (string) it will create the new `Pagefile` item from it and add it.


@param Pagefile|string $item If item is a string (filename) it will create the new `Pagefile` item from it and add it.

@return $this

## ___delete()

Delete a pagefile item

Deletes the filename associated with the Pagefile and removes it from this Pagefiles array.
The actual deletion of the file does not take effect until `$page->save()`.


@param Pagefile|string $item Pagefile or basename

@return $this

## deleteAll()

Delete all files associated with this Pagefiles instance, leaving a blank Pagefiles instance.

The actual deletion of the files does not take effect until `$page->save()`.


@return $this

## rename()

Queue a rename of a Pagefile

This only queues a rename. Rename actually occurs when page is saved.
Note this differs from the behavior of `Pagefile::rename()`.


@param Pagefile $item

@param string $name

@return Pagefiles

@see Pagefile::rename()

## ___clone()

Duplicate the Pagefile and add to this Pagefiles instance

After duplicating a file, you must follow up with a save of the page containing it.
Otherwise the file is marked for deletion.

@param Pagefile $item Pagefile item to duplicate

@param array $options Options to modify default behavior:
 - `action` (string): Specify "append", "prepend", "after", "before" or blank to only return Pagefile. (default="after")
 - `pagefiles` (Pagefiles): Pagefiles instance file should be duplicated to. (default=$this)

@return Pagefile|bool Returns new Pagefile or boolean false on fail

## path()

Return the full disk path where files are stored

@return string

## url()

Returns the web accessible index URL where files are stored

@return string

## findTag()

Return all Pagefile objects that have the given tag(s).

Given tag may be any of the following:

- `foo` (single tag): Will return all Pagefile objects having the specified tag.
- `foo|bar|baz` (multiple OR tags): Will return Pagefile objects having at least one of the tags listed.
- `foo,bar,baz` (multiple AND tags): Will return Pagefile objects having ALL of the tags listed (since 3.0.17).
- `['foo','bar','baz']` (multiple AND tags array): Same as above but can be specified as an array (since 3.0.17).

3.0.17 Added support for multiple AND tags and allow tag specified as an array.

@param string|array $tag

@return Pagefiles New Pagefiles array with items that matched the given tag(s).

@see Pagefiles::getTag(), Pagefile::hasTag(), Pagefile::tags()

## getTag()

Return the first Pagefile that matches the given tag or NULL if no match

Given tag may be any of the following:

- `foo` (single tag): Will return the first Pagefile object having the specified tag.
- `foo|bar|baz` (multiple OR tags): Will return first Pagefile object having at least one of the tags listed.
- `foo,bar,baz` (multiple AND tags): Will return first Pagefile object having ALL of the tags listed (since 3.0.17).
- `['foo','bar','baz']` (multiple AND tags array): Same as above but can be specified as an array (since 3.0.17).

3.0.17 Added support for multiple AND tags and allow tag specified as an array.

@param string $tag

@return Pagefile|null

@see Pagefiles::findTag(), Pagefile::hasTag(), Pagefile::tags()

## tags()

Get list of tags for all files in this Pagefiles array, or return files matching given tag(s)

This method can either return a list of all tags available, or return all files
matching the given tag or tags (an alias of findTag method).

~~~~~
// Get string of all tags
$tagsString = $page->files->tags();

// Get array of all tags
$tagsArray = $page->files->tags(true);

// Find all files matching given tag
$pagefiles = $page->files->tags('foobar');
~~~~~


@param bool|string|array $value Specify one of the following:
 - Omit to return all tags as a string.
 - Boolean true if you want to return tags as an array (rather than string).
 - Boolean false to return tags as an array, with lowercase enforced.
 - String if you want to return files matching tags (See `Pagefiles::findTag()` method for usage)
 - Array if you want to return files matching tags (See `Pagefiles::findTag()` method for usage)

@return string|array|Pagefiles Returns all tags as a string or an array, or Pagefiles matching given tag(s).
  When a tags array is returned, it is an associative array where the key and value are both the tag (keys are always lowercase).

@see Pagefiles::findTag(), Pagefile::tags()

## getFile()

Get the Pagefile having the given basename, or null if not found.

@param string $name

@return null|Pagefile

## formatted()

Get or set formatted state

@param bool|null $set

@return bool

## getFieldsPage()

Get mock/placeholder Page object used for Pagefile custom fields

@return Page

@since 3.0.142

## getFiles()

Get all filenames associated with this Pagefiles object

@return array

@since 3.0.233

## __debugInfo()

Debug info

@return array
