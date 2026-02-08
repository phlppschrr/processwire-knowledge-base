# FunctionsAPI::templates()

Source: `wire/core/FunctionsAPI.php`

Get or save templates ($templates API variable as a function)

This function behaves the same as the `$templates` API variable, though does support
an optional shortcut argument for getting a single template.

~~~~~~
$t = templates()->get('basic-page'); // regular syntax
$t = templates('basic-page'); // shortcut syntax
~~~~~~


@param string $name Optional template to retrieve

@return Templates|Template|null

@see Templates
