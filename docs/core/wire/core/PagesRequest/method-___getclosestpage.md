# PagesRequest::___getClosestPage()

Source: `wire/core/PagesRequest.php`

Get closest matching page when getPage() returns an error/NullPage

This is useful for a 404 page to suggest if maybe the user intended a different page
and give them a link to it. For instance, you might have the following code in the
template file used by your 404 page:
~~~~~
echo "<h1>404 Page Not Found</h1>";
$p = $pages->request()->getClosestPage();
if($p->id) {
  echo "<p>Are you looking for <a href='$p->url'>$p->title</a>?</p>";
}
~~~~~

@return Page|NullPage
