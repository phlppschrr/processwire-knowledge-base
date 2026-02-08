# HTMLPurifier_Config

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Configuration object that triggers customizable behavior.

@warning This class is strongly defined: that means that the class
         will fail if an undefined directive is retrieved or set.

@note Many classes that could (although many times don't) use the
      configuration object make it a mandatory parameter.  This is
      because a configuration object should always be forwarded,
      otherwise, you run the risk of missing a parameter and then
      being stumped when a configuration directive doesn't work.

@todo Reconsider some of the public member variables

## create()

Convenience constructor that creates a config object based on a mixed var
@param mixed $config Variable that defines the state of the config
                     object. Can be: a HTMLPurifier_Config() object,
                     an array of directives based on loadArray(),
                     or a string filename of an ini file.
@param HTMLPurifier_ConfigSchema $schema Schema object
@return HTMLPurifier_Config Configured object

## inherit()

Creates a new config object that inherits from a previous one.
@param HTMLPurifier_Config $config Configuration object to inherit from.
@return HTMLPurifier_Config object with $config as its parent.

## createDefault()

Convenience constructor that creates a default configuration object.
@return HTMLPurifier_Config default object.

## get()

Retrieves a value from the configuration.

@param string $key String key
@param mixed $a

@return mixed

## getBatch()

Retrieves an array of directives to values from a given namespace

@param string $namespace String namespace

@return array

## getBatchSerial()

Returns a SHA-1 signature of a segment of the configuration object
that uniquely identifies that particular configuration

@param string $namespace Namespace to get serial for

@return string
@note Revision is handled specially and is removed from the batch
      before processing!

## getSerial()

Returns a SHA-1 signature for the entire configuration object
that uniquely identifies that particular configuration

@return string

## getAll()

Retrieves all directives, organized by namespace

@warning This is a pretty inefficient function, avoid if you can

## set()

Sets a value to configuration.

@param string $key key
@param mixed $value value
@param mixed $a

## _listify()

Convenience function for error reporting

@param array $lookup

@return string

## getHTMLDefinition()

Retrieves object reference to the HTML definition.

@param bool $raw Return a copy that has not been setup yet. Must be
            called before it's been setup, otherwise won't work.
@param bool $optimized If true, this method may return null, to
            indicate that a cached version of the modified
            definition object is available and no further edits
            are necessary.  Consider using
            maybeGetRawHTMLDefinition, which is more explicitly
            named, instead.

@return HTMLPurifier_HTMLDefinition|null

## getCSSDefinition()

Retrieves object reference to the CSS definition

@param bool $raw Return a copy that has not been setup yet. Must be
            called before it's been setup, otherwise won't work.
@param bool $optimized If true, this method may return null, to
            indicate that a cached version of the modified
            definition object is available and no further edits
            are necessary.  Consider using
            maybeGetRawCSSDefinition, which is more explicitly
            named, instead.

@return HTMLPurifier_CSSDefinition|null

## getURIDefinition()

Retrieves object reference to the URI definition

@param bool $raw Return a copy that has not been setup yet. Must be
            called before it's been setup, otherwise won't work.
@param bool $optimized If true, this method may return null, to
            indicate that a cached version of the modified
            definition object is available and no further edits
            are necessary.  Consider using
            maybeGetRawURIDefinition, which is more explicitly
            named, instead.

@return HTMLPurifier_URIDefinition|null

## getDefinition()

Retrieves a definition

@param string $type Type of definition: HTML, CSS, etc
@param bool $raw Whether or not definition should be returned raw
@param bool $optimized Only has an effect when $raw is true.  Whether
       or not to return null if the result is already present in
       the cache.  This is off by default for backwards
       compatibility reasons, but you need to do things this
       way in order to ensure that caching is done properly.
       Check out enduser-customize.html for more details.
       We probably won't ever change this default, as much as the
       maybe semantics is the "right thing to do."

@throws HTMLPurifier_Exception
@return HTMLPurifier_Definition|null

## initDefinition()

Initialise definition

@param string $type What type of definition to create

@return HTMLPurifier_CSSDefinition|HTMLPurifier_HTMLDefinition|HTMLPurifier_URIDefinition
@throws HTMLPurifier_Exception

## maybeGetRawHTMLDefinition()

@return HTMLPurifier_HTMLDefinition|null

## maybeGetRawCSSDefinition()

@return HTMLPurifier_CSSDefinition|null

## maybeGetRawURIDefinition()

@return HTMLPurifier_URIDefinition|null

## loadArray()

Loads configuration values from an array with the following structure:
Namespace.Directive => Value

@param array $config_array Configuration associative array

## getAllowedDirectivesForForm()

Returns a list of array(namespace, directive) for all directives
that are allowed in a web-form context as per an allowed
namespaces/directives list.

@param array $allowed List of allowed namespaces/directives
@param HTMLPurifier_ConfigSchema $schema Schema to use, if not global copy

@return array

## loadArrayFromForm()

Loads configuration values from $_GET/$_POST that were posted
via ConfigForm

@param array $array $_GET or $_POST array to import
@param string|bool $index Index/name that the config variables are in
@param array|bool $allowed List of allowed namespaces/directives
@param bool $mq_fix Boolean whether or not to enable magic quotes fix
@param HTMLPurifier_ConfigSchema $schema Schema to use, if not global copy

@return mixed

## mergeArrayFromForm()

Merges in configuration values from $_GET/$_POST to object. NOT STATIC.

@param array $array $_GET or $_POST array to import
@param string|bool $index Index/name that the config variables are in
@param array|bool $allowed List of allowed namespaces/directives
@param bool $mq_fix Boolean whether or not to enable magic quotes fix

## prepareArrayFromForm()

Prepares an array from a form into something usable for the more
strict parts of HTMLPurifier_Config

@param array $array $_GET or $_POST array to import
@param string|bool $index Index/name that the config variables are in
@param array|bool $allowed List of allowed namespaces/directives
@param bool $mq_fix Boolean whether or not to enable magic quotes fix
@param HTMLPurifier_ConfigSchema $schema Schema to use, if not global copy

@return array

## loadIni()

Loads configuration values from an ini file

@param string $filename Name of ini file

## isFinalized()

Checks whether or not the configuration object is finalized.

@param string|bool $error String error message, or false for no error

@return bool

## autoFinalize()

Finalizes configuration only if auto finalize is on and not
already finalized

## finalize()

Finalizes a configuration object, prohibiting further change

## triggerError()

Produces a nicely formatted error message by supplying the
stack frame information OUTSIDE of HTMLPurifier_Config.

@param string $msg An error message
@param int $no An error number

## serialize()

Returns a serialized form of the configuration object that can
be reconstituted.

@return string
