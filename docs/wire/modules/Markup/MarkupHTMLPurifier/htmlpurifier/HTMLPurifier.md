# HTMLPurifier

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Facade that coordinates HTML Purifier's subsystems in order to purify HTML.

@note There are several points in which configuration can be specified
      for HTML Purifier.  The precedence of these (from lowest to
      highest) is as follows:
         -# Instance: new HTMLPurifier($config)
         -# Invocation: purify($html, $config)
      These configurations are entirely independent of each other and
      are *not* merged (this behavior may change in the future).

@todo We need an easier way to inject strategies using the configuration
      object.

## addFilter()

Adds a filter to process the output. First come first serve

@param HTMLPurifier_Filter $filter HTMLPurifier_Filter object

## purify()

Filters an HTML snippet/document to be XSS-free and standards-compliant.

@param string $html String of HTML to purify
@param HTMLPurifier_Config $config Config object for this operation,
               if omitted, defaults to the config object specified during this
               object's construction. The parameter can also be any type
               that HTMLPurifier_Config::create() supports.

@return string Purified HTML

## purifyArray()

Filters an array of HTML snippets

@param string[] $array_of_html Array of html snippets
@param HTMLPurifier_Config $config Optional config object for this operation.
               See HTMLPurifier::purify() for more details.

@return string[] Array of purified HTML

## instance()

Singleton for enforcing just one HTML Purifier in your system

@param HTMLPurifier|HTMLPurifier_Config $prototype Optional prototype
                  HTMLPurifier instance to overload singleton with,
                  or HTMLPurifier_Config instance to configure the
                  generated version with.

@return HTMLPurifier

## getInstance()

Singleton for enforcing just one HTML Purifier in your system

@param HTMLPurifier|HTMLPurifier_Config $prototype Optional prototype
                  HTMLPurifier instance to overload singleton with,
                  or HTMLPurifier_Config instance to configure the
                  generated version with.

@return HTMLPurifier
@note Backwards compatibility, see instance()
