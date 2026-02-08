# Template::childTemplates()

Source: `wire/core/Template.php`

Get or set child templates (templates allowed for children of pages using this template)

- May be specified as template IDs or names in an array, or Template objects in a TemplatesArray.
- To allow any template to be used for children, specify a blank array.
- To disallow any children (other than what’s already in use) set the `$template->noChildren` property to 1.


@param array|TemplatesArray|null $setValue Specify only when setting, an iterable value containing Template objects, IDs or names

@return TemplatesArray|Template[]

@since 3.0.153
