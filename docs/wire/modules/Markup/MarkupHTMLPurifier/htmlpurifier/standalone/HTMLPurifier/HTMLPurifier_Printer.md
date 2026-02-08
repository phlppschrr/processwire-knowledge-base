# HTMLPurifier_Printer

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/Printer.php`


## __construct()

For HTML generation convenience funcs.
@type HTMLPurifier_Generator
/
protected $generator;

/**
For easy access.
@type HTMLPurifier_Config
/
protected $config;

/**
Initialize $generator.

## prepareGenerator()

Give generator necessary configuration if possible
@param HTMLPurifier_Config $config

## start()

Main function that renders object or aspect of that object
@note Parameters vary depending on printer
/
// function render() {}

/**
Returns a start tag
@param string $tag Tag name
@param array $attr Attribute array
@return string

## end()

Returns an end tag
@param string $tag Tag name
@return string

## element()

Prints a complete element with content inside
@param string $tag Tag name
@param string $contents Element contents
@param array $attr Tag attributes
@param bool $escape whether or not to escape contents
@return string

## elementEmpty()

@param string $tag
@param array $attr
@return string

## text()

@param string $text
@return string

## row()

Prints a simple key/value row in a table.
@param string $name Key
@param mixed $value Value
@return string

## escape()

Escapes a string for HTML output.
@param string $string String to escape
@return string

## listify()

Takes a list of strings and turns them into a single list
@param string[] $array List of strings
@param bool $polite Bool whether or not to add an end before the last
@return string

## getClass()

Retrieves the class of an object without prefixes, as well as metadata
@param object $obj Object to determine class of
@param string $sec_prefix Further prefix to remove
@return string
