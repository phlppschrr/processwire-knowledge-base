# PagesLoader::findMin()

Source: `wire/core/PagesLoader.php`

Minimal find for reduced or delayed overload in some circumstances

This combines the page finding and page loading operation into a single operation
and single query, unlike a regular find() which finds matching page IDs in one
query and then loads them in a separate query. As a result this method does not
need to call the getByIds() method to load pages, as it is able to load them itself.

This strategy may eventually replace the “find() + getByIds()” strategy, but for the
moment is only used when the `$pages->find()` method specifies `field=name` in
the selector. In that selector, `name` can be any field name, or group of them, i.e.
`title|date|summary`, or a non-existing field like `none` to specify that no fields
should be autojoin (for fastest performance).

Note that while this might reduce overhead in some cases, it can also increase the
overall request time if you omit fields that are actually used on the resulting pages.
For instance, if the `title` field is an autojoin field (as it is by default), and
we do a `$pages->find('template=blog-post, field=none');` and then render a list of
blog post titles, then we have just increased overhead because PW would have to
perform a separate query to load each blog-post page’s title. On the other hand, if
we render a list of blog post titles with date and summary, and the date and summary
fields are not configured as autojoin fields, then we can specify all those that we
use in our rendered list to greatly improve performance, like this:
`$pages->find('template=blog-post, field=title|date|summary');`.

While this method combines what find() and getById() do in one query, there does not
appear to be any overhead benefit when the two strategies are dealing with identical
conditions, like the same autojoin fields.


@param string|array|Selectors $selector

@param array $options
 - `cache` (bool): Allow pulling from and saving results to cache? (default=true)
 - `joinFields` (array): Names of fields to also join into the page load

@return PageArray

@throws WireException

@since 3.0.172
