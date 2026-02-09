# ProcessWire 2.6.18 updates, pagination and SEO

Source: https://processwire.com/blog/posts/processwire-2.6.18-updates-pagination-and-seo/

## Sections


## ProcessWire 2.6.18 updates, pagination and SEO

25 September 2015 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-2.6.18-updates-pagination-and-seo/#comments)


## ProcessWire 2.6.18, looking towards 2.7

We're now starting to focus on ProcessWire 2.7 and getting the dev branch ready to become the new version. We'll be aiming for release potentially as soon as a month from now. That means these blog posts won't be covering quite as many new features as the last few months have. Instead, we'll be focusing on making sure that what we've got now is as stable and streamlined as possible.

During this "preparing stable version" time, future posts will likely be covering more tips, techniques and best practices, more than new features. That's because we'll be optimizing what we've already got over the next month, rather than adding much new stuff. There's already so much new stuff between ProcessWire 2.6.2 and 2.6.18 (as we've covered in the last dozen or so blog posts), that we want to get it to ProcessWire's stable branch sooner rather than later, for everyone else to enjoy.

Given the above, much of this week's focus went towards covering existing issue reports from GitHub, fixing minor bugs and general housekeeping in the core source code. That's what you'll find in ProcessWire 2.6.18 this week, along with a couple small but useful new features, covered below. This trend will likely continue next week as we work to cover all remaining issues and begin to evaluate pending pull requests for potential inclusion in 2.6.18.

To see all the issues that have been covered, see our [dev branch commit log](https://github.com/ryancramerdesign/ProcessWire/commits/dev) for September 22 through September 25. Here's what else we've got for you this week:

Huge thanks to Antti, Teppo, Pete and all of you for keeping everything running here last week when I was out of town. If you haven't yet read [Antti's great blog post](/blog/posts/introducing-iftrunner-and-the-story-behind-it/) from last week, be sure to check it out. Hope that you all have a great weekend and week ahead. Be sure to stop by and read the [ProcessWire Weekly](http://weekly.pw) this weekend.


### New "http" prefix available for all $config->urls properties

Now you can take any `$config->urls` property like "root" or "templates", etc., and prepend "http" to the property name to retrieve the URL with the current scheme and hostname. For instance:

```
// outputs: /
echo $config->urls->root;

// outputs: http://domain.com/
echo $config->urls->httpRoot;

// outputs: /site/templates/
echo $config->urls->templates;

// outputs: http://domain.com/site/templates/
echo $config->urls->httpTemplates;
```

This works with any property in `$config->urls`, including those that you may add yourself.


### New $config->urls->next and $config->urls->prev properties

When you use ProcessWire's built-in pagination, it will now populate `$config->urls->next` and `$config->urls->prev` properties that contain the next pagination URL and the previous pagination URL. This is primarily useful for hinting to Google and other search engines using link rel=prev and rel=next tags. Here's how you might do that below. This code would go within your document `<head>` section.

```
if($config->urls->next) {
  echo "<link rel='next' content='{$config->urls->next}'>";
}
if($config->urls->prev) {
  echo "<link rel='prev' content='{$config->urls->prev}'>";
}
```

Note that ProcessWire doesn't know what the "next" and "prev" URLs would be until after you've paginated something, so this technique would require the [delayed output](/to/delayed-output/) approach. Or if using [direct output](/to/direct-output/), you'd at least have to use delayed output for your rendered pagination (i.e. render your pagination and store it in a variable to output later, before executing the code example above).

If you want your next/prev URLs to also include the scheme and hostname, use the `$config->httpNext` or `$config->httpPrev` properties rather than the next and prev properties.

More about using next/prev rel tags can be found at Google [here](http://googlewebmastercentral.blogspot.com/2011/09/pagination-with-relnext-and-relprev.html) and [here](https://support.google.com/webmasters/answer/1663744?hl=en). Lets talk more about pagination…


## Pagination and ProcessWire

If you are rendering large lists of pages like search results, lists of products, blog posts, or the like, it's a good idea to paginate them so that you are displaying 10, 20, 50 results per page… or how many ever you want to (though should probably keep it under 100). This enables faster page render time and avoids stuffing too many links on a single page. Pagination splits your results into more accessible and efficient bite size chunks that can scale forever, regardless of how large your site or application grows.


### How to enable pagination

- Make sure that you have the core MarkupPagerNav module installed (Modules > Core > Markup).
- Enable page numbers for any templates that will be outputting paginated lists of pages. You can do this from Setup > Templates > [your-template] > URLs > Allow Page Numbers.
- When finding the pages that will be paginated, add a "limit=100" to the selector (replacing 100 with the number of items you want to display per pagination). For example:

```php
$products = $pages->find("parent=/products/, sort=name, limit=25");
```

Adding that limit=25 is all that's necessary to make ProcessWire paginate the results. It will automatically load the correct set of 25 pages when accessed with a page number URL.


### Rendering your pagination

The MarkupPagerNav module (included with ProcessWire) includes everything you need to paginate a PageArray returned from a `$pages->find()` operation (or anything that returns a PageArray from the database, like `$page->children()`, and so on). This module adds a `renderPager()` method to every PageArray that you can call to render pagination markup.

```php
$products = $pages->find("parent=/products/, sort=name, limit=25");
$content = "<ul>";
foreach($products as $product) {
  $content .= "<li><a href='$product->url'>$product->title</a></li>";
}
$content .= "</ul>";
$content .= $products->renderPager();
```

If you want to change the default pagination markup, you can pass an $options array to this renderPager method. See the [pagination documentation](/api/modules/markup-pager-nav/) or the [MarkupPagerNav](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/modules/Markup/MarkupPagerNav/MarkupPagerNav.module#L87) class for more details on all the options available. For example:

```
$content .= $products->renderPager(array(
  'listMarkup' => "<ul class='pagination'>{out}</ul>",
  'nextItemLabel' => "Next",
  'previousItemLabel' => "Previous",
  'numPageLinks' => 5
));
```

Using the available options to the renderPager() method, it is possible to make it output markup consistent with the needs of nearly any existing front-end framework (i.e. Foundation, Bootstrap, Uikit, etc.)


### Style your pagination with CSS

If you aren't modifying the default markup that MarkupPagerNav provides, you'll want to add CSS styles to your stylesheet files to make the pagination look like pagination, rather than a regular HTML list. This is easy to do yourself by inspecting the output and adding styles for it, though you may also want to see the [pagination documentation](/api/modules/markup-pager-nav/) page for a good example to start from.


### Avoiding pagination pitfalls

When you perform a `$pages->find()`, `$pages->children()` or any kind of page finding operation that includes a "limit=n" in the selector (on a page that supports pagination) ProcessWire automatically determines the starting result based on the current page number. If you have other find() operations with "limit=n" selectors occurring elsewhere during that same request, ProcessWire will try to paginate them too. That may not be what you want.

For instance, lets say that your paginated results page also includes a sidebar with links to the 3 newest blog posts, which aren't meant to be paginated. When you hit page 2 in the pagination, you'll find that those 3 blog posts are no longer the newest posts, but instead the next 3 newest posts. To avoid this situation, accompany your "limit=3" selector with a "start=0", which clarifies that you don't want ProcessWire to paginate those particular results. For example:

```php
$posts = $pages->find("parent=/blog/, sort=-created, start=0, limit=3");
```


## Pagination and SEO in ProcessWire

Google is pretty good at figuring out all that it needs from your paginations without you specifically having to do anything, especially when you are using ProcessWire. But it's also true that, regardless of CMS or platform, pagination is one of the most likely sources of duplicate content in a site, among other potential problems with any kind of paginated content. So it's good to be aware of the potential issues and optimize when appropriate. The issues and best practices we outline here aren't specific to ProcessWire, but the solutions and examples are.

Google says all of this is optional, so you may only want to pursue some of these best practices if you find pagination to be an SEO problem for your specific case. Though the same can be said for most aspects of SEO. Google says it's perfectly okay to "do nothing" for pagination, but since they also support and outline many of these strategies themselves, I think it's worthwhile, especially when optimizing search accessibility is part of your project scope or budget. Optimizing your pagination and doing it correctly can also give you a potential edge over other sites that may be ignoring the issues.

If you do pursue any of these strategies, just make sure you do them right, do your own research, and test test test. Sometimes implementing SEO strategies incorrectly is significantly worse than not implementing them at all. Further, many of these strategies are either/or strategies, so you shouldn't implement them all, but instead determine which are most appropriate for your situation.


### Why is pagination sometimes a problem for SEO?

Whether in ProcessWire or any other system that supports pagination, the output of pagination typically implies a single page with a results/list section that changes between paginations. The underlying page is the same, and often shares the same `<title>`, headline tags, and other content with the first pagination. Further, the content of a given pagination like "page 2" may change often, or collide with another pagination, due to other variables like sorting or filters. There is a lot of potential for duplicate content, and that's something you want to avoid with any search strategy.

There is also a lot of potential for search crawlers to get stuck, spending all their time in endless paginations and variable variations of them, rather than the pages that really matter on your site. The content of paginated pages is often purely links to significant content, rather than the paginated pages themselves being significant content. Google might consider these paginated pages (especially after the first pagination) to be relatively low-quality content that has little value from a search results perspective. Google prefers quality over quantity.

With these issues in mind, here are some best practices and examples when using pagination with ProcessWire. Keep in mind we're focusing primarily on pagination of pages showing lists of page results. We aren't talking about pagination of a single article, which is different, though less-common type of pagination in ProcessWire. For that type of pagination, it's better to do nothing, or use a canonical link tag that references a "view all" page containing the entire article.


### Throw a 404 when a requested pagination produces no results

It's a best practice to throw a 404 when a pagination is requested that contains no results. While the MarkupPagerNav module isn't going to render links for paginations that don't exist, it's always possible Google has indexed those paginations at some point in the past (like if the result set has grown smaller) and you don't want empty pages getting indexed by search engines. You do this by checking if the result set is empty and the current page number is something greater than 1. You would typically perform this check immediately after your paginated $pages->find() or equivalent operation. For example:

```php
$products = $pages->find("parent=/products/, sort=name, limit=25");
if(!count($products) && $input->pageNum > 1) {
  throw new Wire404Exception();
}
```

This ensures that Google and other search engines won't ever attempt to index paginations that don't exist. It also ensures that these useless blank pages won't end up in template cache or ProCache.


### Using meta robots "noindex,follow" tags with pagination

A meta robots tag looks like this, and goes in your document `<head>`:

```
if($input->pageNum > 1) {
  echo "<meta name='robots' content='noindex,follow'>";
}
```

This prevents Google (and other search engines) from indexing paginations beyond the first, but still enables them to follow and index the pages linked from the paginations. This is a safe, easy and desirable solution because paginated pages often carry the same exact <title>, meta description and other content as the first pagination (unless you've specifically changed it), which might be considered duplicate content in the eyes of Google.

It's a good idea to use a meta robots "noindex,follow" tag when you want to avoid any potential duplicate content issues, or you don't consider the content beyond the first pagination to be significant to search engines (even if the links on them are significant).


### Using canonical link tags with pagination

A canonical link tag would look like this in your document `<head>`:

```
if($input->pageNum > 1) {
  echo "<link rel='canonical' href='$page->httpUrl'>";
}
```

The above canonical link tag would appear on any paginated page after the first pagination. It essentially says "consider this equivalent to the first pagination." It's a way of indicating that all the paginations shouldn't be considered separate URLs in the eyes of Google. When it comes to SERPs (search engine result pages), they should always send users to the first pagination. Though for this particular scenario, I would instead suggest using the meta robots "noindex,follow" tag instead (mentioned earlier).

The canonical link tag can be useful if you are providing a "view all" page, as discussed further in this post. It enables you to take all your paginations and point them to a single "view all" page. Read the next section for more info on that.

By the way, there are plenty of other good reasons (outside of pagination) to use canonical link tags from an SEO perspective, especially if your site is accessible at multiple host names or schemes, or accepts GET variables that aren't significant to search indexing. But you'll need to carefully balance their use with your intentions for the search accessibility of pagination. If your paginated pages are significant to search engines and multiple host names or schemes are possible, you'll want to construct your canonical link tag in a manner that recognizes pagination:

```
// specify scheme and host statically rather than from $page->httpUrl
$canonicalURL = 'https://www.domain.com' . $page->url;

// if on a pagination, include that as part of your canonical URL
if($input->pageNum > 1) {
  $canonicalURL .= $config->pageNumUrlPrefix . $input->pageNum;
}
echo "<link rel='canonical' href='$canonicalURL'>";
```

You may need to adjust the above code to be consistent with your settings for trailing slashes as specified in each template's URLs tab (we are assuming the defaults here). Also note the above does not consider URL segments, which could be applicable to your case. If you are using them, you might add something like this before the `$input->pageNum` check in the previous example:

```
// add in any URL segments
if($input->urlSegmentStr) {
  $canonicalURL .= $input->urlSegmentStr . '/';
}
```


### Using a pagination "view all" page

A "view all" page provides a single URL at which all the results can be viewed together, rather than paginated. Your paginated pages (including the first) would all contain a canonical link tag in the document head that points to this "view all" page.

The "view all" page would typically be triggered by a URL segment that you implement, like "view-all", i.e. "/path/to/page/view-all/". When you detect that URL segment, you would output your results without pagination, i.e.

```
if($input->urlSegmentStr == 'view-all') {
  // non-paginated
  $products = $page->children();
} else {
  // paginated, 10 results per page
  $products = $page->children("limit=10");
}
if(!count($products) && $input->pageNum > 1) {
  throw new Wire404Exception();
}

// render markup for results however you want to
$content = $products->render();

if($products->getLimit()) {
  // include pagination only when results are paginated
  $content .= $products->renderPager();
}
```

In your document `<head>`, you'd want to output a canonical link tag on the pages that don't have the view-all URL segment:

```
if($page->template == 'products' && $input->urlSegmentStr != 'view-all') {
  echo "<link rel='canonical' href='{$page->httpUrl}view-all/'>";
}
```

I would only suggest this "view all" strategy if your max quantity of paginations is always going to be small (like less than 5 or 10), and the max quantity of links isn't going to be much more than a hundred or so. The reason is that this "view all" strategy doesn't scale. It requires that all potential matches be loaded at once, which can make for a slow render (and potential denial-of-service target), or even a potential out-of-memory condition if the list grows too large. A view-all page with a thousand page links is useless. We all know that Google doesn't like slow loading pages, error pages, or pages with hundreds or thousands of links.

The "view all" strategy doesn't scale with Google either. They consider pages with hundreds or thousands of links to be low-quality and don't bother with them after a certain quantity. So when you read elsewhere that Google "favors the view all strategy", it should always be qualified with "for small scale situations". Most of the situations we are describing in this post focus on infinitely scalable solutions, so avoid the "view all" strategy if you are dealing with any kind of scale. But if you are just dealing with a few paginations, or you are paginating a multi-page article, then the "view all" strategy is worth considering.


### Using rel=next and rel=prev meta tags for pagination

These were described earlier in this post, so I won't rehash what was already covered above. But these "hints" to Google may be a useful component of your pagination SEO strategy. You don't necessarily need ProcessWire 2.6.18+ to use them either. You can easily populate your own next/prev URLs with a little bit of code built next to your `$pages->find()` operation:

```php
$items = $pages->find("parent=/products/, limit=25, sort=name");
$baseURL = $page->url . $config->pageNumUrlPrefix;
if($items->getStart() + $items->getLimit() < $items->getTotal()) {
  $config->urls->next = $baseURL . ($input->pageNum+1);
}
if($input->pageNum > 1) {
  $config->urls->prev = $baseURL . ($input->pageNum-1);
}
```

When it comes to outputting your link rel=next or rel=prev tags, you can use the same example provided earlier in this post.


### Using canonical link or noindex tags when user input filters or sorts output

When your paginated pages produce results without user input, but enable user input to filter or sort results via GET request with query string, you may want to keep Google out of the user filtered/sorted versions. There are a couple of good reasons for this:

- It's not distinct content (thereby low quality or duplicate in the eyes of Google).
- It potentially creates an infinite number of URLs for crawlers to get stuck in, wasting time and consuming resources.

For the case of GET variables affecting the output, I would either output a link canonical or meta robots noindex tag in the document head. To be honest, I don't know for certain which is preferable for this scenario–either seems like it will get the job done. Though I might lean towards canonical. Maybe someone reading this will reply with something more definitive. Essentially you'd detect the condition and output your meta/link tag like this:

```
if($page->template == 'products' && count($_GET)) {
  echo "<link rel='canonical' href='$input->httpUrl'>";
}
```

Note: `$input->httpUrl` includes URL segments and page numbers. If you instead want to make your first pagination the canonical URL, you'd replace $input->httpUrl with `$page->httpUrl`.


### Use distinct title and headline tags on your paginations

If you are opting to have google index your paginations (beyond the first page), and/or taking the "do nothing" approach, it's a good idea to make sure your paginations have distinct `<title>` tags, headlines and perhaps meta descriptions (if used). Actually, this is a good idea regardless of your SEO strategy towards pagination.

When paginations are indexable, Google doesn't like seeing the same exact <title> on every one of them, as there's really no way to distinguish between page 1 and page 50, from an outside perspective. And Google's SERPs are an outside perspective. Yet, there really isn't much one can say to distinguish page 1 from 50… they are all products, blog posts, coffees, widgets or whatever. So work with what you've got. We at least know the page number, so we can say "Products Page 1":

```
$title = "Products Page $input->pageNum";
```

But that's too boring, lets instead say "Products 1 to 25 of 100" which reveals even a little more information:

```
$products = $page->children("limit=25"); 

$first = $products->getStart() + 1;
$last = $products->getStart() + count($products);
$total = $products->getTotal();

// text for <h1> and <title>
$title = "Products $first to $last of $total";

// generate markup for output
$content = "<h1>$title</h1>" .
  $products->render() .
  $products->renderPager();
```

Perhaps there are other useful indicators you want to include with this meta information about the page content, when available. Examples might include: "sorted by date" or "in category: dark coffees", and so on. This is how you give each of your paginations more value as something distinct on their own.


### What other pagination techniques do you find helpful?

We've provided an overview of several pagination best practices for SEO here, but we'd also be interested in hearing from you about what techniques you've learned or found to be helpful. Please reply in the comments section below.
