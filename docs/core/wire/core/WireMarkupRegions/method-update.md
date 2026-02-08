# $wireMarkupRegions->update($selector, $content, $markup, array $options = array()): string

Source: `wire/core/WireMarkupRegions.php`

Update the region(s) that match the given $selector with the given $content (markup/text)

## Arguments

- string $selector Specify one of the following: - Name of an attribute that must be present, i.e. "data-region", or "attribute=value" or "tag[attribute=value]". - Specify `#name` to match a specific `id='name'` attribute. - Specify `.name` or `tag.name` to match a specific `class='name'` attribute (class can appear anywhere in class attribute). - Specify `<tag>` to match all of those HTML tags (i.e. `<head>`, `<body>`, `<title>`, `<footer>`, etc.)
- string $content Markup/text to update with
- string $markup Document markup where region(s) exist
- array $options Specify any of the following: - `action` (string): May be 'replace', 'append', 'prepend', 'before', 'after', 'remove', or 'auto'. - `mergeAttr` (array): Array of attrs to add/merge to the wrapping element, or HTML tag with attrs to merge.

## Return value

string
