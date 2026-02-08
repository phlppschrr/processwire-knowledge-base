# $wireTextTools->populatePlaceholders($str, $vars, array $options = array()): string

Source: `wire/core/WireTextTools.php`

Given a string ($str) and values ($vars), populate placeholder “{tags}” in the string with the values

- The `$vars` should be an associative array of `[ 'tag' => 'value' ]`.
- The `$vars` may also be an object, in which case values will be pulled as properties of the object.

By default, tags are specified in the format: {first_name} where first_name is the name of the
variable to pull from $vars, `{` is the opening tag character, and `}` is the closing tag char.

The tag parser can also handle subfields and OR tags, if `$vars` is an object that supports that.
For instance `{products.title}` is a subfield, and `{first_name|title|name}` is an OR tag.

~~~~~
$vars = [ 'foo' => 'FOO!', 'bar' => 'BAR!' ];
$str = 'This is a test: {foo}, and this is another test: {bar}';
echo $sanitizer->getTextTools()->populatePlaceholders($str, $vars);
// outputs: This is a test: FOO!, and this is another test: BAR!
~~~~~

## Arguments

- string $str The string to operate on (where the {tags} might be found)
- WireData|object|array $vars Object or associative array to pull replacement values from.
- array $options Array of optional changes to default behavior, including: - `tagOpen` (string): The required opening tag character(s), default is '{' - `tagClose` (string): The optional closing tag character(s), default is '}' - `recursive` (bool): If replacement value contains tags, populate those too? (default=false) - `removeNullTags` (bool): If a tag resolves to a NULL (i.e. field not present), remove it? (default=true) - `removeEmptyTags` (bool): If a tag value resolves to blank string, false or NULL, remove it? (default=true) 3.0.237+ - `entityEncode` (bool): Entity encode the values pulled from $vars? (default=false) - `entityDecode` (bool): Entity decode the values pulled from $vars? (default=false) - `allowMarkup` (bool): Allow markup to appear in populated variables? (default=true)

## Return value

string String with tags populated.

## Meta

- @since 3.0.126 Use wirePopulateStringTags() function for older versions
