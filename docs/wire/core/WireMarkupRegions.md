# WireMarkupRegions

Source: `wire/core/WireMarkupRegions.php`

ProcessWire Markup Regions

Supports finding and manipulating of markup regions in an HTML document.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## debug

Debug during development of this class

## debugLandmark

Markup landmark where debug notes should be placed

## find()

Locate and return all regions of markup having the given attribute

@param string $selector Specify one of the following:
 - Name of an attribute that must be present, i.e. "data-region", or "attribute=value" or "tag[attribute=value]".
 - Specify `#name` to match a specific `id='name'` attribute.
 - Specify `.name` or `tag.name` to match a specific `class='name'` attribute (class can appear anywhere in class attribute).
 - Specify `.name*` to match class name starting with a name prefix.
 - Specify `<tag>` to match all of those HTML tags (i.e. `<head>`, `<body>`, `<title>`, `<footer>`, etc.)

@param string $markup HTML document markup to perform the find in.

@param array $options Optional options to modify default behavior:
 - `single` (bool): Return just the markup from the first matching region (default=false).
 - `verbose` (bool): Specify true to return array of verbose info detailing what was found (default=false).
 - `wrap` (bool): Include wrapping markup? Default is false for id or attribute matches, and true for class matches.
 - `max` (int): Maximum allowed regions to return (default=500).
 - `exact` (bool): Return region markup exactly as-is? (default=false). Specify true when using return values for replacement.
 - `leftover` (bool): Specify true if you want to return a "leftover" key in return value with leftover markup.
 - `type` (string|int): Optional type name to return for each region.

@return array Returns one of the following:
 - Associative array of [ 'id' => 'markup' ] when finding specific attributes or #id attributes.
 - Regular array of markup regions when finding regions having a specific class attribute.
 - Associative array of verbose information when the verbose option is used.

@throws WireException if given invalid $find string

## findMulti()

Multi-selector version of find(), where $selector contains CSV

@param string $selector

@param string $markup

@param array $options

@return array

## hasClass()

Does the given class exist in given $classes array?

@param string $class May be class name, or class prefix if $class has "*" at end.

@param array $classes

@return bool|string Returns false if no match, or class name if matched

## parseFindSelector()

Given a $find selector return array with tests and other meta info

@param string $find

@return array Returns array of [
  'tests' => [ 0 => '', 1 => '', ...],
  'find' => '',
  'findTag' => '',
  'hasClass' => '',
]

## getTagRegion()

Given all markup after a tag, return just the portion that is the tag body/region

@param string $region Markup that occurs after the ">" of the tag you want to get the region of.

@param array $tagInfo Array returned by getTagInfo method.

@param array $options Options to modify behavior, see getMarkupRegions $options argument.
 - `verbose` (bool): Verbose mode (default=false)
 - `wrap` (bool): Whether or not wrapping markup should be included (default=false)

@return array|string Returns string except when verbose mode enabled it returns array.

## getTagInfo()

Given HTML tag like “<div id='foo' class='bar baz'>” return associative array of info about it

Returned info includes:
 - `name` (string): Tag name
 - `id` (string): Value of id attribute
 - `pwid` (string): PW region ID from 'pw-id' or 'data-pw-id', or if not present, then same as 'id'
 - `action` (string): Action for this region, without “pw-” prefix.
 - `actionTarget` (string): Target id for the action, if applicable.
 - `actionType` (string): "class" if action specified as class name, "attr" if specified as a pw- or data-pw attribute.
 - `classes` (array): Array of class names (from class attribute).
 - `attrs` (array): Associative array of all attributes, all values are strings.
 - `attrStr` (string): All attributes in a string
 - `tag` (string): The entire tag as given
 - `close` (string): The HTML string that would close this tag

@param string $tag Must be a tag in format “<tag attrs>”

@return array

## stripRegions()

Strip the given region non-nested tags from the document

Note that this only works on non-nested tags like HTML comments, script or style tags.

@param string $tag Specify "<!--" to remove comments or "<script" to remove scripts, or "<tag" for any other tags.

@param string $markup Markup to remove the tags from

@param bool $getRegions Specify true to return array of the strip regions rather than the updated markup

@return string|array

## stripOptional()

Strip optional tags/comments from given markup

@param string $markup

@param bool $debug

@return string

## mergeTags()

Merge attributes from one HTML tag to another

- Attributes (except class) that appear in $mergeTag replace those in $htmlTag.
- Attributes in $mergeTag not already present in $htmlTag are added to it.
- Class attribute is combined with all classes from $htmlTag and $mergeTag.
- The tag name from $htmlTag is used, and the one from $mergeTag is ignored.

@param string $htmlTag HTML tag string, optionally containing attributes

@param array|string $mergeTag HTML tag to merge (or attributes array)

@return string Updated HTML tag string with merged attributes

## renderAttributes()

Given an associative array of “key=value” attributes, render an HTML attribute string of them

- For boolean attributes without value (like "checked" or "selected") specify boolean true as the value.
- If value of any attribute is an array, it will be converted to a space-separated string.
- Values get entity encoded, unless you specify false for the second argument.

@param array $attrs Associative array of attributes.

@param bool $encode Entity encode attribute values? Default is true, so if they are already encoded, specify false.

@param string $quote Quote style, specify double quotes, single quotes, or blank for none except when required (default=")

@return string

## hasAttribute()

Does the given attribute name and value appear somewhere in the given html?

@param string $name

@param string|bool $value Value to find, or specify boolean true for boolean attribute without value

@param string $html

@return bool Returns false if it doesn't appear, true if it does

## update()

Update the region(s) that match the given $selector with the given $content (markup/text)

@param string $selector Specify one of the following:
 - Name of an attribute that must be present, i.e. "data-region", or "attribute=value" or "tag[attribute=value]".
 - Specify `#name` to match a specific `id='name'` attribute.
 - Specify `.name` or `tag.name` to match a specific `class='name'` attribute (class can appear anywhere in class attribute).
 - Specify `<tag>` to match all of those HTML tags (i.e. `<head>`, `<body>`, `<title>`, `<footer>`, etc.)

@param string $content Markup/text to update with

@param string $markup Document markup where region(s) exist

@param array $options Specify any of the following:
 - `action` (string): May be 'replace', 'append', 'prepend', 'before', 'after', 'remove', or 'auto'.
 - `mergeAttr` (array): Array of attrs to add/merge to the wrapping element, or HTML tag with attrs to merge.

@return string

## replace()

Replace the region(s) that match the given $selector with the given $replace markup

@param string $selector See the update() method $selector argument for supported formats

@param string $replace Markup to replace with

@param string $markup Document markup where region(s) exist

@param array $options See $options argument for update() method

@return string

## append()

Append the region(s) that match the given $selector with the given $content markup

@param string $selector See the update() method $selector argument for details

@param string $content Markup to append

@param string $markup Document markup where region(s) exist

@param array $options See the update() method $options argument for details

@return string

## prepend()

Prepend the region(s) that match the given $selector with the given $content markup

@param string $selector See the update() method for details

@param string $content Markup to prepend

@param string $markup Document markup where region(s) exist

@param array $options See the update() method for details

@return string

## before()

Insert region(s) that match the given $selector before the given $content markup

@param string $selector See the update() method for details

@param string $content Markup to prepend

@param string $markup Document markup where region(s) exist

@param array $options See the update() method for details

@return string

## after()

Insert the region(s) that match the given $selector after the given $content markup

@param string $selector See the update() method for details

@param string $content Markup to prepend

@param string $markup Document markup where region(s) exist

@param array $options See the update() method for details

@return string

## remove()

Remove the region(s) that match the given $selector

@param string $selector See the update() method for details

@param string $markup Document markup where region(s) exist

@param array $options See the update() method for details

@return string

## initHtml()

Initialize given HTML for markup regions

@param string $html

@since 3.0.250

## populate()

Identify and populate markup regions in given HTML

To use this, you must set `$config->useMarkupRegions = true;` in your /site/config.php file.
In the future it may be enabled by default for any templates with text/html content-type.

This takes anything output before the opening `<!DOCTYPE` and connects it to the right places
within the `<html>` that comes after it. For instance, if there's a `<div id='content'>` in the
document, then a #content element output prior to the doctype will replace it during page render.
This enables one to use delayed output as if it’s direct output. It also makes every HTML element
in the output with an “id” attribute a region that can be populated from any template file. It’s
a good pairing with a `$config->appendTemplateFile` that contains the main markup and region
definitions, though can be used with or without it.

Beyond replacement of elements, append, prepend, insert before, insert after, and remove are also
supported via “pw-” prefix attributes that you can add. The attributes do not appear in the final output
markup. When performing replacements or modifications to elements, PW will merge the attributes
so that attributes present in the final output are present, plus any that were added by the markup
regions. See the examples for more details.

Examples
========
Below are some examples. Note that “main” is used as an example “id” attribute of an element that
appears in the main document markup, and the examples below focus on manipulating it. The examples
assume there is a `<div id=main>` in the _main.php file (appendTemplateFile), and the lines in the
examples would be output from a template file, which manipulates what would ultimately be output
when the page is rendered.

In the examples, a “pw-id” or “data-pw-id” attribute may be used instead of an “id” attribute, when
or if preferred. In addition, any “pw-” attribute may be specified as a “data-pw-” attribute if you
prefer it.
~~~~~~
Replacing and removing elements

  <div id='main'>This replaces the #main div and merges any attributes</div>
  <div pw-replace='main'>This does the same as above</div>
  <div id='main' pw-replace>This does the same as above</div>
  <div pw-remove='main'>This removes the #main div</div>
  <div id='main' pw-remove>This removes the #main div (same as above)</div>

Prepending and appending elements

  <div id='main' class='pw-prepend'><p>This prepends #main with this p tag</p></div>
  <p pw-prepend='main'>This does the same as above</p>
  <div id='main' pw-append><p>This appends #main with this p tag</p></div>
  <p pw-append='main'>Removes the #main div</p>

Modifying attributes on an existing element

  <div id='main' class='bar' pw-prepend><p>This prepends #main and adds "bar" class to main</p></div>
  <div id='main' class='foo' pw-append><p>This appends #main and adds a "foo" class to #main</p></div>
  <div id='main' title='hello' pw-append>Appends #main with this text + adds title attribute to #main</div>
  <div id='main' class='-baz' pw-append>Appends #main with this text + removes class “baz” from #main</div>

Inserting new elements

  <h2 pw-before='main'>This adds an h2 headline with this text before #main</h2>
  <footer pw-after='main'><p>This adds a footer element with this text after #main</p></footer>
  <div pw-append='main' class='foo'>This appends a div.foo to #main with this text</div>
  <div pw-prepend='main' class='bar'>This prepends a div.bar to #main with this text</div>

~~~~~~

@param string $htmlDocument Document to populate regions to

@param string|array $htmlRegions Markup containing regions (or regions array from a find call)

@param array $options Options to modify behavior:
 - `useClassActions` (bool): Allow "pw-*" actions to be specified in class names? Per original/legacy spec. (default=false)
 - `useFileRegions` (bool): Allow use of markup file regions? (default=false)

@return int Number of updates made to $htmlDocument

## populateSingles()

Populate single-use tags as unnamed markup regions

@param string $htmlDocument

@param array|string $htmlRegions

@since 3.0.250

## populateFileRegions()

Populate file regions

@param string $htmlDocument

@param array|string $htmlRegions

@param array $options

@param bool $debug

## removeRegionTags()

Remove any <region> or <pw-region> tags present in the markup, leaving their innerHTML contents

Also removes data-pw-id and pw-id attributes

@param string $html

@return bool True if tags or attributes were removed, false if not

## hasRegions()

Is the given HTML markup likely to have regions?

@param string $html

@return bool

## hasRegionActions()

Does the given HTML markup have references to any pw-actions?

@param string $html

@return bool

## fileRegions()

Get instance of WireMarkupFileRegions

@return WireMarkupFileRegions

@since 3.0.254
