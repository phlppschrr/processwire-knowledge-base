# $wireMarkupRegions->populate(&$htmlDocument, $htmlRegions, array $options = array()): int

Source: `wire/core/WireMarkupRegions.php`

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

## Example

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

## Usage

~~~~~
// basic usage
$int = $wireMarkupRegions->populate($htmlDocument, $htmlRegions);

// usage with all arguments
$int = $wireMarkupRegions->populate(&$htmlDocument, $htmlRegions, array $options = array());
~~~~~

## Arguments

- `$htmlDocument` `string` Document to populate regions to
- `$htmlRegions` `string|array` Markup containing regions (or regions array from a find call)
- `$options` (optional) `array` Options to modify behavior: - `useClassActions` (bool): Allow "pw-*" actions to be specified in class names? Per original/legacy spec. (default=false) - `useFileRegions` (bool): Allow use of markup file regions? (default=false)

## Return value

- `int` Number of updates made to $htmlDocument
