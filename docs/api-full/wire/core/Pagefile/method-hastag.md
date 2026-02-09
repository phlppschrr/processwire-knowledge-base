# $pagefile->hasTag($tag): bool|string

Source: `wire/core/Pagefile.php`

Does this file have the given tag(s)?


3.0.17 Added support for AND mode, where multiple tags can be specified and all must be present to return true.
3.0.17 OR mode now returns found tag rather than boolean true.

## Example

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

## Usage

~~~~~
// basic usage
$bool = $pagefile->hasTag($tag);
~~~~~

## Arguments

- `$tag` `string` Specify one of the following: - Single tag without whitespace. - Multiple tags separated by a "|" to determine if Pagefile has at least one of the tags. - Multiple tags separated by a comma to determine if Pagefile has all of the tags. (since 3.0.17)

## Return value

- `bool|string` True if it has the given tag(s), false if not. - If multiple tags were specified separated by a "|", then if at least one was present, this method returns the found tag. - If multiple tags were specified separated by a space or comma, and all tags are present, it returns true. (since 3.0.17)

## See Also

- [Pagefile::tags()](method-tags.md)
- [Pagefile::addTag()](method-addtag.md)
- [Pagefile::removeTag()](method-removetag.md)
