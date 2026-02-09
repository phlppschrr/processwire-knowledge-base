# PagesAccess

Source: `wire/core/PagesAccess.php`

ProcessWire Pages Access

Pages Access
Maintains the pages_access table which serves as a way to line up pages to the templates that maintain their access roles.
This class serves as a way for PageFinder to determine if a user has access to a page
before actually loading it.

The pages_access table contains just two columns:

	- `pages_id` (int): Any given page
	- `templates_id` (int): The template that sets this pages access

Pages using templates that already define their access (determined by $template->useRoles)
are omitted from the pages_access table, as they aren't necessary.

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [rebuild()](method-rebuild.md)
Method: [updateTemplate()](method-___updatetemplate.md) (hookable)
Method: [updatePage()](method-___updatepage.md) (hookable)
Method: [deletePage()](method-deletepage.md)
Method: [getTemplates()](method-gettemplates.md)
Method: [getAccessTemplates()](method-getaccesstemplates.md)
