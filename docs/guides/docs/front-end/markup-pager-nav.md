# MarkupPagerNav (markup for pagination)

Source: https://processwire.com/docs/front-end/markup-pager-nav/

## Summary

This module renders navigation for pagination. Such navigation usually appears as a list of "1, 2, 3, next…" links at the bottom of search results.

## Key Points

- This module renders navigation for pagination. Such navigation usually appears as a list of "1, 2, 3, next…" links at the bottom of search results.
- In ProcessWire, this is most commonly used when you want to separate a large list of links into multiple pages, making it easier for the user to browse, and quicker for the server to render. For instance, lets say that you needed to generate a list of links to 100 pages, but only wanted to display 10 per page. This module makes that easy, and it is already hooked into other modules to make it even simpler. Here is an example from the Skyscrapers demo site.
- The MarkupPagerNav module is designed to automatically paginate the results of any API method that returns more than one page (i.e. a PageArray). The most common example is the $pages->find() method, which we will use in the examples below.

## Sections


### Enabling Pagination


### Using Pagination in your Templates

The MarkupPagerNav module is designed to automatically paginate the results of any API method that returns more than one page (i.e. a PageArray). The most common example is the $pages->find() method, which we will use in the examples below.


### Example #1

In this example, we will retrieve all pages in the site with an ID greater than 1, limit the results to 10, and sort alphabetically by title. The result would be all pages except for the homepage, retrieving a max of 10 at a time. This is a somewhat contrived example, so you would most likely want to replace the selector in this example with with your own selector. Regardless, you'll always want to specify a "limit" equal to the number of results you want to show per page, when using pagination.


### Example #2

Most likely you aren't using that built-in render method in the previous example because you are generating your own markup for your search results. Not to worry, generating your pagination is still just as easy. Just call $results->renderPager() rather than $results->render(). That will render just the pagination links, leaving you to generate the markup for your results. In the example below, we use this method, but also print out the pagination at both the top and bottom of the results:


### Do I have to keep track of the page number?

Not unless you want to. ProcessWire will keep track of the page number and automatically adjust the results returned from any method that returns pages and has a limit applied to it. Generally that means you don't have to pay any attention to what the page number is in your template code, unless you want to print it in a headline or <title> tag, for instance. You can always retrieve the current page number from $input->pageNum.


### Are there any side effects?

If your template has page numbers enabled (as this page instructed) then ProcessWire is going to paginate all calls to API functions that return PageArrays where you have specified a limit. This includes:


### Is Pagination Compatible with Template Caching?

Yes, pagination may be used with template caching and ProcessWire will cache up to 999 paginated versions of each page.


### Styling Pagination

If you tried out the examples above, you would have noticed that the pagination was unstyled and thus appeared just like any other unordered list on your site. ProcessWire doesn't make any assumptions about your site's design, so you should style the list in your CSS stylesheet(s) to be consistent with your site. But here are some styles to paste into your stylesheet as a good starting point, or feel free to use them as-is if you prefer.
