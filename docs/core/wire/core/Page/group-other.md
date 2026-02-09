# Page: other

Source: `wire/core/Page.php`

- $title: string The page’s title (headline) text
- [$path: string](method-path.md) The page’s URL path from the homepage (i.e. /about/staff/ryan/)
- [$url: string](method-url.md) The page’s URL path from the server's document root
- [$httpUrl: string](method-httpurl.md) Same as $page->url, except includes scheme (http or https) and hostname.
- [$template: Template|string](method-template.md) The Template object this page is using. The template name (string) may also be used for assignment.
- $fields: Fieldgroup All the Fields assigned to this page (via its template). Returns a Fieldgroup.
- $outputFormatting: bool Whether output formatting is enabled or not. Same as calling $page->of() with no arguments.
- $fieldgroup: Fieldgroup Fieldgroup used by page template. Shorter alias for $page->template->fieldgroup (same as $page->fields)
- [$render: PageRender](method-___render.md) May be used for field markup rendering like $page->render->title.
