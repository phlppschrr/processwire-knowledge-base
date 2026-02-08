# Page: other

Source: `wire/core/Page.php`

@property string $title The page’s title (headline) text

@property string $path The page’s URL path from the homepage (i.e. /about/staff/ryan/)

@property string $url The page’s URL path from the server's document root

@property string $httpUrl Same as $page->url, except includes scheme (http or https) and hostname.

@property Template|string $template The Template object this page is using. The template name (string) may also be used for assignment.

@property Fieldgroup $fields All the Fields assigned to this page (via its template). Returns a Fieldgroup.

@property bool $outputFormatting Whether output formatting is enabled or not. Same as calling $page->of() with no arguments.

@property Fieldgroup $fieldgroup Fieldgroup used by page template. Shorter alias for $page->template->fieldgroup (same as $page->fields)

@property PageRender $render May be used for field markup rendering like $page->render->title.
