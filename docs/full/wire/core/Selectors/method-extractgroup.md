# Selectors::extractGroup()

Source: `wire/core/Selectors.php`

Given a string like name@field=... or @field=... extract the part that comes before the @

This part indicates the group name, which may also be blank to indicate grouping with other blank grouped items

@param string $str

@return null|string
