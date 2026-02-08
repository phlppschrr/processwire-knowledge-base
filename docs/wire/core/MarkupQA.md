# MarkupQA

Source: `wire/core/MarkupQA.php`

HTML Markup Quality Assurance

Provides runtime quality assurance for markup stored in [textarea] field values.

1. Ensures URLs referenced in <a> and <img> tags are relative to actual site root.
2. Ensures local page URLs referenced in <a> tags up-to-date with current $page URL.
3. Identifies and logs <img> tags that point to non-existing files in PW's file system.
4. Re-creates image variations that don't exist, when the original still exists.
5. Populates blank 'alt' attributes with actual file description.

- For #1 use the wakeupUrls($value) and sleepUrls($value) methods.
- For #2 use the wakeupHrefs($value) and sleepHrefs($value) methods.
- For #3-5 use the checkImgTags($value, $options) method, where $options specifies 3-5.

Runtime errors are logged to: /site/assets/logs/markup-qa-errors.txt

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Page|null $page

@param Field|null $field

## setPage()

Set the current Page

@param Page $page

## setField()

Set the current Field

@param Field $field

## ignorePaths()

Get or set paths to ignore for link abstraction

To get ignored paths call function with no arguments. Otherwise you are setting them.

@param array|string|null $paths Array of paths or string of one path, or CSV or newline separated string of multiple paths.

@param bool $replace True to replace all existing paths, or false to merge with existing paths (default=false)

@return array Returns array of current ignore paths

@throws WireException if given invalid $paths argument

## debug()

Get or set debug status

Applies only if current user is a superuser

@param bool|null $set Omit this argument to get or specify bool to set

@return bool

## verbose()

Get or set verbose state

Whether or not to set/track verbose information to page, i.e.
`$page->_markupQA = array('field_name' => array(counts))`

When getting, if $page or $field have not been populated, verbose is always false.

@param bool|null $set Omit this argument to get or specify bool to set

@return bool

## wakeupUrls()

Wakeup URLs in href or src attributes for presentation

@param $value

## sleepUrls()

Sleep URLs in href or src attributes for storage

@param $value

## checkUrls()

Wake URLs for wakeup or sleep, converting root URLs as necessary

@param string $value

@param bool $sleep

## relativeToAbsolutePath()

Convert a relative path to be absolute

@param string $path

@return string Returns absolute path, or blank string on error

## sleepLinks()

Sleep href attributes, adding a data-pwid attribute to <a> tags that resolve to a Page

Should be used AFTER sleepUrls() has already been called, so that any URLs are already
relative to "/" rather than potential "/subdir/".

@param string $value

## wakeupLinks()

Wakeup href attributes, using the data-pwid attribute to update the href attribute as necessary

Should be used BEFORE wakeupUrls() is called so that href attributes are relative to "/" rather than
a potential "/subdir/" that wouldn't be recognized as a page path.

@param $value

@return array Returns array of replacements that were made (3.0.184+)

## findLinks()

Find pages linking to another

@param Page|null $page Page to find links to, or omit to use page specified in constructor

@param array $fieldNames Field names to look in or omit to use field specified in constructor

@param string $selector Optional selector to use as a filter

@param array $options Additional options
 - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false)
 - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false)
 - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true)
    You can specify false for this option to make it perform faster, but with a potentially less accurate result.

@return PageArray|array|int

## linkWarning()

Display and log a warning about a path that didn't resolve

@param string $path

@param bool $logWarning

## checkImgTags()

Quality assurance for <img> tags

@param string $value

@param array $options What actions should be performed:
 - replaceBlankAlt (bool): Replace blank alt attributes with file description? (default=true)
 - removeNoExists (bool): Remove references to images that don't exist (or re-create images when possible) (default=true)
 - removeNoAccess (bool): Remove references to images user doesn't have view permission to (default=true)

## checkImgTag()

Quality assurance for one <img> tag

@param string $value Entire markup

@param string $img Just the found <img> tag

@param array $options What actions should be performed:
 - replaceBlankAlt (bool): Replace blank alt attributes with file description? (default=true)
 - removeNoExists (bool): Remove references to images that don't exist (or re-create images when possible) (default=true)
 - removeNoAccess (bool): Remove references to images user doesn't have view permission to (default=true)

## checkImgExists()

Attempt to re-create images that don't exist, when possible

@param Pageimage $pagefile

@param $img

@param $src

@param $value

@return int Returns 0 on no change, negative count on broken, positive count on fixed

## error()

Record error message to image-errors log

@param string $text

@param int $flags

@return $this

## setVerbose()

Get or set a setting

@param string $key Setting name to get or set, or omit to get all settings

@param string|array|int|null $value Setting value to set, or omit when getting setting

@return string|array|int|null|$this Returns value of $key

public function setting($key = null, $value = null) {
if($key === null) return $this->settings; // return all
if($value === null) return isset($this->settings[$key]) ? $this->settings[$key] : null; // return one
if($key === 'ignorePaths') return $this->ignorePaths($value); // set specific
$this->settings[$key] = $value; // set
return $value;
}

## getPagePathFromId()

Given page ID return the path to it

@param int $pageID

@param Language|null $language

@return string

@since 3.0.231

## isPagePathHooked()

Is the Page::path method hooked in a manner that might affect MarkupQA?

@return bool

@since 3.0.231
