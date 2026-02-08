# Sanitizer::selectorValueAdvanced()

Source: `wire/core/Sanitizer.php`

Sanitize selector value for advanced text search operator (#=)

The [advanced text search operator](https://processwire.com/docs/selectors/operators/#contains-advanced)
`#=` supports some characters that are typically excluded from selector values, so this method enables
you to prepare a selector value for use with it. This method should not be used for sanitizing any other
kinds of selector values.

Characters that have meaning to the advanced text search operator include `+-*()"` and thus their
appearance in the `$value` argument is assumed to be a command rather than text to search for. Though
note that non-matching double quotes or parenthesis are removed.

*Note: If double quotes are used in your selector value, this method will convert them to matching
parenthesis, i.e. `+"phrase"` gets converted to `+(phrase)`.*


@param string|array $value

@param array $options See options for Sanitizer::selectorValue() method

@return bool|mixed|string

@since 3.0.182

@see Sanitizer::selectorValue()

@see https://processwire.com/docs/selectors/operators/#contains-advanced
