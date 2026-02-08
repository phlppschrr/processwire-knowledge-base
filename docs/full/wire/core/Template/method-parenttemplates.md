# $template->parentTemplates($setValue = null): TemplatesArray

Source: `wire/core/Template.php`

Get or set parent templates (templates allowed for parent pages of pages using this template)

- May be specified as template IDs or names in an array, or Template objects in a TemplatesArray.
- To allow any template as parent, specify a blank array.
- To disallow any parents (other than what’s already in use) set the `$template->noParents` property to 1.

## Usage

~~~~~
// basic usage
$templatesArray = $template->parentTemplates();

// usage with all arguments
$templatesArray = $template->parentTemplates($setValue = null);
~~~~~

## Arguments

- `$setValue` (optional) `array|TemplatesArray|null` Specify only when setting, an iterable value containing Template objects, IDs or names

## Return value

- `TemplatesArray`

## Since

3.0.153
