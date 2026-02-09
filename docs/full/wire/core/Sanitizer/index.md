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
- [`__construct()`](method-__construct.md)
- [`nameFilter($value, array $allowedExtras, $replacementChar, $beautify = false, $maxLength = 128)`](method-namefilter.md)
- [`name(string $value, bool|int $beautify = false, int $maxLength = 128, string $replacement = '_', array $options = array()): string`](method-name.md)
- [`names(string|array $value, string $delimeter = ' ', array $allowedExtras = array('-', '_', '.'), string $replacementChar = '_', bool $beautify = false): string|array`](method-names.md)
- [`attrName(string $value, int $maxLength = 255): string`](method-attrname.md)
- [`htmlClass(string $value): string`](method-htmlclass.md)
- [`htmlClasses(string|array $value, bool $getArray = false): string|array`](method-htmlclasses.md)
- [`fieldName(string $value, bool|int $beautify = false, int $maxLength = 128): string`](method-fieldname.md)
- [`fieldSubfield(string $value, int $limit = 1): string`](method-fieldsubfield.md)
- [`pageName(string $value, bool|int|array $beautify = false, int|array $maxLength = 128, array $options = array()): string`](method-pagename.md)
- [`pageNameTranslate(string $value, int $maxLength = 128): string`](method-pagenametranslate.md)
- [`pageNameUTF8(string $value, int $maxLength = 128): string`](method-pagenameutf8.md)
- [`punyDecodeName(string $value, int $version = 0): string`](method-punydecodename.md)
- [`punyEncodeName(string $value, int $version = 0): string`](method-punyencodename.md)
- [`getPunycodeVersion(int $version = 0): int`](method-getpunycodeversion.md)
- [`punycode(): Punycode`](method-punycode.md)
- [`filename(string $value, bool|int $beautify = false, int $maxLength = 128): string`](method-filename.md)
- [`path(string $value, int|array $options = array()): bool|string`](method-path.md)
- [`pagePathName(string $value, bool|int $beautify = false, int $maxLength = 2048): string`](method-pagepathname.md)
- [`pagePathNameUTF8(string $value): string`](method-pagepathnameutf8.md)
- [`alpha(string $value, bool|int $beautify = false, int $maxLength = 1024): string`](method-alpha.md)
- [`alphanumeric(string $value, bool|int $beautify = false, int $maxLength = 1024): string`](method-alphanumeric.md)
- [`digits(string $value, int $maxLength = 1024): string`](method-digits.md)
- [`email(string $value, array $options = array()): string`](method-email.md)
- [`emailHeader(string $value, bool $headerName = false): string`](method-emailheader.md)
- [`word(string $value, array $options = array()): string`](method-word.md)
- [`words($value, array $options = array()): string`](method-words.md)
- [`text(string $value, array $options = array()): string`](method-text.md)
- [`textarea(string $value, array $options = array()): string`](method-textarea.md)
- [`line(string $value, int|array $maxLength = 0, array $options = array()): string`](method-line.md)
- [`lines(string $value, int|array $maxLength = 0, array $options = array()): string`](method-lines.md)
- [`markupToText(string $value, array $options = array()): string`](method-markuptotext.md)
- [`markupToLine(string $value, array $options = array()): string`](method-markuptoline.md)
- [`url(string $value, bool|array $options = array()): string`](method-url.md)
- [`httpUrl(string $value, array $options = array()): string`](method-httpurl.md)
- [`filterValidateURL(string $url, array $options): string`](method-filtervalidateurl.md)
- [`selectorValue(string|array $value, array|int $options = array()): string|int|bool|mixed`](method-selectorvalue.md)
- [`selectorValueAdvanced(string|array $value, array $options = array()): bool|mixed|string`](method-selectorvalueadvanced.md)
- [`selectorValueArray(array $value, array $options = array()): string`](method-selectorvaluearray.md)
- [`selectorValueV2(string|array $value, array $options = array()): bool|mixed|string`](method-selectorvaluev2.md)
- [`selectorValueV1($value, array $options = array()): string`](method-selectorvaluev1.md)
- [`entities(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8', bool $doubleEncode = true): string`](method-entities.md)
- [`entities1(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8'): string`](method-entities1.md)
- [`entitiesA(array|string|int|float|object|bool $value, int $flags = ENT_QUOTES, string $encoding = 'UTF-8', bool $doubleEncode = true): array|string|int|float|bool`](method-entitiesa.md)
- [`entitiesA1(array|string|int|float|object|bool $value, int $flags = ENT_QUOTES, string $encoding = 'UTF-8'): array|string|int|float|bool`](method-entitiesa1.md)
- [`entitiesMarkdown(string $str, array|bool|int $options = array()): string`](method-entitiesmarkdown.md)
- [`bracketTagsToHtml(string $str, array $options): string`](method-brackettagstohtml.md)
- [`unentities(string $str, int|bool $flags = ENT_QUOTES, string $encoding = 'UTF-8'): string`](method-unentities.md)
- [`purify(string $str, array $options = array()): string`](method-purify.md)
- [`purifier(array $options = array()): MarkupHTMLPurifier`](method-purifier.md)
- [`removeNewlines(string $str, string $replacement = ' '): string`](method-removenewlines.md)
- [`removeWhitespace(string $str, array|string $options = array()): string`](method-removewhitespace.md)
- [`trim(string $str, string|array $chars = '', string $method = 'trim'): string`](method-trim.md)
- [`truncate(string $str, int|array $maxLength = 300, array|string $options = array()): string`](method-truncate.md)
- [`trunc(string $str, int|array $maxLength = 300, array $options = array()): string`](method-trunc.md)
- [`removeMB4(string|array $value, array $options = array()): string|array`](method-removemb4.md)
- [`hyphenCase(string $value, array $options = array()): string`](method-hyphencase.md)
- [`kebabCase(string $value, array $options = array()): string`](method-kebabcase.md)
- [`snakeCase(string $value, array $options = array()): string`](method-snakecase.md)
- [`camelCase(string $value, array $options = array()): string`](method-camelcase.md)
- [`pascalCase(string $value, array $options = array()): string`](method-pascalcase.md)
- [`chars(string $value, string|array $allow = '', string $replacement = '', bool $collapse = true, bool|null $mb = null): string`](method-chars.md)
- [`string(string|int|array|object|bool|float $value, $sanitizer = null): string`](method-string.md)
- [`date(string|int $value, string|null $format = null, array $options = array()): string|int|null`](method-date.md)
- [`textdomain(string $value): string`](method-textdomain.md)
- [`match(string $value, string $regex): string`](method-match.md)
- [`int($value, array $options = array())`](method-int.md)
- [`int(mixed $value, array $options = array()): int`](method-int.md)
- [`intUnsigned(mixed $value, array $options = array()): int`](method-intunsigned.md)
- [`intSigned(mixed $value, array $options = array()): int`](method-intsigned.md)
- [`range(int|float|string $value, int|float|string|null $min = null, int|float|string|null $max = null): int|float`](method-range.md)
- [`min(int|float|string $value, int|float|string $min = PHP_INT_MIN): int|float`](method-min.md)
- [`max(int|float|string $value, int|float|string $max = PHP_INT_MAX): int|float`](method-max.md)
- [`float(float|string|int $value, array $options = array()): float|string`](method-float.md)
- [`array($value, $sanitizer = null, array $options = array())`](method-___array.md) (hookable)
- [`array(array|string|mixed $value, string|array $sanitizer = null, array $options = array()): array`](method-___array.md) (hookable)
- [`arrayVal(mixed $value, array $options = array()): array`](method-arrayval.md)
- [`intArray(array|string|mixed $value, array|bool $options = array()): array`](method-intarray.md)
- [`intArrayVal(array|string|mixed $value, array|bool $options = array()): array`](method-intarrayval.md)
- [`minArray(array $data, bool|array $allowEmpty = false, bool $convert = false): array`](method-minarray.md)
- [`flatArray(array $value, array $options = array()): array`](method-flatarray.md)
- [`wordsArray(string|array $value, array $options = array()): array`](method-wordsarray.md)
- [`wordsArrayNumberReplacements(string &$value, string $prefix = 'REP'): array`](method-wordsarraynumberreplacements.md)
- [`option(string|int $value, array $allowedValues = array()): string|int|null`](method-option.md)
- [`options(array $values, array $allowedValues = array()): array`](method-options.md)
- [`bool($value)`](method-bool.md)
- [`bool($value): bool`](method-bool.md)
- [`bit(string|int|array $value): int`](method-bit.md)
- [`checkbox(int|bool|string|mixed|null $value, int|bool|string|mixed|null $yes = true, int|bool|string|mixed|null $no = false): int|bool|string|mixed|null`](method-checkbox.md)
- [`maxLength(string|int|array|float $value, int $maxLength = 128, null|int $maxBytes = null): array|float|int|string`](method-maxlength.md)
- [`minLength(string $value, int $minLength = 1, string $padChar = '', bool $padLeft = false): string`](method-minlength.md)
- [`maxBytes(string $value, int $maxBytes = 128): string`](method-maxbytes.md)
- [`testAll(mixed $value): array`](method-___testall.md) (hookable)
- [`getAll(bool $getReturnTypes = false): array`](method-getall.md)
- [`getTextTools(): WireTextTools`](method-gettexttools.md)
- [`getNumberTools(): WireNumberTools`](method-getnumbertools.md)
- [`validateFile($filename, array $options = array())`](method-validatefile.md)
- [`validateFile(string $filename, array $options = array()): bool|array|null`](method-validatefile.md)
- [`__toString()`](method-__tostring.md)
- [`sanitize(mixed $value, string $method = 'text'): string|int|array|float|null`](method-sanitize.md)
- [`validate(string|int|array|float $value, string $method = 'text', $fallback = null): null|mixed`](method-validate.md)
- [`valid(string|int|array|float $value, string $method = 'text', bool $strict = false): bool`](method-valid.md)

Constants:
- [`translate`](const-translate.md)
