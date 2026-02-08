# Pagefile

Source: `wire/core/Pagefile.php`

ProcessWire Pagefile

Represents a single file item attached to a page, typically via a File Fieldtype.
For the most part you’ll want to traverse from the parent `Pagefiles` object than these methods.
Remember to follow up any manipulations with a `$pages->save()` call.
Be sure to see the `Pagefiles::getTag()` and `Pagesfiles::findTag()` methods, which enable you retrieve files by tag.
Pagefile objects are contained by a `Pagefiles` object.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## date-time

@property int $modified Unix timestamp of when Pagefile (file, description or tags) was last modified.

@property-read string $modifiedStr Readable date/time string of when Pagefile was last modified.

@property-read int $mtime Unix timestamp of when file (only) was last modified.

@property-read string $mtimeStr Readable date/time string when file (only) was last modified.

@property int $created Unix timestamp of when file was created.

@property-read string $createdStr Readable date/time string of when Pagefile was created

## other

@property-read string $url URL to the file on the server.

@property-read string $httpUrl URL to the file on the server including scheme and hostname.

@property-read string $URL Same as $url property but with browser cache busting query string appended.

@property-read string $HTTPURL Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.

@property-read string $filename full disk path to the file on the server.

@property-read string $name Returns the filename without the path, same as the "basename" property.

@property-read string $hash Get a unique hash (for the page) representing this Pagefile.

@property string $basename Returns the filename without the path.

@property string $description Value of the file’s description field (string), if enabled. Note you can also set this property directly.

@property string $ext File’s extension (i.e. last 3 or so characters)

@property-read int $filesize File size (number of bytes).

@property string $filesizeStr File size as a formatted string, i.e. “123 Kb”.

@property Pagefiles $pagefiles The Pagefiles WireArray that contains this file.

@property Page $page The Page object that this file is part of.

@property Field $field The Field object that this file is part of.

@property array $filedata

@property int $created_users_id ID of user that added/uploaded the file or 0 if not known (3.0.154+).

@property int $modified_users_id ID of user that last modified the file or 0 if not known (3.0.154+).

@property User|NullPage $createdUser User that added/uploaded the file or NullPage if not known (3.0.154)+.

@property User|NullPage $modifiedUser User that last modified the file or NullPage if not known (3.0.154)+.

@property string $uploadName Original unsanitized filename at upload, see notes for uploadName() method (3.0.212+).

@method void install($filename)

@method string httpUrl()

@method string noCacheURL($http = false)

## tags

@property-read array $tagsArray Get file tags as an array. @since 3.0.17

@property string $tags Value of the file’s tags field (string), if enabled.

## createdTemp

Timestamp 'created' used by pagefiles that are temporary, not yet published

## __construct()

Construct a new Pagefile

~~~~~
// Construct a new Pagefile, assumes that $page->files is a FieldtypeFile Field
$pagefile = new Pagefile($page->files, '/path/to/file.pdf');
~~~~~

@param Pagefiles $pagefiles The Pagefiles WireArray that will contain this file.

@param string $filename Full path and filename to this Pagefile.

## ___install()

Install this Pagefile

Implies copying the file to the correct location (if not already there), and populating its name.
The given $filename may be local (path) or external (URL).


@param string $filename Full path and filename of file to install, or http/https URL to pull file from.

@throws WireException

## filedata()

Get or set filedata

Filedata is any additional data that you want to store with the file’s database record.

- To get a value, specify just the $key argument. Null is returned if request value is not present.
- To get all values, omit all arguments. An associative array will be returned.
- To set a value, specify the $key and the $value to set.
- To set all values at once, specify an associative array for the $key argument.
- To unset, specify boolean false (or null) for $key, and the name of the property to unset as $value.
- To unset, you can also get all values, unset it from the retuned array, and set the array back.


@param string|array|false|null $key Specify array to set all file data, or key (string) to set or get a property,
 Or specify boolean false to remove key specified by $value argument.

@param null|string|array|int|float $value Specify a value to set for given property

@return Pagefile|Pageimage|array|string|int|float|bool|null

## setDescription()

Set a description, optionally parsing JSON language-specific descriptions to separate properties

@param string|array $value

@param Language|null Langage to set it for. Omit to determine automatically.

@return $this

## description()

Get or set the file’s description (with multi-language support).

When not in a multi-language environment, you can still use this method but we recommend using the simpler method of just
getting/seting the `Pagefile::$description` property directly instead.

~~~~~
// Get a Pagefile to work with
$pagefile = $page->files->first();

// Setting description
$pagefile->description('en', 'Setting English description');
$pagefile->description('de', 'Setting German description');

// Getting description for current language (whatever it happens to be)
echo $pagefile->description();

// Getting description for language "de"
echo $pagefile->description('de');
~~~~~


@param null|bool|Language|array
- To GET in current user language: Omit arguments or specify null.
- To GET in another language: Specify a Language name, id or object.
- To GET in all languages as a JSON string: Specify boolean true (if LanguageSupport not installed, regular string returned).
- To GET in all languages as an array indexed by language name: Specify boolean true for both arguments.
- To SET for a language: Specify a language name, id or object, plus the $value as the 2nd argument.
- To SET in all languages as a JSON string: Specify boolean true, plus the JSON string $value as the 2nd argument (internal use only).
- To SET in all languages as an array: Specify the array here, indexed by language ID or name, and omit 2nd argument.

@param null|string $value Specify only when you are setting (single language) rather than getting a value.

@return string|array

## getNext()

Return the next sibling Pagefile in the parent Pagefiles, or NULL if at the end.


@return Pagefile|null

## getPrev()

Return the previous sibling Pagefile in the parent Pagefiles, or NULL if at the beginning.


@return Pagefile|null

## url()

Return the web accessible URL to this Pagefile.

~~~~~
// Example of using the url method/property
foreach($page->files as $file) {
  echo "<li><a href='$file->url'>$file->description</a></li>";
}
~~~~~


@return string

@see Pagefile:httpUrl()

## ___url()

Hookable version of url() method

@return string

## ___httpUrl()

Return the web accessible URL (with scheme and hostname) to this Pagefile.

@return string

@see Pagefile::url()

## filename()

Returns the full disk path name filename to the Pagefile.


@return string

## ___filename()

Hookable version of filename() method

## basename()

Returns the basename of this Pagefile (name and extension, without disk path).

@param bool $ext Specify false to exclude the extension (default=true)

@return string

## uploadName()

Original and unsanitized filename at the time it was uploaded

Returned value is also entity encoded if $page’s output formatting state is ON.
For files uploaded in ProcessWire 3.0.212 or newer. Falls back to current file
basename for files that were uploaded prior to 3.0.212.

@return string

@since 3.0.212

## tags()

Get or set the "tags" property, when in use.

~~~~~
$file = $page->files->first();
$tags = $file->tags(); // Get tags string
$tags = $file->tags(true); // Get tags array
$file->tags("foo bar baz"); // Set tags to be these 3 tags
$tags->tags(["foo", "bar", "baz"]); // Same as above, using array
~~~~~


@param bool|string|array $value Specify one of the following:
  - Omit to simply return the tags as a string.
  - Boolean true if you want to return tags as an array (rather than string).
  - Boolean false to return tags as an array, with lowercase enforced.
  - String or array if you are setting the tags.

@return string|array Returns the current tags as a string or an array.
  When an array is returned, it is an associative array where the key and value are both the tag (keys are always lowercase).

@see Pagefile::addTag(), Pagefile::hasTag(), Pagefile::removeTag()

## hasTag()

Does this file have the given tag(s)?

~~~~~
$file = $page->files->first();

if($file->hasTag('foobar')) {
  // file has the "foobar" tag
}

if($file->hasTag("foo|baz")) {
  // file has either the foo OR baz tag
}

if($file->hasTag("foo,baz")) {
 // file has both the foo AND baz tags (since 3.0.17)
}
~~~~~

3.0.17 Added support for AND mode, where multiple tags can be specified and all must be present to return true.
3.0.17 OR mode now returns found tag rather than boolean true.

@param string $tag Specify one of the following:
 - Single tag without whitespace.
 - Multiple tags separated by a "|" to determine if Pagefile has at least one of the tags.
 - Multiple tags separated by a comma to determine if Pagefile has all of the tags. (since 3.0.17)

@return bool|string True if it has the given tag(s), false if not.
- If multiple tags were specified separated by a "|", then if at least one was present, this method returns the found tag.
- If multiple tags were specified separated by a space or comma, and all tags are present, it returns true. (since 3.0.17)

@see Pagefile::tags(), Pagefile::addTag(), Pagefile::removeTag()

## addTag()

Add the given tag to this file’s tags (if not already present)

~~~~~
$file = $page->files->first();
$file->addTag('foo'); // add single tag
$file->addTag('foo,bar,baz'); // add multiple tags
$file->addTag(['foo', 'bar', 'baz']); // same as above, using array
~~~~~


@param string|array $tag Tag to add, or array of tags to add, or CSV string of tags to add.

@return $this

@since 3.0.17

@see Pagefile::tags(), Pagefile::hasTag(), Pagefile::removeTag()

## removeTag()

Remove the given tag from this file’s tags (if present)

~~~~~
$file = $page->files->first();
$file->removeTag('foo'); // remove single tag
$file->removeTag('foo,bar,baz'); // remove multiple tags
$file->removeTag(['foo', 'bar', 'baz']); // same as above, using array
~~~~~


@param string $tag Tag to remove, or array of tags to remove, or CSV string of tags to remove.

@return $this

@since 3.0.17

@see Pagefile::tags(), Pagefile::hasTag(), Pagefile::addTag()

## filemtime()

Get last modified time of file

@param bool $reset

@return int Unix timestamp

@since 3.0.154

## filesize()

Returns the filesize in number of bytes.

@param bool $reset

@return int

## filesizeStr()

Returns the filesize in a formatted, output-ready string (i.e. "123 kB")

@return string

## ext()

Returns the file’s extension - "pdf", "jpg", etc.

@return string

## __toString()

When dereferenced as a string, a Pagefile returns its basename

@return string

## hash()

Return a unique MD5 hash representing this Pagefile.

This hash can be counted on to be unique among all files on a given page, regardless of field.

@return string

## rename()

Rename this file

Remember to follow this up with a `$page->save()` for the page that the file lives on.


@param string $basename New name to use. Must be just the file basename (no path).

@return string|bool Returns new name (basename) on success, or boolean false if rename failed.

## isNew()

Get or set “new” status of the Pagefile

This is true with a Pagefile that was created during this request and not loaded from DB.

@param bool|null $set

@return bool

## save()

Save this Pagefile independently of the Page it lives on

@return bool

@throws WireException

@since 3.0.154

## getFiles()

Get all filenames associated with this file

@return array

 @since 3.0.233

## hidden()

Get or set hidden state of this file

Files that are hidden do not appear in the formatted field value,
but do appear in the unformatted value.

@param bool|null $set

@since 3.0.237

## __isset()

Ensures that isset() and empty() work for dynamic class properties

@param string $key

@return bool

## __debugInfo()

Debug info

@return array
