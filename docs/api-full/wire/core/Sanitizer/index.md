# Sanitizer

Source: `wire/core/Sanitizer.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Sanitizer

Sanitizer provides shared sanitization functions as commonly used throughout ProcessWire core and modules

Provides methods for sanitizing and validating user input, preparing data for output, and more.
Sanitizer is useful for sanitizing input or any other kind of data that you need to match a particular type or format.
The Sanitizer methods are accessed from the `$sanitizer` API variable and/or `sanitizer()` API variable/function.
For example:
For example:
~~~~~~
$cleanValue = $sanitizer->text($dirtyValue);
~~~~~~
You can replace the `text()` call above with any other sanitizer method. Many sanitizer methods also accept additional
arguments—see each individual method for details.

### Sanitizer and input

Sanitizer methods are most commonly used with user input. As a result, the methods in this class are also accessible
from the `$input->get`, `$input->post` and `$input->cookie` API variables, in the same manner that they are here.
This is a useful shortcut for instances where you don’t need to provide additional arguments to the sanitizer method.
Below are a few examples of this usage:
~~~~~
// get GET variable 'id' as integer
$id = $input->get->int('id');

// get POST variable 'name' as 1-line plain text
$name = $input->post->text('name');

// get POST variable 'comments' as multi-line plain text
$comments = $input->post->textarea('comments');
~~~~~
In ProcessWire 3.0.125 and newer you can also perform the same task as the above with one less `->` level like the
example below:
example below:
~~~~~
$comments = $input->post('comments','textarea');
~~~~~
This is more convenient in some IDEs because it’ll never be flagged as an unrecognized function call. Though outside
of that it makes little difference how you call it, as they both do the same thing.

See the `$input` API variable for more details on how to call sanitizers directly from $input.

### Adding your own sanitizers

You can easily add your own new sanitizers via ProcessWire hooks. Hooks are commonly added in a /site/ready.php file,
or from a Module, though you may add them wherever you want. The following example adds a sanitizer method called
`zip()` which enforces a 5 digit zip code:
~~~~~
$sanitizer->addHook('zip', function(HookEvent $event) {
  $sanitizer = $event->object;
  $value = $event->arguments(0); // get first argument given to method
  $value = $sanitizer->digits($value, 5); // allow only digits, max-length 5
  if(strlen($value) < 5) $value = ''; // if fewer than 5 digits, it is not a zip
  $event->return = $value;
});

// now you can use your zip sanitizer
$dirtyValue = 'Decatur GA 30030';
$cleanValue = $sanitizer->zip($dirtyValue);
echo $cleanValue; // outputs: 30030
~~~~~

### Additional options (3.0.125 or newer)

In ProcessWire 3.0.125+ you can also combine sanitizer methods in a single call. These are defined by separating each
sanitizer method with an understore. The example below runs the value through the text sanitizer and then through the
entities sanitizer:
~~~~~
$cleanValue = $sanitizer->text_entities($dirtyValue);
~~~~~
If you append a number to any sanitizer call that returns a string, it is assumed to be maximum allowed length. For
example, the following would sanitize the value to be text of no more than 20 characters:
example, the following would sanitize the value to be text of no more than 20 characters:
~~~~~
$cleanValue = $sanitizer->text20($dirtyValue);
~~~~~
The above technique also works for any user-defined sanitizers you’ve added via hooks. We like this strategy for
storage of sanitizer calls that are executed at some later point, like those you might store in a module config. It
essentially enables you to define loose data types for sanitization. In addition, if there are other cases where you
need multiple sanitizers to clean a particular value, this strategy can do it with a lot less code than you would
with multiple sanitizer calls.

Most methods in the Sanitizer class focus on sanitization rather than validation, with a few exceptions. You can
convert a sanitizer call to validation call by calling the `validate()` method with the name of the sanitizer and the
value. A validation call simply implies that if the value is modified by sanitization then it is considered invalid
and thus it’ll return a non-value rather than a sanitized value. See the `Sanitizer::validate()` and
`Sanitizer::valid()` methods for usage details.



@link https://processwire.com/api/variables/sanitizer/ Offical $sanitizer API variable Documentation

Methods:
- [`__construct()`](method-__construct.md) Construct the sanitizer
- [`name(string $value, bool|int $beautify = false, int $maxLength = 128, string $replacement = '_', array $options = array()): string`](method-name.md) Sanitize in "name" format (ASCII alphanumeric letters/digits, hyphens, underscores, periods)
- [`names(string|array $value, string $delimeter = ' ', array $allowedExtras = array('-', '_', '.'), string $replacementChar = '_', bool $beautify = false): string|array`](method-names.md) Sanitize a string or array containing multiple names
- [`attrName(string $value, int $maxLength = 255): string`](method-attrname.md) Sanitize to an ASCII-only HTML attribute name
- [`htmlClass(string $value): string`](method-htmlclass.md) Sanitize string to ASCII-only HTML class attribute value
- [`htmlClasses(string|array $value, bool $getArray = false): string|array`](method-htmlclasses.md) Sanitize string to ASCII-only space-separated HTML class attribute values with no duplicates
- [`fieldName(string $value, bool|int $beautify = false, int $maxLength = 128): string`](method-fieldname.md) Sanitize consistent with names used by ProcessWire fields and/or PHP variables
- [`fieldSubfield(string $value, int $limit = 1): string`](method-fieldsubfield.md) Sanitize as a field name but with optional subfield(s) like “field.subfield”
- [`pageName(string $value, bool|int|array $beautify = false, int|array $maxLength = 128, array $options = array()): string`](method-pagename.md) Sanitize as a ProcessWire page name
- [`pageNameTranslate(string $value, int $maxLength = 128): string`](method-pagenametranslate.md) Name filter for ProcessWire Page names with transliteration
- [`pageNameUTF8(string $value, int $maxLength = 128): string`](method-pagenameutf8.md) Sanitize and allow for UTF-8 characters in page name
- [`punyDecodeName(string $value, int $version = 0): string`](method-punydecodename.md) Decode a PW-punycode'd name value
- [`punyEncodeName(string $value, int $version = 0): string`](method-punyencodename.md) Encode a name value to PW-punycode
- [`getPunycodeVersion(int $version = 0): int`](method-getpunycodeversion.md) Get internal Punycode version to use
- [`punycode(): Punycode`](method-punycode.md)
- [`filename(string $value, bool|int $beautify = false, int $maxLength = 128): string`](method-filename.md) Name filter for ProcessWire filenames (basenames only, not paths)
- [`path(string $value, int|array $options = array()): bool|string`](method-path.md) Validate the given path, return path if valid, or false if not valid
- [`pagePathName(string $value, bool|int $beautify = false, int $maxLength = 2048): string`](method-pagepathname.md) Sanitize a page path name
- [`pagePathNameUTF8(string $value): string`](method-pagepathnameutf8.md) Sanitize a UTF-8 page path name (does not perform ASCII/UTF8 conversions)
- [`alpha(string $value, bool|int $beautify = false, int $maxLength = 1024): string`](method-alpha.md) Sanitize to ASCII alpha (a-z A-Z)
- [`alphanumeric(string $value, bool|int $beautify = false, int $maxLength = 1024): string`](method-alphanumeric.md) Sanitize to ASCII alphanumeric (a-z A-Z 0-9)
- [`digits(string $value, int $maxLength = 1024): string`](method-digits.md) Sanitize string to contain only ASCII digits (0-9)
- [`email(string $value, array $options = array()): string`](method-email.md) Sanitize and validate an email address
- [`emailHeader(string $value, bool $headerName = false): string`](method-emailheader.md) Returns a value that may be used in an email header
- [`word(string $value, array $options = array()): string`](method-word.md) Return first word in given string
- [`words($value, array $options = array()): string`](method-words.md) Given string return a new string containing only words
- [`text(string $value, array $options = array()): string`](method-text.md) Sanitize short string of text to single line without HTML
- [`textarea(string $value, array $options = array()): string`](method-textarea.md) Sanitize input string as multi-line text without HTML tags
- [`line(string $value, int|array $maxLength = 0, array $options = array()): string`](method-line.md) Sanitize any string of text to single line, no HTML, and no specific max-length (unless given)
- [`lines(string $value, int|array $maxLength = 0, array $options = array()): string`](method-lines.md) Sanitize input string as multi-line text, no HTML tags, and no specific max length (unless given)
- [`markupToText(string $value, array $options = array()): string`](method-markuptotext.md) Convert a string containing markup or entities to be plain text
- [`markupToLine(string $value, array $options = array()): string`](method-markuptoline.md) Convert a string containing markup or entities to be a single line of plain text
- [`url(string $value, bool|array $options = array()): string`](method-url.md) Sanitize and validate given URL or return blank if it can’t be made valid
- [`httpUrl(string $value, array $options = array()): string`](method-httpurl.md) URL with http or https scheme required
- [`filterValidateURL(string $url, array $options): string`](method-filtervalidateurl.md) Implementation of PHP's FILTER_VALIDATE_URL with IDN and underscore support (will convert to valid)
- [`selectorValue(string|array $value, array|int $options = array()): string|int|bool|mixed`](method-selectorvalue.md) Sanitizes a string value that needs to go in a ProcessWire selector
- [`selectorValueAdvanced(string|array $value, array $options = array()): bool|mixed|string`](method-selectorvalueadvanced.md) Sanitize selector value for advanced text search operator (#=)
- [`selectorValueArray(array $value, array $options = array()): string`](method-selectorvaluearray.md) Wrapper for selectorValueV2() when it receives an array
- [`selectorValueV2(string|array $value, array $options = array()): bool|mixed|string`](method-selectorvaluev2.md) Sanitize selector value (version 2, 3.0.156+)
- [`selectorValueV1($value, array $options = array()): string`](method-selectorvaluev1.md) Sanitize selector value (original, version 1)
- [`entities(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8', bool $doubleEncode = true): string`](method-entities.md) Entity encode a string for output
- [`entities1(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8'): string`](method-entities1.md) Entity encode a string and don’t double encode it if already encoded
- [`entitiesA(array|string|int|float|object|bool $value, int $flags = ENT_QUOTES, string $encoding = 'UTF-8', bool $doubleEncode = true): array|string|int|float|bool`](method-entitiesa.md) Entity encode with support for [A]rrays and other non-string values
- [`entitiesA1(array|string|int|float|object|bool $value, int $flags = ENT_QUOTES, string $encoding = 'UTF-8'): array|string|int|float|bool`](method-entitiesa1.md) Same as entitiesA() but does not double encode
- [`entitiesMarkdown(string $str, array|bool|int $options = array()): string`](method-entitiesmarkdown.md) Entity encode while translating some markdown tags to HTML equivalents
- [`bracketTagsToHtml(string $str, array $options): string`](method-brackettagstohtml.md) Convert HTML bracket tags [tag]...[/tag] to HTML - helper method for entitiesMarkdown()
- [`unentities(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8'): string`](method-unentities.md) Remove entity encoded characters from a string.
- [`purify(string $str, array $options = array()): string`](method-purify.md) Purify HTML markup using HTML Purifier
- [`purifier(array $options = array()): MarkupHTMLPurifier`](method-purifier.md) Return a new HTML Purifier instance
- [`removeNewlines(string $str, string $replacement = ' '): string`](method-removenewlines.md) Remove newlines from the given string and return it
- [`removeWhitespace(string $str, array|string $options = array()): string`](method-removewhitespace.md) Remove or replace all whitespace from string
- [`trim(string $str, string|array $chars = '', string $method = 'trim'): string`](method-trim.md) Trim off all known UTF-8 whitespace types (or given chars) from beginning and ending of string
- [`truncate(string $str, int|array $maxLength = 300, array|string $options = array()): string`](method-truncate.md) Truncate string to given maximum length without breaking words
- [`trunc(string $str, int|array $maxLength = 300, array $options = array()): string`](method-trunc.md) Truncate string to given maximum length without breaking words and with no added visible extras
- [`removeMB4(string|array $value, array $options = array()): string|array`](method-removemb4.md) Removes 4-byte UTF-8 characters (like emoji) that produce error with with MySQL regular “UTF8” encoding
- [`hyphenCase(string $value, array $options = array()): string`](method-hyphencase.md) Convert string to be all hyphenated-lowercase (aka kabab-case, hyphen-case, dash-case, etc.)
- [`kebabCase(string $value, array $options = array()): string`](method-kebabcase.md) Alias of hyphenCase()
- [`snakeCase(string $value, array $options = array()): string`](method-snakecase.md) Convert string to be all snake_case (lowercase and underscores)
- [`camelCase(string $value, array $options = array()): string`](method-camelcase.md) Convert string to be all camelCase
- [`pascalCase(string $value, array $options = array()): string`](method-pascalcase.md) Convert string to PascalCase (like camelCase, but first letter always uppercase)
- [`chars(string $value, string|array $allow = '', string $replacement = '', bool $collapse = true, bool|null $mb = null): string`](method-chars.md) Sanitize string value to have only the given characters
- [`string(string|int|array|object|bool|float $value, $sanitizer = null): string`](method-string.md) Sanitize value to string
- [`date(string|int $value, string|null $format = null, array $options = array()): string|int|null`](method-date.md) Sanitize a date or date/time string, making sure it is valid, and return it
- [`textdomain(string $value): string`](method-textdomain.md) Sanitize as language textdomain
- [`match(string $value, string $regex): string`](method-match.md) Validate that given value matches regex pattern.
- [`int(mixed $value, array $options = array()): int`](method-int.md) Sanitized an integer (unsigned, unless you specify a negative minimum value)
- [`intUnsigned(mixed $value, array $options = array()): int`](method-intunsigned.md) Sanitize to unsigned (0 or positive) integer
- [`intSigned(mixed $value, array $options = array()): int`](method-intsigned.md) Sanitize to signed integer (negative or positive)
- [`range(int|float|string $value, int|float|string|null $min = null, int|float|string|null $max = null): int|float`](method-range.md) Sanitize value to be within the given min and max range
- [`min(int|float|string $value, int|float|string $min = PHP_INT_MIN): int|float`](method-min.md) Sanitize to have a minimum value
- [`max(int|float|string $value, int|float|string $max = PHP_INT_MAX): int|float`](method-max.md) Sanitize to have a maximuim value
- [`float(float|string|int $value, array $options = array()): float|string`](method-float.md) Sanitize to floating point value
- [`array(array|string|mixed $value, string|array $sanitizer = null, array $options = array()): array`](method-___array.md) (hookable) Sanitize array or CSV string to array of values, optionally sanitized by given method
- [`arrayVal(mixed $value, array $options = array()): array`](method-arrayval.md) Simply sanitize value to array with no conversions
- [`intArray(array|string|mixed $value, array|bool $options = array()): array`](method-intarray.md) Sanitize array or CSV string to array of unsigned integers (or signed integers if specified $min is less than 0)
- [`intArrayVal(array|string|mixed $value, array|bool $options = array()): array`](method-intarrayval.md) Sanitize array to be all unsigned integers with no conversions
- [`minArray(array $data, bool|array $allowEmpty = false, bool $convert = false): array`](method-minarray.md) Minimize an array to remove empty values
- [`flatArray(array $value, array $options = array()): array`](method-flatarray.md) Given a potentially multi-dimensional array, return a flat 1-dimensional array
- [`wordsArray(string|array $value, array $options = array()): array`](method-wordsarray.md) Return array of all words in given value (excluding punctuation and other non-word characters)
- [`wordsArrayNumberReplacements(string &$value, string $prefix = 'REP'): array`](method-wordsarraynumberreplacements.md) Identify decimals, minus signs and commas in numbers, replace them, and return the replacements array
- [`option(string|int $value, array $allowedValues = array()): string|int|null`](method-option.md) Return $value if it exists in $allowedValues, or null if it doesn't
- [`options(array $values, array $allowedValues = array()): array`](method-options.md) Return given values that that also exist in $allowedValues whitelist
- [`bool($value): bool`](method-bool.md) Convert the given value to a boolean
- [`bit(string|int|array $value): int`](method-bit.md) Sanitize to a bit, returning only integer 0 or 1
- [`checkbox(int|bool|string|mixed|null $value, int|bool|string|mixed|null $yes = true, int|bool|string|mixed|null $no = false): int|bool|string|mixed|null`](method-checkbox.md) Sanitize checkbox value
- [`maxLength(string|int|array|float $value, int $maxLength = 128, null|int $maxBytes = null): array|float|int|string`](method-maxlength.md) Limit length of given value to that specified
- [`minLength(string $value, int $minLength = 1, string $padChar = '', bool $padLeft = false): string`](method-minlength.md) Validate or sanitize a string to have a minimum length
- [`maxBytes(string $value, int $maxBytes = 128): string`](method-maxbytes.md) Limit bytes used by given string to max specified
- [`testAll(mixed $value): array`](method-___testall.md) (hookable) Run value through all sanitizers, return array indexed by sanitizer name and resulting value
- [`getAll(bool $getReturnTypes = false): array`](method-getall.md) Get all sanitizer method names and optionally types they return
- [`getTextTools(): WireTextTools`](method-gettexttools.md) Get instance of WireTextTools
- [`getNumberTools(): WireNumberTools`](method-getnumbertools.md) Get instance of WireNumberTools
- [`validateFile(string $filename, array $options = array()): bool|array|null`](method-validatefile.md) Validate and sanitize a file using FileValidator modules
- [`sanitize(mixed $value, string $method = 'text'): string|int|array|float|null`](method-sanitize.md) Call a sanitizer method indirectly where method name can contain combined/combo methods
- [`validate(string|int|array|float $value, string $method = 'text', $fallback = null): null|mixed`](method-validate.md) Validate that value remains unchanged by given sanitizer method, or return null if not
- [`valid(string|int|array|float $value, string $method = 'text', bool $strict = false): bool`](method-valid.md) Is given value valid? (i.e. unchanged by given sanitizer method)

Constants:
- [`translate = 2`](const-translate.md)
