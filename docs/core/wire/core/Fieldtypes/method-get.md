# Fieldtypes::get()

Source: `wire/core/Fieldtypes.php`

Given a Fieldtype name (or class name) return the instantiated Fieldtype module.

If the requested Fieldtype is not already installed, it will be installed here automatically.

@param string $key Fieldtype name or class name, or dynamic property of Fieldtypes

@return Fieldtype|null
