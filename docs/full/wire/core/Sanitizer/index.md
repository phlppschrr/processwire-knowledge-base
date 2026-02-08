# Sanitizer

Source: `wire/core/Sanitizer.php`

ProcessWire Sanitizer

Sanitizer provides shared sanitization functions as commonly used throughout ProcessWire core and modules

Provides methods for sanitizing and validating user input, preparing data for output, and more.
Sanitizer is useful for sanitizing input or any other kind of data that you need to match a particular type or format.
The Sanitizer methods are accessed from the `$sanitizer` API variable and/or `sanitizer()` API variable/function.
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


ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

@link https://processwire.com/api/variables/sanitizer/ Offical $sanitizer API variable Documentation

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [nameFilter()](method-namefilter.md)
Method: [name()](method-name.md)
Method: [names()](method-names.md)
Method: [attrName()](method-attrname.md)
Method: [htmlClass()](method-htmlclass.md)
Method: [htmlClasses()](method-htmlclasses.md)
Method: [fieldName()](method-fieldname.md)
Method: [fieldSubfield()](method-fieldsubfield.md)
Method: [pageName()](method-pagename.md)
Method: [pageNameTranslate()](method-pagenametranslate.md)
Method: [pageNameUTF8()](method-pagenameutf8.md)
Method: [punyDecodeName()](method-punydecodename.md)
Method: [punyEncodeName()](method-punyencodename.md)
Method: [getPunycodeVersion()](method-getpunycodeversion.md)
Method: [punycode()](method-punycode.md)
Method: [filename()](method-filename.md)
Method: [path()](method-path.md)
Method: [pagePathName()](method-pagepathname.md)
Method: [pagePathNameUTF8()](method-pagepathnameutf8.md)
Method: [alpha()](method-alpha.md)
Method: [alphanumeric()](method-alphanumeric.md)
Method: [digits()](method-digits.md)
Method: [email()](method-email.md)
Method: [emailHeader()](method-emailheader.md)
Method: [word()](method-word.md)
Method: [words()](method-words.md)
Method: [text()](method-text.md)
Method: [textarea()](method-textarea.md)
Method: [line()](method-line.md)
Method: [lines()](method-lines.md)
Method: [markupToText()](method-markuptotext.md)
Method: [markupToLine()](method-markuptoline.md)
Method: [url()](method-url.md)
Method: [httpUrl()](method-httpurl.md)
Method: [filterValidateURL()](method-filtervalidateurl.md)
Method: [selectorValue()](method-selectorvalue.md)
Method: [selectorValueAdvanced()](method-selectorvalueadvanced.md)
Method: [selectorValueArray()](method-selectorvaluearray.md)
Method: [selectorValueV2()](method-selectorvaluev2.md)
Method: [selectorValueV1()](method-selectorvaluev1.md)
Method: [entities()](method-entities.md)
Method: [entities1()](method-entities1.md)
Method: [entitiesA()](method-entitiesa.md)
Method: [entitiesA1()](method-entitiesa1.md)
Method: [entitiesMarkdown()](method-entitiesmarkdown.md)
Method: [bracketTagsToHtml()](method-brackettagstohtml.md)
Method: [unentities()](method-unentities.md)
Method: [purify()](method-purify.md)
Method: [purifier()](method-purifier.md)
Method: [removeNewlines()](method-removenewlines.md)
Method: [removeWhitespace()](method-removewhitespace.md)
Method: [trim()](method-trim.md)
Method: [truncate()](method-truncate.md)
Method: [trunc()](method-trunc.md)
Method: [removeMB4()](method-removemb4.md)
Method: [hyphenCase()](method-hyphencase.md)
Method: [kebabCase()](method-kebabcase.md)
Method: [snakeCase()](method-snakecase.md)
Method: [camelCase()](method-camelcase.md)
Method: [pascalCase()](method-pascalcase.md)
Method: [chars()](method-chars.md)
Method: [string()](method-string.md)
Method: [date()](method-date.md)
Method: [textdomain()](method-textdomain.md)
Method: [match()](method-match.md)
Method: [int()](method-int.md)
Method: [int()](method-int.md)
Method: [intUnsigned()](method-intunsigned.md)
Method: [intSigned()](method-intsigned.md)
Method: [range()](method-range.md)
Method: [min()](method-min.md)
Method: [max()](method-max.md)
Method: [float()](method-float.md)
Method: [array()](method-___array.md) (hookable)
Method: [array()](method-___array.md) (hookable)
Method: [arrayVal()](method-arrayval.md)
Method: [intArray()](method-intarray.md)
Method: [intArrayVal()](method-intarrayval.md)
Method: [minArray()](method-minarray.md)
Method: [flatArray()](method-flatarray.md)
Method: [wordsArray()](method-wordsarray.md)
Method: [wordsArrayNumberReplacements()](method-wordsarraynumberreplacements.md)
Method: [option()](method-option.md)
Method: [options()](method-options.md)
Method: [bool()](method-bool.md)
Method: [bool()](method-bool.md)
Method: [bit()](method-bit.md)
Method: [checkbox()](method-checkbox.md)
Method: [maxLength()](method-maxlength.md)
Method: [minLength()](method-minlength.md)
Method: [maxBytes()](method-maxbytes.md)
Method: [testAll()](method-___testall.md) (hookable)
Method: [getAll()](method-getall.md)
Method: [getTextTools()](method-gettexttools.md)
Method: [getNumberTools()](method-getnumbertools.md)
Method: [validateFile()](method-validatefile.md)
Method: [validateFile()](method-validatefile.md)
Method: [__toString()](method-__tostring.md)
Method: [sanitize()](method-sanitize.md)
Method: [validate()](method-validate.md)
Method: [valid()](method-valid.md)

Constants:
Const: [translate](const-translate.md)
