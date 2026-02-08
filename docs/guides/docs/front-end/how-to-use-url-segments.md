# URL segments and routing

Source: https://processwire.com/docs/front-end/how-to-use-url-segments/

## Summary

URL segments enable your page’s template file to become a URL router or controller to act upon different URLs sent to it.

## Key Points

- URL segments enable your page’s template file to become a URL router or controller to act upon different URLs sent to it.
- URL segments are the parts of a URL or path delimited by slashes. So if you had the path /path/to/page/ then "path", "to", and "page" would each be a URL segment. But ProcessWire actually uses the term "URL segments" to refer to the extra parts of that URL/path that did not resolve to a page.
- Lets assume that the path /products/tools/hammer/ resolved to an actual page in our site when accessed at that URL. But lets say that we accessed the URL /products/tools/hammer/photos/ and the /photos/ portion at the end does not resolve to a page. Because "photos" did not resolve to a page, ProcessWire considers this a URL segment for the "hammer" page. If URL segments are enabled for the page's template, then the "hammer" page will displayed, despite the fact that we had the "photos" segment at the end. Because it is the first URL segment that didn't resolve to a page, it is considered URL segment #1.

## Sections


### What are URL segments?

URL segments are the parts of a URL or path delimited by slashes. So if you had the path /path/to/page/ then "path", "to", and "page" would each be a URL segment. But ProcessWire actually uses the term "URL segments" to refer to the extra parts of that URL/path that did not resolve to a page.


### How do you enable URL segments?

URL segments are not enabled by default. They have to be enabled for each template you want them in: Setup > Templates > [your template] > URLs > Enable URL segments. By default, ProcessWire allows up to 4 stacked URL segments before it'll start throwing 404s. You may modify this setting in your /site/config.php file via the $config->maxUrlSegments directive:


### Where can you use URL segments?

You can use URL segments on any page where your template settings allow, regardless of whether it has children or not. Should there be a child page that has the same name as a URL segment that the parent page's template is looking for, the pages in the tree always have precedence. Meaning, URL segments only apply if the requested URL did not resolve to an actual page. As a result, you should avoid using URL segments where you think the page names and URL segments could collide.


### How does a template file identify URL segments?

URL segments can be accessed from the $input API variable:


### Best practices

When you have URL segments enabled for your template, any segments can be used to arrive at the same page. As a result, it is a best practice to respond to the segments you want, and deny all others. We recommend that you trigger a "404 not found" error when you come across an unrecognized URL segment. Lets take the example from the previous section and modify it to account for this:


### Using $input->urlSegmentStr instead

If you want to retrieve all URL segments in one string, then $input->urlSegmentStr() does the trick. This is often preferable to retrieving a single URL segment like $input->urlSegment1 because we can automatically exclude the possibility of additional URL segments. If you simply replace the switch statement in the previous example with switch($input->urlSegmentStr) then you can effectively remove the first line of code from the example, which would throw a 404 if a second URL segment was also present.


### Page numbers and URL segments

When using pagination, you may also see page numbers in URLs, like /a/b/c/page2/. The page2 portion is not considered a URL segment and is instead considered a page number. When page numbers are enabled for your template, any URLs matching the page number format will not be counted towards your URL segments. When both URL segments and page numbers are used, the page numbers always appear at the end.


### URL segment whitelist
