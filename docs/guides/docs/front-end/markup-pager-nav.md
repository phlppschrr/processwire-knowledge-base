# Unknown

Source: https://processwire.com/docs/front-end/markup-pager-nav/

This module renders navigation for pagination. Such navigation usually appears as a list of "1, 2, 3, next…" links at the bottom of search results.

In ProcessWire, this is most commonly used when you want to separate a large list of links into multiple pages, making it easier for the user to browse, and quicker for the server to render. For instance, lets say that you needed to generate a list of links to 100 pages, but only wanted to display 10 per page. This module makes that easy, and it is already hooked into other modules to make it even simpler. [Here is an example](http://demo.processwire.com/cities/new-york-city/) from the Skyscrapers demo site.

- [Enabling Pagination](#enabling-pagination)
- [Using Pagination in your Templates](#using-pagination-in-your-templates)
- [Example #1](#example-1)
- [Example #2](#example-2)
- [Do I have to keep track of the page number?](#do-i-have-to-keep-track-of-the-page-number)
- [Are there any side effects?](#are-there-any-side-effects)
- [Is Pagination Compatible with Template Caching?](#is-pagination-compatible-with-template-caching)
- [Styling Pagination](#styling-pagination)
- [Custom Options and Markup (Optional)](#custom-options-and-markup-optional)
- [Custom Options Reference](#custom-options-reference)

---

[#](#)

### Enabling Pagination

1. Make sure the "Pager" (*MarkupPagerNav*) module is installed in Admin > Modules. If it's not installed, click the *Install* link next to it.
2. Determine what template(s) you want to use pagination with. Go to Admin > Setup > Templates > [Your Template] > URLs, and check the box for: *Allow Page Numbers. *Save.
3. Pagination should now be enabled and ready to use in your templates.

[#](#)

### Using Pagination in your Templates

The *MarkupPagerNav* module is designed to automatically paginate the results of any API method that returns more than one page (i.e. a *PageArray*). The most common example is the $pages->find() method, which we will use in the examples below.

[#](#)

### Example #1

In this example, we will retrieve all pages in the site with an ID greater than 1, limit the results to 10, and sort alphabetically by title. The result would be all pages except for the homepage, retrieving a max of 10 at a time. This is a somewhat contrived example, so you would most likely want to replace the selector in this example with with your own [selector](/api/selectors/). Regardless, you'll always want to specify a "limit" equal to the number of results you want to show per page, when using pagination.

```
<?php
$results = $pages->find("id>1, limit=10, sort=title");
echo $results->render();
```

We used the built-in render() method above to print a simple list of the pages found. Assuming that there are more pages found than what you specified for the "limit", you should see a list of pagination links appear at the end of the list. This works because when pagination is enabled, the render() method automatically prints pagination when it detects that there are more results than what was provided. You might notice that the pagination links are unstyled. There are some CSS styles further in this document that work as a good starting point to paste into your stylesheet.

[#](#)

### Example #2

Most likely you aren't using that built-in render method in the previous example because you are generating your own markup for your search results. Not to worry, generating your pagination is still just as easy. Just call $results->renderPager() rather than $results->render(). That will render just the pagination links, leaving you to generate the markup for your results. In the example below, we use this method, but also print out the pagination at both the top and bottom of the results:

```
<?php
$results = $pages->find("id>1, limit=10, sort=title");
$pagination = $results->renderPager();
echo $pagination;
echo "<ul>";
foreach($results as $result) {
    echo "<li><a href='{$result->url}'>{$result->title}</a></li>";
}
echo "</ul>";
echo $pagination;
```

[#](#)

### Do I have to keep track of the page number?

Not unless you want to. ProcessWire will keep track of the page number and automatically adjust the results returned from any method that returns pages and has a limit applied to it. Generally that means you don't have to pay any attention to what the page number is in your template code, unless you want to print it in a headline or `<title>` tag, for instance. You can always retrieve the current page number from [$input](/docs/start/variables/input/)->pageNum.

[#](#)

### Are there any side effects?

If your template has page numbers enabled (as this page instructed) then ProcessWire is going to paginate all calls to API functions that return PageArrays where you have specified a limit. This includes:

```
// where "n" is any positive number
$pages->find("limit=n");
$page->find("limit=n");
$page->children("limit=n");
$page->siblings("limit=n");
```

In my experience, the situations where this would be an undesirable side effect are rare. However, if you are viewing a paginated list on any page number greater than 1, and you find ProcessWire returning the wrong set of pages, then replace your "limit=n" selector with the following:

```
$pages->find("start=0, limit=n");
```

That will ensure that ProcessWire does not attempt to paginate the results of that function call when on page numbers greater than 1.

[#](#)

### Is Pagination Compatible with Template Caching?

Yes, pagination may be used with template caching and ProcessWire will cache up to 999 paginated versions of each page.

Note that GET and POST vars are not cached (regardless of whether you are using pagination), so if you are paginating results generated from values in GET or POST vars, you should not use template caching.

[#](#)

### Styling Pagination

If you tried out the examples above, you would have noticed that the pagination was unstyled and thus appeared just like any other unordered list on your site. ProcessWire doesn't make any assumptions about your site's design, so you should style the list in your CSS stylesheet(s) to be consistent with your site. But here are some styles to paste into your stylesheet as a good starting point, or feel free to use them as-is if you prefer.

```
.MarkupPagerNav {
  clear: both;
  margin: 1em 0;
  font-family: Arial, sans-serif;
}
.MarkupPagerNav li {
  display: inline;
  list-style: none;
  margin: 0;
}

.MarkupPagerNav li a,
.MarkupPagerNav li.MarkupPagerNavSeparator {
  display: block;
  float: left;
  padding: 2px 9px;
  color: #fff;
  background: #2f4248;
  margin-right: 3px;
  font-size: 10px;
  font-weight: bold;
  text-transform: uppercase;
}

.MarkupPagerNav li.MarkupPagerNavOn a,
.MarkupPagerNav li a:hover {
  color: #fff;
  background: #db1174;
  text-decoration: none;
}

.MarkupPagerNav li.MarkupPagerNavSeparator {
  display: inline;
  color: #777;
  background: #d2e4ea;
  padding-left: 3px;
  padding-right: 3px;
}
```

[#](#)

### Custom Options and Markup (Optional)

The examples above have ProcessWire generating the HTML5/XHTML markup for your pagination links, and all use the default pagination options. These are typically just fine, but there may be an instance where you want to modify this behavior. To do so, specify an $options array to the renderPager method. You may specify one or more options. The defaults will be used for any options that you omit. Below is an example that might modify the markup output by the renderPager method (though the values shown here are actually the defaults):

```
<?php
echo $results->renderPager(array(
  'nextItemLabel' => "Next",
  'previousItemLabel' => "Prev",
  'listMarkup' => "<ul class='MarkupPagerNav'>{out}</ul>",
  'itemMarkup' => "<li class='{class}'>{out}</li>",
  'linkMarkup' => "<a href='{url}'><span>{out}</span></a>"
));
```

Below is a reference of all the options available, along with the defaults.

[#](#)

### Custom Options Reference

[https://processwire.com/api/ref/markup-pager-nav/](https://processwire.com/api/ref/markup-pager-nav/)- [/docs/front-end/](/docs/front-end/)- [/docs/front-end/output/](/docs/front-end/output/)- [/docs/front-end/how-to-use-url-segments/](/docs/front-end/how-to-use-url-segments/)- [/docs/front-end/include/](/docs/front-end/include/)- [/docs/front-end/front-end-editing/](/docs/front-end/front-end-editing/)- [/docs/front-end/markup-pager-nav/](/docs/front-end/markup-pager-nav/)- [/docs/](/docs/)- [/api/ref/](/api/ref/)- [/docs/start/](/docs/start/)- [/docs/front-end/](/docs/front-end/)- [/docs/tutorials/](/docs/tutorials/)- [/docs/selectors/](/docs/selectors/)- [/docs/modules/](/docs/modules/)- [/docs/fields/](/docs/fields/)- [/docs/user-access/](/docs/user-access/)- [/docs/security/](/docs/security/)- [/docs/multi-language-support/](/docs/multi-language-support/)- [/docs/more/](/docs/more/)
