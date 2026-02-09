# Optimizing processwire.com and major upgrades to ProCache

Source: https://processwire.com/blog/posts/optimizing-processwire.com-and-major-upgrades-to-procache/

## Sections


## Optimizing processwire.com and major upgrades to ProCache

15 May 2015 by Ryan Cramer [ 5 Comments](/blog/posts/optimizing-processwire.com-and-major-upgrades-to-procache/#comments)


### A great start for ProcessWire 2.6

One week ago [we released ProcessWire 2.6](/blog/posts/processwire-2.6-is-here/) and the reception has been great. No major issues have been reported and we've not heard of any significant upgrade hiccups. If you aren't using ProcessWire 2.6 yet, we encourage you to upgrade and enjoy. As always, please let us know if you run into any issues, but we think you'll find the upgrade very easy and worthwhile.

What's next for 2.6? We'll be working on some minor reported details and largely cosmetic tweaks for version 2.6.1 over the next couple of weeks. But there's no reason to wait on upgrading–grab and enjoy it now. Thanks again to all of you for making ProcessWire 2.6 such a success.


### Optimizing processwire.com

At processwire.com we are dealing with increasingly large amounts of traffic. Occasionally we get traffic spikes that are more than the number of connections that Apache will accept, despite being on a dedicated server (though admittedly only an entry-level server).

The forums, powered by IP.Board are responsible for a lot of the load, and there's not much we can do about that. But since we write ProcessWire, there's plenty we can do from the ProcessWire side. So we've looked at it as a challenge and opportunity to see how far we can optimize content delivery with ProcessWire, even with limited server resources.

On the ProcessWire side, most HTTP requests to the server are delivering static cached pages from ProCache or external assets linked from them (like images, stylesheets, javascript). When traffic spikes, the quantity of concurrent HTTP requests may occasionally go above what Apache is willing to deliver from a single server. When that happens, Apache gets overloaded. So we've been on a mission to see how far we can optimize content delivery without upgrading the hardware side of it.

ProcessWire's core is already well optimized for content delivery, so the most potential optimization has to do with the front end:

- reducing HTTP requests
- compressing delivery with GZIP
- minifying and merging CSS and JS files
- minifying HTML
- optimizing expiration settings in the .htaccess file
- offloading static file asset delivery to a content delivery network (CDN)

All of this fits in line with what ProCache was designed for. So over the last few weeks, we've been making major upgrades to ProCache to support this.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1118/screen_shot_2015-05-12_at_2_44_25_pm.png)We've been using several tools to evaluate our progress such as [webpagetest.org](http://www.webpagetest.org) and [gtmetrix.com](http://www.gtmetrix.com) (PageSpeed and YSlow), among others. These tools use a school grading scale. Prior to integration with the new version of ProCache, we were scoring all C, D and F scores, which is pretty much standard for most sites out there. After integrating the new version of ProCache, we are scoring straight As across the board. This is all without any changes to the site template files. Read on to learn more about what this new version of ProCache brings:


## New ProCache 3.0 and what it adds

The latest version of [ProCache](/blog/categories/procache/) (3.0) was released today in the ProCache board (registered ProCache users can download now). Previously ProCache focused purely on eliminating PHP and MySQL from the content delivery process by creating a static file cache, which drastically improves site performance. Now it does a whole lot more…


### Content delivery network (CDN) integration

ProCache now lets you offload all of your site's file assets seamlessly to a CDN. You don't need to make any changes in your site's code, ProCache takes care of it. This lets your server focus purely on delivering the HTML content, while the CDN handles delivery of all the other image and file assets.

The benefits are not just to your server, but perhaps even more-so to the visitor. Most CDNs are regionally focused, enabling them to select the server closest to the visitor to deliver the assets from. This means everything loads more quickly than it otherwise would. Our server is in the US, so every file-based asset had to be sent across the ocean for those of you in Europe (as an example). Now when you load a page at processwire.com, all the images and css/js files are sent to you from a server that is likely only a few miles from where you are.

You can use ProCache with any CDN that supports origin-pull, which includes most CDN services out there. As of this week, all of our file-based assets are delivered from [Amazon's CDN](http://aws.amazon.com/cloudfront/) called CloudFront. We're currently using the free version of it, but with great results so far. I'm convinced that CDN integration is a great upgrade for any site, regardless of how much traffic you get.

[More about ProCache's CDN features](/api/modules/procache/cdn/)


### Built-in HTML minification

Reducing the quantity of bytes that get sent through the pipe helps get content to visitors faster. Though I've never been too big on HTML minification in the past simply because it always seemed to cause lost visual whitespace issues when viewing a page, regardless of what minification library I tried. So I took the time to code one from scratch that worked the way I wanted it to… and didn't make me have to adjust my template files to make them minify-friendly. You can see the results by viewing the source of any page here.

ProCache's HTML minify function performs the expected reduction of unnecessary whitespace and removal of comments in the HTML, but it also provides the following additional options:

- Automatic removal of quotes from HTML attributes when compatible with HTML5 (i.e. for attribute values that don't have whitespace or other characters that require quotes).
- Automatic conversion of XHTML style self-closing tags to shorter HTML5 syntax. That means converting something like `<img src=image.jpg />` to `<img src=image.jpg>` It's a small detail, but every little bit counts.
- Conversion of absolute href attributes to relative href attributes, for when relative is shorter. For instance, if I were to link to the parent of this blog post, it would link to `/blog/posts/`. After HTML minification, it would simply link to `../` – Multiply that over all the links in your output, and you can see significant savings from this conversion.
- ProCache can also be configured to disable minification for logged-in users (or guest users), which can be helpful for development when you need readable HTML source code.
- Minification of inline `<script>` and `<style>` blocks using dedicated JS and CSS minification functions.
- Ability to specify block-level tags where minfication should be skipped. By default, it'll skip minification on `<pre>` and `<textarea>` tags, but you have the ability to specify more as needed.
- Ability to specify `<!--NoMinify--> ... <!--/NoMinify-->` HTML comments to indicate sections of the document that you want the minification to ignore.


### Built-in javascript and CSS merge and minification

ProCache will automatically identify all the CSS and JS references in your document automatically and merge and minify them together. No code changes to your site are required, just check the box to enable and it takes care of it for you.*

In support of reducing HTTP requests, it also identifies assets referenced from your CSS file(s) and base64 encode's them directly into the CSS file. This is mostly beneficial on smaller background images and such, and you can specify the maximum size it should encode in the ProCache settings.

As you would expect, any changes to your site's CSS or JS files are picked up automatically and re-merged and minified immediately, so that you don't have to pay any attention to what's happening behind the scenes.

*Should you prefer it, ProCache also provides API-functions for merge/minify that you can use from your template files.


### .htaccess expires and GZIP directives

Compressing output with GZIP at the server side drastically reduces the number of bytes that get sent through the pipe (perhaps cutting your output size in half or more). And telling the client-side how long to cache assets locally makes a big difference in how many requests are placed upon your server (and thus how long a user spends waiting). ProCache's "Tweaks" tab now includes instructions and examples on optimizing your .htaccess file to maximize the performance of your site.


### Optimization without ProCache

We thought it made sense to keep expanding ProCache to cover a broader and broader scope of site optimizations, but that doesn't mean that you need ProCache to optimize your site.

No post that discusses minification and ProcessWire would be complete without mention of the excellent [AIOM+ module](http://modules.processwire.com/modules/all-in-one-minify/) which provides merge and minification, and has for quite a long time. ProCache's merge and minfication functions are completely different from those in AIOM+, but many of the end results will be similar. In terms of end-user implementation, the biggest difference between AIOM+ and ProCache is that ProCache has the ability to identify your CSS and JS files for merge and minification automatically from your existing HTML output. Though AIOM+ also does something that ProCache doesn't (and likely won't) which is domain sharding.

In terms of optimizing your .htaccess file, look no further than the [HTML5 boilerplate](https://html5boilerplate.com/) .htaccess file. [It contains](https://github.com/h5bp/html5-boilerplate/blob/master/dist/.htaccess) everything you need to know about expires headers, enabling GZIP and more. In fact, ProCache's .htaccess optimizations are largely influenced by those of HTML5 boilerplate.
