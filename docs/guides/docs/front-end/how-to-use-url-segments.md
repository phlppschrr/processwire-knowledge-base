# Using URL segments and routing in ProcessWire CMS

Source: https://processwire.com/docs/front-end/how-to-use-url-segments/

## Summary

URL segments enable your page’s template file to become a URL router or controller to act upon different URLs sent to it.

## Key Points

- URL segments enable your page’s template file to become a URL router or controller to act upon different URLs sent to it.
- URL segments are the parts of a URL or path delimited by slashes. So if you had the path /path/to/page/ then "path", "to", and "page" would each be a URL segment. But ProcessWire actually uses the term "URL segments" to refer to the extra parts of that URL/path that did not resolve to a page.
- Lets assume that the path /products/tools/hammer/ resolved to an actual page in our site when accessed at that URL. But lets say that we accessed the URL /products/tools/hammer/photos/ and the /photos/ portion at the end does not resolve to a page. Because "photos" did not resolve to a page, ProcessWire considers this a URL segment for the "hammer" page. If URL segments are enabled for the page's template, then the "hammer" page will displayed, despite the fact that we had the "photos" segment at the end. Because it is the first URL segment that didn't resolve to a page, it is considered URL segment #1.

## Sections


## URL segments and routing

URL segments enable your page’s template file to become a URL router or controller to act upon different URLs sent to it.


### What are URL segments?

URL segments are the parts of a URL or path delimited by slashes. So if you had the path /path/to/page/ then "path", "to", and "page" would each be a URL segment. But ProcessWire actually uses the term "URL segments" to refer to the extra parts of that URL/path that did not resolve to a page.

Lets assume that the path /products/tools/hammer/ resolved to an actual page in our site when accessed at that URL. But lets say that we accessed the URL /products/tools/hammer/photos/ and the /photos/ portion at the end does not resolve to a page. Because "photos" did not resolve to a page, ProcessWire considers this a URL segment for the "hammer" page. If URL segments are enabled for the page's template, then the "hammer" page will displayed, despite the fact that we had the "photos" segment at the end. Because it is the first URL segment that didn't resolve to a page, it is considered URL segment #1.

If there was yet another segment appended to it, like /products/tools/hammer/photos/grip/ then "photos" would be URL segment #1 and "grip" would be URL segment #2. The "hammer" page would still be displayed, but its template file could respond to the different URL segments however it wanted. In this case, the logic in the template file might look for "photos" in URL segment #1 and display a photo gallery when present.

As you might gather from this example, URL segments enable your page's template file to become a URL router or controller to act upon different URLs sent to it.


### How do you enable URL segments?

URL segments are not enabled by default. They have to be enabled for each template you want them in: Setup > Templates > [your template] > URLs > Enable URL segments. By default, ProcessWire allows up to 4 stacked URL segments before it'll start throwing 404s. You may modify this setting in your /site/config.php file via the `$config->maxUrlSegments` directive:

```
$config->maxUrlSegments = 4;
```


### Where can you use URL segments?

You can use URL segments on any page where your template settings allow, regardless of whether it has children or not. Should there be a child page that has the same name as a URL segment that the parent page's template is looking for, the pages in the tree always have precedence. Meaning, URL segments only apply if the requested URL did not resolve to an actual page. As a result, you should avoid using URL segments where you think the page names and URL segments could collide.


### How does a template file identify URL segments?

URL segments can be accessed from the [$input](https://processwire.com/docs/start/variables/input/) API variable:

```
$input->urlSegment($n); // Retrieve the $n'th URL segment (1–3*)
$input->urlSegment1; // Retrieve the first: /path/to/page/aaa/
$input->urlSegment2; // Retrieve the second: /path/to/page/aaa/bbb/
$input->urlSegment3; // Retrieve the third: /path/to/page/aaa/bbb/ccc/
$input->urlSegmentStr; // Retrieve all: /path/to/page/aaa/bbb/ccc/
```

Example:

```
if($input->urlSegment1 == 'photos') {
  // display photo gallery
} else if($input->urlSegment1 == 'map') {
  // display map
} else {
  // display main content
}
```


### Best practices

When you have URL segments enabled for your template, any segments can be used to arrive at the same page. As a result, it is a best practice to respond to the segments you want, and deny all others. We recommend that you trigger a "404 not found" error when you come across an unrecognized URL segment. Lets take the example from the previous section and modify it to account for this:

```
// we are only using 1 URL segment, so send a 404 if there's more than 1
if(strlen($input->urlSegment2)) throw new Wire404Exception();

if($input->urlSegment1 == 'photos') {
  // display photo gallery

} else if($input->urlSegment1 == 'map') {
  // display map

} else if(strlen($input->urlSegment1)) {
  // unknown URL segment, send a 404
  throw new Wire404Exception();

} else {
  // display main content
}
```

Another way of doing the same thing is to use PHP's [switch](http://php.net/manual/en/control-structures.switch.php) statement:

```
// we are only using 1 URL segment, so send a 404 if there's more than 1
if(strlen($input->urlSegment2)) throw new Wire404Exception();

switch($input->urlSegment1) {
  case '':
    // Segment 1 is empty so display main content
    break;

  case 'photos':
    // Display photo gallery
    break;

  case 'map':
    // Display map
    break;

  default:
    // Anything else? Throw a 404
    throw new Wire404Exception();
}
```

Arguably this method is easier to follow and to add further options, but it is a matter of personal preference.


### Using $input->urlSegmentStr instead

If you want to retrieve all URL segments in one string, then `$input->urlSegmentStr()` does the trick. This is often preferable to retrieving a single URL segment like `$input->urlSegment1` because we can automatically exclude the possibility of additional URL segments. If you simply replace the switch statement in the previous example with `switch($input->urlSegmentStr)` then you can effectively remove the first line of code from the example, which would throw a 404 if a second URL segment was also present.

The urlSegmentStr method/property is also convenient if you need to check multiple segments at a time. Note that the urlSegmentStr never contains a leading or trailing slash.

```
if($input->urlSegmentStr() === 'photos/primary') {
  // display primary photo
} else if($input->urlSegmentStr() === 'photos/secondary') {
  // display secondary photo
} else if(strlen($urlSegmentStr)) {
  // unknown URL segment
  throw new Wire404Exception();
}
```


### Page numbers and URL segments

When using pagination, you may also see page numbers in URLs, like /a/b/c/page2/. The page2 portion is not considered a URL segment and is instead considered a page number. When page numbers are enabled for your template, any URLs matching the page number format will not be counted towards your URL segments. When both URL segments and page numbers are used, the page numbers always appear at the end.


### URL segment whitelist

If you don't want your template file to have to determine when to throw a 404 for unknown URL segment(s) you can define a whitelist of URL segments. This is done by editing any template (Setup > Templates > your_template) and then clicking on the URLs tab. You'll see a “Which URL Segments do you want to allow?” field where you can directly specify the URL segments you want to allow, or a regular expression to match what's allowed.
