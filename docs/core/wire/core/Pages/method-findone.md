# Pages::findOne()

Source: `wire/core/Pages.php`

Like find() but returns only the first match as a Page object (not PageArray).

This is functionally similar to the `get()` method except that its default behavior is to
filter for access control and hidden/unpublished/etc. states, in the same way that the
`find()` method does. You can add an `include=...` to your selector string to bypass.
This method also accepts an `$options` array, whereas `get()` does not.

~~~~~~
// Find the newest page using the blog-post template
$blogPost = $pages->findOne("template=blog-post, sort=-created");
~~~~~~


@param string|array|Selectors $selector Selector string, array or Selectors object

@param array|string $options See $options for $pages->find()

@return Page|NullPage Returns a Page on success, or a NullPage (having id=0) on failure

@since 3.0.0

@see Pages::get(), Pages::find(), Pages::findMany()
