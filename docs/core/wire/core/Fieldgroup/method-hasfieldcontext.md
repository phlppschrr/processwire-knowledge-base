# Fieldgroup::hasFieldContext()

Source: `wire/core/Fieldgroup.php`

Does the given Field have context data available in this fieldgroup?

A Field with context data is one that overrides one or more settings present with the Field
when it is outside the context of this Fieldgroup. For example, perhaps a Field has a
columnWidth setting of 100% in its global settings, but only 50% when used in this Fieldgroup.


@param int|string|Field $field Field object, name or id

@param string $namespace Optional namespace string for context

@return bool True if additional context information is available, false if not.
