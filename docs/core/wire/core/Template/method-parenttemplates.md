# Template::parentTemplates()

Source: `wire/core/Template.php`

Get or set parent templates (templates allowed for parent pages of pages using this template)

- May be specified as template IDs or names in an array, or Template objects in a TemplatesArray.
- To allow any template as parent, specify a blank array.
- To disallow any parents (other than what’s already in use) set the `$template->noParents` property to 1.


@param array|TemplatesArray|null $setValue Specify only when setting, an iterable value containing Template objects, IDs or names

@return TemplatesArray

@since 3.0.153
