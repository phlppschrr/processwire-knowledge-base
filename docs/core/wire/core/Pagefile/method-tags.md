# Pagefile::tags()

Source: `wire/core/Pagefile.php`

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
