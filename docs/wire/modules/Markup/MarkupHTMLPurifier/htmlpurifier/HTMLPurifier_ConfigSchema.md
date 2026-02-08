# HTMLPurifier_ConfigSchema

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Configuration definition, defines directives and their defaults.

## instance()

Retrieves an instance of the application-wide configuration definition.
@param HTMLPurifier_ConfigSchema $prototype
@return HTMLPurifier_ConfigSchema

## add()

Defines a directive for configuration
@warning Will fail of directive's namespace is defined.
@warning This method's signature is slightly different from the legacy
         define() static method! Beware!
@param string $key Name of directive
@param mixed $default Default value of directive
@param string $type Allowed type of the directive. See
     HTMLPurifier_VarParser::$types for allowed values
@param bool $allow_null Whether or not to allow null values

## addValueAliases()

Defines a directive value alias.

Directive value aliases are convenient for developers because it lets
them set a directive to several values and get the same result.
@param string $key Name of Directive
@param array $aliases Hash of aliased values to the real alias

## addAllowedValues()

Defines a set of allowed values for a directive.
@warning This is slightly different from the corresponding static
         method definition.
@param string $key Name of directive
@param array $allowed Lookup array of allowed values

## addAlias()

Defines a directive alias for backwards compatibility
@param string $key Directive that will be aliased
@param string $new_key Directive that the alias will be to

## postProcess()

Replaces any stdClass that only has the type property with type integer.
