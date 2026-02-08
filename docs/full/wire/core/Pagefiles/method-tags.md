# Pagefiles::tags()

Source: `wire/core/Pagefiles.php`

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
