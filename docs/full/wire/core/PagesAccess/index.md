# PagesAccess

Source: `wire/core/PagesAccess.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

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

Methods:
- [`__construct($item = null)`](method-__construct.md)
- [`rebuild(int $parent_id = 1, int $accessTemplateID = 0, bool $doDeletions = true)`](method-rebuild.md)
- [`updateTemplate(Template $template)`](method-___updatetemplate.md) (hookable)
- [`updatePage(Page $page)`](method-___updatepage.md) (hookable)
- [`deletePage(Page $page)`](method-deletepage.md)
- [`getTemplates()`](method-gettemplates.md)
- [`getAccessTemplates()`](method-getaccesstemplates.md)
