# Functions

Source: `wire/core/Functions.php`

ProcessWire Functions

Common API functions useful outside of class scope

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

These shortcuts for creating WireArray types are available in ProcessWire 3.0.123 and newer.
These file system functions are procedural versions of some of those provided by the `$files` API variable.

## wire()

Return an API variable, or return current ProcessWire instance if given no arguments

- Call `wire()` with no arguments returns the current ProcessWire instance.
- Call `wire('var')` to return the API variable represented by 'var', or null if not present.
- Call `wire('all')` or `wire('*')` to return an iterable object of all API variables.
- Call `wire($object)` to attach $object to the current instance ($object must be Wire-derived object).


@param string $name If omitted, returns current ProcessWire instance.

@return null|ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|string|mixed Requested API variable or null if it does not exist

## wireInstance()

Get or set the current ProcessWire instance


@param Wire|null $wire To set specify ProcessWire instance or any Wire-derived object in it, or omit to get current instance.

@return ProcessWire

@since 3.0.125

## wireMkdir()

Create a directory (optionally recursively) that is writable to ProcessWire and uses the $config chmod settings

This is procedural version of the `$files->mkdir()` method.


@param string $path

@param bool $recursive If set to true, all directories will be created as needed to reach the end.

@param string $chmod Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755"
	If omitted, then ProcessWire’s $config->chmodDir setting is used instead.

@return bool

@see WireFileTools::mkdir()

## wireRmdir()

Remove a directory (optionally recursively)

This is procedural version of the `$files->rmdir()` method. See that method for more options.


@param string $path

@param bool $recursive If set to true, all files and directories in $path will be recursively removed as well.

@return bool

@see WireFileTools::rmdir()

## wireChmod()

Change the mode of a file or directory (optionally recursive)

If no `$chmod` mode argument is specified the `$config->chmodFile` or $config->chmodDir` settings will be used.

This is procedural version of the `$files->chmod()` method.


@param string $path May be a directory or a filename

@param bool $recursive If set to true, all files and directories in $path will be recursively set as well.

@param string $chmod If you want to set the mode to something other than PW's chmodFile/chmodDir settings,
  you may override it by specifying it here. Ignored otherwise. Format should be a string, like "0755".

@return bool Returns true if all changes were successful, or false if at least one chmod failed.

@throws WireException when it receives incorrect chmod format

@see WireFileTools::chmod()

## wireCopy()

Copy all files recursively from one directory to another

This is procedural version of the `$files->copy()` method.


@param string $src Path to copy files from

@param string $dst Path to copy files to. Directory is created if it doesn’t already exist.

@param bool|array Array of options:
	- `recursive` (bool): Whether to copy directories within recursively. (default=true)
	- `allowEmptyDirs` (bool): Copy directories even if they are empty? (default=true)
	- If a boolean is specified for $options, it is assumed to be the 'recursive' option.

@return bool True on success, false on failure.

@see WireFileTools::copy()

## wireUnzipFile()

Unzips the given ZIP file to the destination directory

This is procedural version of the `$files->unzip()` method. See that method for more details.


@param string $file ZIP file to extract

@param string $dst Directory where files should be unzipped into. Directory is created if it doesn’t exist.

@param array $options See `WireFileTools::unzip()` for options.

@return array Returns an array of filenames (excluding $dst) that were unzipped.

@throws WireException All error conditions result in WireException being thrown.

@see WireFileTools::unzip()

## wireZipFile()

Create a ZIP file from given files

This is procedural version of the `$files->zip()` method. See that method for all options.


@param string $zipfile Full path and filename to create or update (i.e. /path/to/myfile.zip)

@param array|string $files Array of files to add (full path and filename), or directory (string) to add.
	If given a directory, it will recursively add everything in that directory.

@param array $options Options modify default behavior:
	- `allowHidden` (bool|array): allow hidden files? May be boolean, or array of hidden files (basenames) you allow. (default=false)
		Note that if you actually specify a hidden file in your $files argument, then that overrides this.
	- `allowEmptyDirs` (bool): allow empty directories in the ZIP file? (default=true)
	- `overwrite` (bool): Replaces ZIP file if already present (rather than adding to it) (default=false)
	- `exclude` (array): Files or directories to exclude
	- `dir` (string): Directory name to prepend to added files in the ZIP

@return array Returns associative array of:
	- `files` (array): all files that were added
	- `errors` (array): files that failed to add, if any

@throws WireException Original ZIP file creation error conditions result in WireException being thrown.

@see WireFileTools::zip()

## wireSendFile()

Send the contents of the given filename via http

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a WireException if the file can’t be sent for some reason.

This is procedural version of the `$files->send()` method. See that method for all options.


@param string $filename Full path and filename to send

@param array $options Optional options that you may pass in (see `WireHttp::sendFile()` for details)

@param array $headers Optional headers that are sent (see `WireHttp::sendFile()` for details)

@throws WireException

@see WireHttp::sendFile(), WireFileTools::send()

## wireRelativeTimeStr()

Given a unix timestamp (or date string), returns a formatted string indicating the time relative to now

Examples: “1 day ago”, “30 seconds ago”, “just now”, etc.

This is the procedural version of `$datetime->relativeTimeStr()`.

Based upon: http://www.php.net/manual/en/function.time.php#89415


@param int|string $ts Unix timestamp or date string

@param bool|int|array $abbreviate Whether to use abbreviations for shorter strings.
	- Specify boolean TRUE for abbreviations (abbreviated where common, not always different from non-abbreviated)
	- Specify integer 1 for extra short abbreviations (all terms abbreviated into shortest possible string)
	- Specify boolean FALSE or omit for no abbreviations.
	- Specify associative array of key=value pairs of terms to use for abbreviations. The possible keys are:
	  just now, ago, from now, never, second, minute, hour, day, week, month, year, decade, seconds, minutes,
   hours, days, weeks, months, years, decades

@param bool $useTense Whether to append a tense like “ago” or “from now”,
	May be ok to disable in situations where all times are assumed in future or past.
	In abbreviate=1 (shortest) mode, this removes the leading "+" or "-" from the string.

@return string

@see WireDateTime::relativeTimeStr()

## wireMail()

Send an email or get a WireMail object to populate before send

- Please note that the order of arguments is different from PHP’s mail() function.
- If no arguments are specified it simply returns a WireMail object (see #4 below).
- This is a procedural version of functions provided by the `$mail` API variable (see that for more options).
- This function will attempt to use an installed module that extends WireMail.
- If no other WireMail module is installed, the default `WireMail` (which uses PHP mail) will be used instead.

~~~~~~
// Default usage:
wireMail($to, $from, $subject, $body, $options);

// Specify body and/or bodyHTML in $options array (perhaps with other options):
$options = [ 'body' => $body, 'bodyHTML' => $bodyHTML ];
wireMail($to, $from, $subject, $options);

// Specify both $body and $bodyHTML as arguments, but no $options:
wireMail($to, $from, $subject, $body, $bodyHTML);

// Specify a blank call to wireMail() to get the WireMail sending object. This can
// be either WireMail() or a class descending from it. If a WireMail descending
// module is installed, it will be returned rather than WireMail():
$mail = wireMail();
$mail->to('user@domain.com')->from('you@company.com');
$mail->subject('Mail Subject')->body('Mail Body Text')->bodyHTML('Body HTML');
$numSent = $mail->send();


@param string|array $to Email address TO. For multiple, specify CSV string or array.

@param string $from Email address FROM. This may be an email address, or a combined name and email address.
	Example of combined name and email: `Karen Cramer <karen@processwire.com>`

@param string $subject Email subject

@param string|array $body Email body or omit to move straight to $options array

@param array|string $options Array of options OR the $bodyHTML string. Array $options are:
 - `bodyHTML` (string): Email body as HTML.
	- `body` (string): Email body as plain text. This is created automatically if you only provide $bodyHTML.
	- `headers` (array): Associative array of ['header name' => 'header value']
	- Any additional options you provide will be sent along to the WireMail module or class, in tact.

@return int|WireMail Returns number of messages sent or WireMail object if no arguments specified.

## wirePopulateStringTags()

Given a string ($str) and values ($vars), replace “{tags}” in the string with the values

- The `$vars` should be an associative array of `[ 'tag' => 'value' ]`.
- The `$vars` may also be an object, in which case values will be pulled as properties of the object.

By default, tags are specified in the format: {first_name} where first_name is the name of the
variable to pull from $vars, `{` is the opening tag character, and `}` is the closing tag char.

The tag parser can also handle subfields and OR tags, if `$vars` is an object that supports that.
For instance `{products.title}` is a subfield, and `{first_name|title|name}` is an OR tag.

~~~~~
$vars = [ 'foo' => 'FOO!', 'bar' => 'BAR!' ];
$str = 'This is a test: {foo}, and this is another test: {bar}';
echo wirePopulateStringTags($str, $vars);
// outputs: This is a test: FOO!, and this is another test: BAR!
~~~~~


@param string $str The string to operate on (where the {tags} might be found)

@param WireData|object|array $vars Object or associative array to pull replacement values from.

@param array $options Array of optional changes to default behavior, including:
	- `tagOpen` (string): The required opening tag character(s), default is '{'
	- `tagClose` (string): The optional closing tag character(s), default is '}'
	- `recursive` (bool): If replacement value contains tags, populate those too? (default=false)
	- `removeNullTags` (bool): If a tag resolves to a NULL, remove it? If false, tag will remain. (default=true)
	- `entityEncode` (bool): Entity encode the values pulled from $vars? (default=false)
	- `entityDecode` (bool): Entity decode the values pulled from $vars? (default=false)

@return string String with tags populated.

## wireTempDir()

Return a new temporary directory/path ready to use for files

- The directory will be automatically removed after a set period of time (default=120s).
- This is a procedural version of the `$files->tempDir()` method.

~~~~~
$td = wireTempDir('hello-world');
$path = (string) $td; // or use $td->get();
file_put_contents($path . 'some-file.txt', 'Hello world');
~~~~~


@param Object|string $name Provide the object that needs the temp dir, or name your own string

@param array|int $options Options array to modify default behavior:
 - `maxAge` (integer): Maximum age of temp dir files in seconds (default=120)
 - `basePath` (string): Base path where temp dirs should be created. Omit to use default (recommended).
 - Note: if you specify an integer for $options, then 'maxAge' is assumed.

@return WireTempDir If you typecast return value to a string, it is the temp dir path (with trailing slash).

@see WireFileTools::tempDir(), WireTempDir

## wireRenderFile()

Given a filename, render it as a ProcessWire template file

This is a shortcut to using the `TemplateFile` class, as well as the procedural version of `$files->render()`.

File is assumed relative to `/site/templates/` (or a directory within there) unless you specify a full path.
If you specify a full path, it will accept files in or below any of the following:

- /site/templates/
- /site/modules/
- /wire/modules/

Note this function returns the output to you, so that you can send the output wherever you want (delayed output).
For direct output, use the `wireIncludeFile()` or `$files->include()` function instead.


@param string $filename Assumed relative to /site/templates/ unless you provide a full path name with the filename.
 If you provide a path, it must resolve somewhere in site/templates/, site/modules/ or wire/modules/.

@param array $vars Optional associative array of variables to send to template file.
 Please note that all template files automatically receive all API variables already (you don't have to provide them).

@param array $options Associative array of options to modify behavior:
 - `defaultPath` (string): Path where files are assumed to be when only filename or relative filename is specified (default=/site/templates/)
 - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php)
 - `allowedPaths` (array): Array of paths that are allowed (default is templates, core modules and site modules)
 - `allowDotDot` (bool): Allow use of ".." in paths? (default=false)
 - `throwExceptions` (bool): Throw exceptions when fatal error occurs? (default=true)

@return string|bool Rendered template file or boolean false on fatal error (and throwExceptions disabled)

@throws WireException if template file doesn’t exist

@see wireIncludeFile(), WireFileTools::render(), WireFileTools::include()

## wireIncludeFile()

Include a PHP file passing it all API variables and optionally your own specified variables

This is the procedural version of the `$files->include()` method.

This is the same as PHP’s `include()` function except for the following:

- It receives all API variables and optionally your custom variables
- If your filename is not absolute, it doesn’t look in PHP’s include path, only in the current dir.
- It only allows including files that are part of the PW installation: templates, core modules or site modules
- It will assume a “.php” extension if filename has no extension.

Note this function produces direct output. To retrieve output as a return value, use the
`wireRenderFile()` or `$files->render()` function instead.


@param string $filename Filename to include

@param array $vars Optional variables you want to hand to the include (associative array)

@param array $options Array of options to modify behavior:
 - `func` (string): Function to use: include, include_once, require or require_once (default=include)
 - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php)
 - `allowedPaths` (array): Array of start paths include files are allowed from. Note current dir is always allowed.

@return bool Always returns true

@throws WireException if file doesn’t exist or is not allowed

@see wireRenderFile(), WireFileTools::include(), WireFileTools::render()

## wireDate()

Format a date, using PHP date(), strftime() or other special strings (see arguments).

This is designed to work the same wa as PHP’s `date()` but be able to accept any common format
used in ProcessWire. This is helpful in reducing code in places where you might have logic
determining when to use `date()`, `strftime()`, or `wireRelativeTimeStr()`.

This is the procedural version of the `$datetime->date()` method.

~~~~~
echo wireDate('Y-m-d H:i:s'); // Outputs: 2019-01-20 06:48:11
echo wireDate('relative', '2019-01-20 06:00'); // Outputs: 48 minutes ago
~~~~~


@param string|int $format Use any PHP date() or strftime() format, or one of the following:
	- `relative` for a relative date/time string.
 - `relative-` for a relative date/time string with no tense.
	- `rel` for an abbreviated relative date/time string.
	- `rel-` for an abbreviated relative date/time string with no tense.
	- `r` for an extra-abbreviated relative date/time string.
	- `r-` for an extra-abbreviated relative date/time string with no tense.
	- `ts` makes it return a unix timestamp.
	- Specify blank string to make it use the system date format ($config->dateFormat) .
	- If given an integer and no second argument specified, it is assumed to be the second ($ts) argument.

@param int|string|null $ts Optionally specify the date/time stamp or strtotime() compatible string. If not specified, current time is used.

@return string|bool Formatted date/time, or boolean false on failure

## wireIconMarkup()

Render markup for a system icon

It is NOT necessary to specify an icon prefix like “fa-” with the icon name.

Modifiers recognized in the class attribute:
lg, fw, 2x, 3x, 4x, 5x, spin, spinner, li, border, inverse,
rotate-90, rotate-180, rotate-270, flip-horizontal, flip-vertical,
stack, stack-1x, stack-2x

~~~~~
// Outputs: "<i class='fa fa-home'></i>"
echo wireIconMarkup('home');

// Outputs: "<i class='fa fa-home fa-fw fa-lg my-class'></i>"
echo wireIconMarkup('home', 'fw lg my-class');

// Outputs "<i class='fa fa-home fa-fw' id='root-icon'></i>" (3.0.229+ only)
echo wireIconMarkup('home', 'fw id=root-icon');
echo wireIconMarkup('home fw id=root-icon'); // same as above
~~~~~


@param string $icon Icon name (currently a font-awesome icon name)

@param string $class Any of the following:
 - Additional attributes for class (example: "fw" for fixed width)
 - Your own custom class(es) separated by spaces
 - Any additional attributes in format `key="val" key='val' or key=val` string (3.0.229+)
 - An optional trailing space to append an `&nbsp;` to the return icon markup (3.0.229+)
 - Any of the above may also be specified in the $icon argument in 3.0.229+.

@return string

## wireIconMarkupFile()

Get the markup or class name for an icon that can represent the given filename

~~~~~
// Outputs: "<i class='fa fa-pdf-o'></i>"
echo wireIconMarkupFile('file.pdf');
~~~~~


@param string $filename Can be any type of filename (with or without path).

@param string|bool $class Additional class attributes, i.e. "fw" for fixed-width (optional).
	Or specify boolean TRUE to get just the icon class name (no markup).

@return string

## wireBytesStr()

Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB


@param int $bytes Quantity in bytes

@param bool|int|array $small Make returned string as small as possible? (default=false)
 - `true` (bool): Yes, make returned string as small as possible.
 - `1` (int): Same as `true` but with space between number and unit label.
 - Or optionally specify the $options argument here if you do not need the $small argument.

@param array|int $options Options to modify default behavior, or if an integer then `decimals` option is assumed:
 - `decimals` (int|null): Number of decimals to use in returned value or NULL for auto (default=null).
    When null (auto) a decimal value of 1 is used when appropriate, for megabytes and higher (3.0.214+).
 - `decimal_point` (string|null): Decimal point character, or null to detect from locale (default=null).
 - `thousands_sep` (string|null): Thousands separator, or null to detect from locale (default=null).
 - `small` (bool): If no $small argument was specified, you can optionally specify it in this $options array.
 - `type` (string): To force return value as specific type, specify one of: bytes, kilobytes, megabytes,
    gigabytes, terabytes; or just: b, k, m, g, t. (3.0.148+ only, terabytes 3.0.214+).

@return string

## wireClassName()

Normalize a class name with or without namespace, or get namespace of class

Default behavior is to return class name without namespace.


@param string|object $className Class name or object instance

@param bool|int|string $withNamespace Should return value include namespace? (default=false)
 - `false` (bool): Return only class name without namespace (default).
 - `true` (bool): Yes include namespace in returned value.
 - `1` (int): Return only namespace (i.e. “ProcessWire”, with no backslashes unless $verbose argument is true)

@param bool $verbose When namespace argument is true or 1, use verbose return value (added 3.0.143). This does the following:
 - If returning class name with namespace, this makes it include a leading backslash, i.e. `\ProcessWire\Wire`
 - If returning namespace only, adds leading backslash, plus trailing backslash if namespace is not root, i.e. `\ProcessWire\`

@return string|null Returns string or NULL if namespace-only requested and unable to determine

## wireClassNamespace()

Get namespace for given class

~~~~~
echo wireClassNamespace('Page'); // returns: "\ProcessWire\"
echo wireClassNamespace('DirectoryIterator'); // returns: "\"
echo wireClassNamespace('UnknownClass'); // returns "" (blank)

// Specify true for 2nd argument to make it include class name
echo wireClassNamespace('Page', true); // outputs: \ProcessWire\Page

// Specify true for 3rd argument to find all matching classes
// and return array if more than 1 matches (or string if just 1):
$val = wireClassNamespace('Foo', true, true);
if(is_array($val)) {
  // 2+ classes found, so array value is returned
  // $val: [ '\Bar\Foo', '\Foo', '\Baz\Foo' ]
} else {
  // string value is returned when only one class matches
  // $val: '\Bar\Foo'
}
~~~~~


@param string|object $className

@param bool $withClass Include class name in returned namespace? (default=false)

@param bool $strict Return array of namespaces if multiple match? (default=false)

@return string|array Returns one of the following:
 - String of `\Namespace\` (leading+trailing backslashes) if namespace found.
 - String of `\` if class in root namespace.
 - Blank string if unable to find namespace for class.
 - Array of namespaces only if $strict option is true AND multiple namespaces were found for class.
 - If the $withClass option is true, then return value(s) have class, i.e. `\Namespace\ClassName`.

@since 3.0.150

## wireClassExists()

Does the given class name exist?

ProcessWire namespace aware version of PHP’s class_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.


@param string $className

@param bool $autoload

@return bool

## wireMethodExists()

Does the given class have the given method?

ProcessWire namespace aware version of PHP’s method_exists() function

If given a class name that does not include a namespace, the `\ProcessWire` namespace is assumed.


@param string $className Class name or object

@param string $method Method name

@param bool $hookable Also return true if "method" exists in a hookable format "___method"? (default=false) 3.0.204+

@return bool

## wireClassImplements()

Get an array of all the interfaces that the given class implements

- ProcessWire namespace aware version of PHP’s class_implements() function.
- Return value has array keys as class name with namespace and array values as class name without namespace.


@param string|object $className

@param bool $autoload

@return array

## wireClassParents()

Return array of all parent classes for given class/object

ProcessWire namespace aware version of PHP’s class_parents() function

Returns associative array where array keys are full namespaced class name, and
values are the non-namespaced classname.


@param string|object $className

@param bool $autoload

@return array

## wireInstanceOf()

Does given instance (or class) represent an instance of the given className (or class names)?

Since version 3.0.108 the $className argument may also represent an interface,
array of interfaces, or mixed array of interfaces and class names. Previous versions did
not support interfaces unless the $instance argument was an object.


@param object|string $instance Object instance to test (or string of its class name).

@param string|array $className Class/interface name or array of class/interface names to test against.

@param bool $autoload Allow PHP to autoload the class? (default=true)

@return bool|string Returns one of the following:
 - `false` (bool): if not an instance (whether $className argument is string or array).
 - `true` (bool): if given a single $className (string) and $instance is an instance of it.
 - `ClassName` (string): first matching class/interface name if $className was an array of classes to test.

## wireIsCallable()

Is the given $var callable as a function?

ProcessWire namespace aware version of PHP’s is_callable() function


@param string|callable $var

@param bool $syntaxOnly

@var string $callableName

@return bool

## wireCount()

Return the count of item(s) present in the given value

Duplicates behavior of PHP count() function prior to PHP 7.2, which states:

> Returns the number of elements in $value. When the parameter is neither an array nor an
object with implemented Countable interface, 1 will be returned. There is one exception,
if $value is NULL, 0 will be returned.


@param mixed $value

@return int

## wireLength()

Returns string length of any type (string, array, object, bool, int, etc.)

- If given a string it returns the multibyte string length.
- If given a bool, returns 1 for true or 0 for false.
- If given an int or float, returns its length when typecast to string.
- If given array or object it duplicates the behavior of `wireCount()`.
- If given null returns 0.

@param string|array|object|int|bool|null $value

@param bool $mb Use multibyte string length when available (default=true)

@return int

@since 3.0.192

## wireLen()

Returns string byte length of any type (string, array, object, bool, int, etc.)

This is identical to the `wireLength()` function except that it does not use
multibyte string lengths on strings, so it returns a byte length when given
a multibyte string rather than a visual character length. So on strings
it uses strlen() rather than mb_strlen().

@param string|array|object|int|bool|null $value

@return int

@since 3.0.192

## wireEmpty()

Is the given value empty according to ProcessWire standards?

This works the same as PHP’s empty() function except for the following:

- It returns true for Countable objects that have 0 items.
- It considers whitespace-only strings to be empty.
- It considers WireNull objects (like NullPage or any others) to be empty (3.0.149+).
- It uses the string value of objects that can be typecast strings (3.0.150+).
- You cannot pass it an undefined variable without triggering a PHP warning.

~~~~~
// behavior with Countable objects
$a = new WireArray();
empty($a); // PHP’s function returns false
wireEmpty($a); // PW’s function returns true
$a->add('item');
wireEmpty($a); // returns false, since there is now an item

// behavior with whitespace-only string
$s = '  ';
empty($s); // PHP’s function returns false
wireEmpty($s); // PW’s function returns true

// behavior with undefined variable $v
isset($v); // returns false
empty($v); // returns true
wireEmpty($v); // returns true but with PHP’s warning triggered
~~~~~

@param mixed $value Value to test if empty

@return bool

@since 3.0.143

## wire404()

Stop execution with a 404 unless redirect URL available (for front-end use)

This is an alternative to using a manual `throw new Wire404Exception()` and is recognized by
PW as a front-end 404 where PagePathHistory (or potentially other modules) are still allowed
to change the behavior of the request from a 404 to something else (like a 301 redirect).


@param string $message Optional message to send to Exception message argument (not used in output by default)

@throws Wire404Exception

@since 3.0.146

## WireArray()

Create new WireArray, add given $items to it, and return it

This is the same as creating a `new WireArray()` and then adding items to it with separate `add()` calls,
except that this function enables you to do it all in one shot.

~~~~~~
$a = WireArray(); // create empty WireArray
$a = WireArray('foo'); // create WireArray with one "foo" string
$a = WireArray(['foo', 'bar', 'baz']); // create WireArray with 3 strings
~~~~~~


@param array|WireArray|mixed $items

@return WireArray

@since 3.0.123

## WireData()

Create a new WireData instance and optionally add given associative array of data to it

~~~~~
$data = WireData([ 'hello' => 'world', 'foo' => 'bar' ]);
~~~~~


@param array|\Traversable $data Can be an associative array or Traversable object of data to set, or omit if not needed

@return WireData

@since 3.0.126

## PageArray()

Create new PageArray, add given $items (pages) to it, and return it

This is the same as creating a `new PageArray()` and then adding items to it with separate `add()` calls,
except that this function enables you to do it all in one shot.

~~~~~
$a = PageArray(); // create empty PageArray
$a = PageArray($page); // create PageArray with one page
$a = PageArray([ $page1, $page2, $page3 ]); // create PageArray with multiple items
~~~~~


@param array|PageArray $items

@return PageArray

@since 3.0.123
