# $wireMarkupRegions->find($selector, $markup, array $options = array()): array

Source: `wire/core/WireMarkupRegions.php`

Locate and return all regions of markup having the given attribute

## Usage

~~~~~
// basic usage
$array = $wireMarkupRegions->find($selector, $markup);

// usage with all arguments
$array = $wireMarkupRegions->find($selector, $markup, array $options = array());
~~~~~

## Arguments

- `$selector` `string` Specify one of the following: - Name of an attribute that must be present, i.e. "data-region", or "attribute=value" or "tag[attribute=value]". - Specify `#name` to match a specific `id='name'` attribute. - Specify `.name` or `tag.name` to match a specific `class='name'` attribute (class can appear anywhere in class attribute). - Specify `.name*` to match class name starting with a name prefix. - Specify `<tag>` to match all of those HTML tags (i.e. `<head>`, `<body>`, `<title>`, `<footer>`, etc.)
- `$markup` `string` HTML document markup to perform the find in.
- `$options` (optional) `array` Optional options to modify default behavior: - `single` (bool): Return just the markup from the first matching region (default=false). - `verbose` (bool): Specify true to return array of verbose info detailing what was found (default=false). - `wrap` (bool): Include wrapping markup? Default is false for id or attribute matches, and true for class matches. - `max` (int): Maximum allowed regions to return (default=500). - `exact` (bool): Return region markup exactly as-is? (default=false). Specify true when using return values for replacement. - `leftover` (bool): Specify true if you want to return a "leftover" key in return value with leftover markup. - `type` (string|int): Optional type name to return for each region.

## Return value

- `array` Returns one of the following: - Associative array of [ 'id' => 'markup' ] when finding specific attributes or #id attributes. - Regular array of markup regions when finding regions having a specific class attribute. - Associative array of verbose information when the verbose option is used.

## Exceptions

- `WireException` if given invalid $find string
