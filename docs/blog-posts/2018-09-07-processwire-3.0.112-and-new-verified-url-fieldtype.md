# ProcessWire 3.0.112 and new Verified URL Fieldtype

Source: https://processwire.com/blog/posts/processwire-3.0.112-and-new-verified-url-fieldtype/

## Sections


## ProcessWire 3.0.112 and new Verified URL Fieldtype

7 September 2018 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-3.0.112-and-new-verified-url-fieldtype/#comments)

*Last week I [briefly mentioned](/talk/topic/19905-quick-weekly-update-31-aug-2018/) in the forums a new Verified URL Fieldtype that I was working on. This week, we'll take a closer look at that. Plus, there is an alpha version of it ready for download in the ProFields board. In addition, there's a new core version on the dev branch this week…*


## ProcessWire 3.0.112

ProcessWire 3.0.112 on the dev branch contains some relatively minor updates and fixes relative to version 3.0.111. One of the most significant updates in this version is a refactoring of the ProcessPageClone module, plus related hooks and language support. Several improvements were also made to the recently added PagesNames class, which is also accessible directly from $pages->names(). Several small improvements have also been added to the WireHttp class, though they do not affect the API outside of it. Finally, an issue was fixed with CKEditor where drag/drop of an image into non-default language was not properly uploading the image.


## ProFields: Verified URL Fieldtype


### What Verified URL does

The Verified URL Fieldtype (FieldtypeVerifiedURL module) extends the core FieldtypeURL module and adds the ability to verify that the entered URL actually exists. It does this with an HTTP HEAD request. That HEAD request returns an HTTP status code, which reveals whether the URL is active and working, is producing a redirect, or is producing an error.

The module remembers this status code and stores it with the URL, so that you can easily isolate working URLs from non-working URLs. This Fieldtype is particularly handy on sites that have to maintain a lot of URLs for one reason or another.

In addition to initially verifying the status of a URL, the module goes back and re-verifies the URLs at set intervals. This ensures the long-term quality of the URLs that you store in your site's data. If an initially valid URL later becomes a 404 "not found", this module will find it for you automatically in the background.


### Pulling page titles

The Verified URL Fieldtype can optionally pull and store the contents of the <title> tag on URLs that resolve to HTML pages. This is helpful for display of anchor text on links the URL might be getting used in. But it's also helpful for the editor to identify URLs that may be valid, but no longer desirable.

For instance, on a site where I'm using this field, some URLs are reporting as valid (because technically, they are), but the <title> on them is "Domain for Sale", and that's a pretty good indicator that we don't want to be linking to it anymore.


### Identifying redirects

This Fieldtype can optionally be configured to identify and store the redirect URL for 301 permanent or 302 temporary redirects. If the URL stored in the field results in a 301/302 redirect, then the redirect URL gets stored in a "redirect" property of the field's value, should you want to use it.

It can also be configured to update the stored URL to reflect the new redirect URL. However, I've set it up so that it only provides this option if the website's domain name hasn't changed. If a 301 redirect involves a domain name change, that's something that probably needs to be manually inspected, just as a matter of safety/security.


### Handling errors

When a URL results in an error status, the Fieldtype can be optionally be configured to make the formatted URL value blank on the front-end, so that you can easily skip over outputting them, without having to inspect the HTTP status code to see if it's an error code. Basically, it can behave as if the field had no value present, even if it technically does behind the scenes.

URLs that produce errors (like 404s and 500s, or any error code) can be checked back upon at a set interval, just in case they come back online. You can also configure how many chances they get. For instance, if 3 attempts over 3 weeks all produce error codes, then we can probably stop checking it going forward. By default, the module comes configured with a behavior like this.


### Checking URLs

Checking the status of URLs can be a fairly time consuming process, since it involves initiating outbound HTTP requests to the URLs. To accommodate this, FieldtypeVerifiedURL limits how much work it will perform on any single request. You can configure the maximum time to allow it to use per request. Though it won't use any time unless a Verified URL field is accessed from a page, and that particular URL has not yet been verified, or its verification data is considered expired.

For the first site that I'm using this field on, I have several hundred "product" pages that each have a couple of Verified URL fields on them. These fields were previously regular URL fields. It doesn't attempt to verify the URLs until each of those pages is accessed, either in the page editor, or on the front-end. As users browse the site, the Verified URL data will naturally populate over time.


### Using Verified URLs

Once the FieldtypeVerifiedURL module is installed, you can create a new Verified URL field, or you can convert any existing regular URL field to be a Verified URL field. However, a Verified URL field comes with quite a few more configuration options, so you'd want to review them on the “Details” tab of the field editor, and make updates as you see fit.

From the API side, output of a Verified URL field can be handled the same way as a regular URL field. However, by default, a Verified URL is an object (of type VerifiedURL, which is a type of WireData). The string value of this object is just the URL. But there are some other properties you can access from it. Here's a few examples of using them below. Lets say that we've got a Verified URL field named "some_url".

```php
// output the URL
echo $page->some_url; // http://weekly.pw

// output the status code of the URL
echo $page->some_url->status; // 301

// output the status string of a URL
echo $page->some_url->statusStr; // 301 Moved Permanently (1 day ago)

// output the redirect URL (note https rather than http)
echo $page->some_url->redirect; // https://weekly.pw

// output the <title> tag of the URL
echo $page->some_url->title; // ProcessWire Weekly

// find all pages with 404s in some_url field
$items = $pages->find("some_url.status=404");
```


### Good use case

While I'm currently using Verified URL with a scientific database project (client work), I wanted to point out a very good use case present on this site. Our sites directory maintains user-submitted URLs for websites running ProcessWire. In order to keep our sites directory fresh and up-to-date, we'll be transitioning it to use the Verified URL Fieldtype to maintain the URLs to websites running ProcessWire.

The Verified URL Fieldtype will enable us to detect when sites in the directory are no longer active, and automatically remove them from our directory unless/until they come back online, all on its own. We may also use hooks in Verified URL to confirm that the site is actually running ProcessWire (or most likely, since it's not always possible to tell for certain).


### Download Verifed URL Fieldtype

If you are interested in using the Verified URL Fieldtype, it is available for ProFields subscribers to download in the [ProFields download area](/talk/topic/6413-profields-download/). Because I've been doing major programming on it as recently as today, I'm releasing it as an alpha version, as there's a good chance some more fine tuning will take place in the coming days. So if you do test it out, test thoroughly in a development environment before using in production. By this time next week we'll likely be at a beta version, and then hopefully a final/stable release version shortly afterwards. If you have a chance to try it out, thanks, and please let me know how it works for you.


### Verifed URL Screenshots

A couple examples of Verifed URL fields as seen in the page editor:

Below is an example of using Lister/ListerPro to find all pages that have a Verified URL field named “source_url” with status of 400 or higher, which would all be HTTP error codes. These would be pages that I might need to revisit to see if I had the wrong URL, or perhaps I need to locate new URLs for them.

In the screenshot below you can see the configuration screen for a Verified URL field. This reveals a lot about how it works and what can be configured:

Thanks for reading! Next week will likely focus on covering the queue of GitHub issue reports for ProcessWire version 3.0.113. By the end of September (or early October), I'm hoping to transition our stable dev version to the next master branch version. In early to mid October, the plan at present is to take a brief break from the core and shift focus to making some updates on the processwire.com website, and then return to the core shortly after. Hope that you enjoy your weekend, and be sure to visit [weekly.pw](https://weekly.pw) for the latest ProcessWire news and updates.
