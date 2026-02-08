# Templates

Source: `wire/core/Templates.php`

ProcessWire Templates

Manages and provides access to all the Template instances

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

Manages and provides access to all the Templates.

## other

@method bool save(Template $template) Save the given Template.

@method bool delete() delete(Template $template) Delete the given Template. Note that this will throw a fatal error if the template is in use by any pages.

@method array getExportData(Template $template) Export Template data for external use.

@method array setImportData(Template $template, array $data) Given an array of Template export data, import it to the given Template.

@method void fileModified(Template $template) Hook called when a template detects that its file has been modified.

@method array getTags($getTemplateNames = false) Get tags for all templates (3.0.179+)

## __construct()

Construct the Templates

@param Fieldgroups $fieldgroups Reference to the Fieldgroups

## add()

Add and save new template (and fieldgroup) with given name and return it

@param string $name

@param array $properties Any additional properties to add to template

@return Template

@throws WireException if given invalid template name or template already exists

@since 3.0.170

## get()

Get a template by name or ID

Given a template ID or name, return the matching template or NULL if not found.

@param string|int $key Template name or ID

@return Template|null|string

## ___save()

Save a Template

~~~~~
$templates->save($template);
~~~~~

@param Saveable|Template $item Template to save

@return bool True on success, false on failure

@throws WireException

## ___delete()

Delete a Template

@param Template|Saveable $item Template to delete

@return bool True on success, false on failure

@throws WireException Thrown when you attempt to delete a template in use, or a system template.

## ___clone()

Clone the given Template

Note that this also clones the Fieldgroup if the template being cloned has its own named fieldgroup.

@todo: clone the fieldgroup context settings too.

@param Template|Saveable $item Template to clone

@param string $name Name of new template that will be created, or omit to auto-assign.

@return bool|Template $item Returns the new Template on success, or false on failure

## rename()

Rename given template (and its fieldgroup, and file, when possible)

Given template must have its previous 'name' still present, and new name provided in $name
argument to this method.

@param Template $template

@param string $name New name to use

@since 3.0.170

@throws WireException if rename cannot be completed

## getNumPages()

Return the number of pages using the provided Template

@param Template $tpl Template you want to get count for

@return int Total number of pages in use by given Template

## encodeData()

Overridden from WireSaveableItems to retain specific keys

@param array $value

@return string

## ___getExportData()

Export Template data for external use


@param Template $template Template you want to export

@return array Associative array of export data

## ___setImportData()

Given an array of Template export data, import it to the given Template

~~~~~~
// Example of return value
$returnValue = array(
  'property_name' => array(
    'old' => 'old value', // old value (in string comparison format)
    'new' => 'new value', // new value (in string comparison format)
    'error' => 'error message or blank if no error' // error message (string) or messages (array)
  ),
  'another_property_name' => array(
    // ...
  )
);
~~~~~~


@param Template $template Template you want to import to

@param array $data Import data array (must have been exported from getExportData() method).

@return array Returns array with list of changes (see example in method description)

## getParentPage()

Return the parent page that this template assumes new pages are added to

- This is based on family settings, when applicable.
- It also takes into account user access, if requested (see arg 1).
- If there is no defined parent, NULL is returned.
- If there are multiple defined parents, a NullPage is returned (use $getAll to get them).

@param Template $template

@param bool $checkAccess Whether or not to check for user access to do this (default=false).

@param bool|int $getAll Specify true to return all possible parents (makes method always return a PageArray)
  Or specify int of maximum allowed `Page::status*` constant for items in returned PageArray (since 3.0.138).

@return Page|NullPage|null|PageArray

## getParentPages()

Return all possible parent pages for the given template, if predefined

@param Template $template

@param bool $checkAccess Specify true to exclude parent pages that user doesn't have access to add pages to (default=false)

@param int $maxStatus Max allowed `Page::status*` constant (default=0 which means not applicable). Since 3.0.138

@return PageArray

## getPageClass()

Get class name to use for pages using given Template

Note that value can be different from the `$template->pageClass` property, since it is determined at runtime.
If it is different, then it is at least a class that extends the one defined by pageClass.

@param Template $template

@param bool $withNamespace Include namespace? (default=true)

@return string Returned class name includes namespace

@since 3.0.152

## ___getTags()

Get all tags used by templates

@param bool $getTemplateNames Get arrays of template names for each tag? (default=false)

@return array In return value both key and value are the tag

@since 3.0.176 + hookable in 3.0.179

## ___fileModified()

Hook called when a Template detects that its file has changed

Note that the hook is not called until something in the system (like a page render) asks for the template’s filename.
That’s because it would not be efficient for PW to check the file for every template in the system on every request.


@param Template $template

@since 3.0.141
