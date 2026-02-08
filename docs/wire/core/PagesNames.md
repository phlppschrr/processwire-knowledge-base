# PagesNames

Source: `wire/core/PagesNames.php`

ProcessWire Pages Names

Pages Names
$pages->names
This class includes methods for generating and modifying page names.
While these methods are mosty for internal core use, some may at times be useful from the public API as well.
You can access methods from this class via the Pages API variable at `$pages->names()`.
~~~~~
if($pages->names()->pageNameExists('something')) {
  // A page named “something” exists
}

// generate a globally unique random page name
$name = $pages->names()->uniqueRandomPageName();
~~~~~

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## setupNewPageName()

Assign a name to given Page (if it doesn’t already have one)


@param Page $page Page to setup a new name for

@param string $format Optional format string to use for name

@return string Returns page name that was assigned

## hasAutogenName()

Does the given page have an auto-generated name (during this request)?


@param Page $page

@return string|bool Returns auto-generated name if present, or boolean false if not

## hasAdjustedName()

Does the given page have a modified “name” during this request?


@param Page $page

@param bool|null $set Specify boolean true or false to set whether or not it has an adjusted name, or omit just to get

@return bool

## isUntitledPageName()

Does the given page have an untitled page name?


@param string $name

@return bool

## nameAndNumber()

If given name has a numbered suffix, return array with name (excluding suffix) and the numbered suffix

Returns array like `[ 'name', 123 ]` where `name` is name without the suffix, and `123` is the numbered suffix.
If the name did not have a numbered suffix, then the 123 will be 0 and `name` will be the given `$name`.


@param string $name

@param string $delimiter Character(s) that separate name and numbered suffix

@return array

## hasNumberSuffix()

Does the given name or Page have a number suffix? Returns the number if yes, or false if not


@param string|Page $name

@param bool $getNamePrefix Return the name prefix rather than the number suffix? (default=false)

@return int|bool|string Returns false if no number suffix, or int for number suffix or string for name prefix (if requested)

## defaultPageNameFormat()

Get the name format string that should be used for given $page if no name was assigned


@param Page $page

@param array $options
 - `fallbackFormat` (string): Fallback format if another cannot be determined (default='untitled-time').
 - `parent` (Page|null): Optional parent page to use instead of $page->parent (default=null).

@return string

## pageNameFromFormat()

Create a page name from the given format

- Returns a generated page name that is not yet assigned to the page.
- If no format is specified, it first falls back to page parent template `childNameFormat` property (if present).
- If no format can be determined, it falls back to a randomly generated page name.
- Does not check if page name is already in use.

Options for $format argument:

- `title` Build name based on “title” field.
- `field` Build name based on any other field name you choose, replace “field” with any field name.
- `text` Text already in the right format (that’s not a field name) will be used literally, replace “text” with your text.
- `random` Randomly generates a name.
- `untitled` Uses an auto-incremented “untitled” name.
- `untitled-time` Uses an “untitled” name followed by date/time number string.
- `a|b|c` Builds name from first matching field name, where a|b|c are your field names.
- `{field}` Builds name from the given field name.
- `{a|b|c}` Builds name first matching field name, where a|b|c would be replaced with your field names.
- `date:Y-m-d-H-i` Builds name from current date - replace “Y-m-d-H-i” with desired wireDate() format.
- `string with space` A string that does not match one of the above and has space is assumed to be a wireDate() format.
- `string with /` A string that does not match one of the above and has a “/” slash is assumed to be a wireDate() format.

For formats above that accept a wireDate() format, see `WireDateTime::date()` method for format details. It accepts PHP
date() format, PHP strftime() format, as well as some other predefined options.


@param Page $page

@param string|array $format Optional format. If not specified, pulls from $page’s parent template.

@param array $options Options to modify behavior. May also be specified in $format argument.
 - `language` (Language|string): Language to use
 - `format` (string): Optional format to use, if $options were specified in $format argument.

@return string

## uniquePageName()

Get a unique page name

1. If given no arguments, it returns a random globally unique page name.
2. If given just a $name, it returns that name (if globally unique), or an incremented version of it that is globally unique.
3. If given both $page and $name, it returns given name if unique in parent, or incremented version that is.
4. If given just a $page, the name is pulled from $page and behavior is the same as #3 above.

The returned value is not yet assigned to the given $page, so if it is something different than what
is already on $page, you’ll want to assign it manually after this.


@param string|Page|array $name Name to make unique
 You may optionally substitute the $page argument or $options arguments here, if that is all you need.

@param Page|string|null|array Page to exclude from duplicate check and/or to pull $name or parent from (if not otherwise specified).
 Note that specifying a Page is important if the page already exists, as it is used as the page to exclude when checking for
 name collisions, and we want to exclude $page from that check. You may optionally substitute the $options or $name arguments
 here, if that is all you need. If $parent or $name are specified separately from this $page argument, they will override
 whatever parent or name settings are on this $page argument.

@param array $options
 - `parent` (Page|null): Optionally specify a different parent if $page does not currently have the parent you want to use.
 - `language` (Language|int): Get unique for this language (if multi-language page names active).
 - `page` (Page|null): If you specified no $page argument, you can optionally bundle it in the $options array.
 - `name` (string): If you specified no $name argument, you can optionally bundle it in the $options array.

@return string Returns unique name

## adjustNameLength()

If name exceeds maxLength, truncate it, while keeping any numbered suffixes in place


@param string $name

@param int $maxLength

@return string

## incrementName()

Increment the suffix of a page name, or add one if not present


@param string $name

@param int|null $num Number to use, or omit to determine and increment automatically

@return string

## pageNameExists()

Is the given name is use by a page?

If the `multilang` option is used, it checks if the page name exists in any language.
IF the `language` option is used, it only checks that particular language (regardless of `multilang` option).


@param string $name

@param array $options
 - `page` (Page|int): Ignore this Page or page ID
 - `parent` (Page|int): Limit search to only this parent.
 - `multilang` (bool): Check other languages if multi-language page names supported? (default=false)
 - `language` (Language|int): Limit check to only this language (default=null)

@return int Returns quantity of pages using name, or 0 if name not in use.

## uniqueRandomPageName()

Get a random, globally unique page name


@param array $options
 - `page` (Page): If name is or should be assigned to a Page, specify it here. (default=null)
 - `length` (int): Required/fixed length, or omit for random length (default=0).
 - `min` (int): Minimum required length, if fixed length not specified (default=6).
 - `max` (int): Maximum allowed length, if fixed length not specified (default=min*2).
 - `alpha` (bool): Include alpha a-z letters? (default=true)
 - `numeric` (bool): Include numeric digits 0-9? (default=true)
 - `confirm` (bool): Confirm that name is globally unique? (default=true)
 - `parent` (Page|int): If specified, name must only be unique for this parent Page or ID (default=0).
 - `prefix` (string): Prepend this prefix to page name (default='').
 - `suffix` (string): Append this suffix to page name (default='').

@return string

## untitledPageName()

Return the untitled page name string


@return string

## pageNameHasConflict()

Does given page have a name that has a conflict/collision?

In multi-language environment this applies to default language only.


@param Page $page Page to check

@return string|bool Returns string with conflict reason or boolean false if no conflict

@throws WireException If given invalid $options argument

@since 3.0.127

## checkNameConflicts()

Check given page’s name for conflicts and increment as needed while also triggering a warning notice


@param Page $page

@since 3.0.127
