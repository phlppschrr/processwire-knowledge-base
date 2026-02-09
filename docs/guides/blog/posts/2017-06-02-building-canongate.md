# Building the Canongate website with ProcessWire

Source: https://processwire.com/blog/posts/building-canongate/

## Sections


## Building the Canongate website with ProcessWire

2 June 2017 by Ryan Cramer [ 4 Comments](/blog/posts/building-canongate/#comments)

Hi I’m [Alex Capes](http://alexcapes.com/), a freelance web developer based in London. I work with design agencies and directly with clients to create user-friendly web experiences. I made the switch from Wordpress to Processwire around 5 years ago and haven’t looked back. If you have a project you’d like to talk about, [I’d love to hear from you](http://alexcapes.com/).

I recently worked with design agency [Human After All](http://www.humanafterall.co.uk/) to build a website for leading independent book publisher [Canongate Books](https://canongate.co.uk/). Founded in 1973 in Edinburgh, Canongate has [a rich history](https://canongate.co.uk/about/) of publishing landmark works of fiction, including Alasdair Gray’s masterpiece [Lanark](https://canongate.co.uk/books/28-lanark-a-life-in-four-books/) and Yann Martel’s [Life of Pi](https://canongate.co.uk/books/318-life-of-pi/), amongst [many others](https://canongate.co.uk/books/all/).

This was a fairly large-scale project that began in the summer of 2016 with discovery/UX workshops. I began initial prototyping in October 2016, with full development work starting in January 2017. The site was launched on May 18th 2017.

The build included some unusual challenges ([XML data feed](#data-feed)) and some very familiar ones ([page load speed](#speed)). This post hopefully gives you a bit of insight into how I tackled these challenges. There are many aspects to this project that not covered here, so if you’d like to know more please [drop me a line](http://alexcapes.com/).


### Data feed

The major technical challenge I faced was importing book data into Processwire via an XML data feed — still [an industry standard](http://www.editeur.org/83/Overview/) in the world of book publishing.

The initial back-catalogue dump of data consisted of 1000+ books, each with multiple editions (60mb+ of XML files!). Ongoing updates to the catalogue (up to 300 book updates) would be delivered nightly to the server and updated via a cron job.

I began to trawl through the web to figure out how to get PHP and large XML files working nicely together.

Initial attempts using [PHP SimpleXML](http://php.net/manual/en/book.simplexml.php) ended in dismal failure. Working with such large files caused memory issues due to SimpleXML loading everything into the memory before being accessible via PHP.

The solution seemed to be [XMLReader](http://php.net/manual/en/book.xmlreader.php), but the trade-off here was working with complex and often unreadable code. I felt at this point that I might have reached an impasse.

Fortunately I came across [this clever method](https://rythie.com/blog/blog/2011/02/27/using-a-hybrid-of-xmlreader-and-simplexml/) combining the readability of SimpleXML with the ability of XMLReader to handle large files by iterating through each item in the XML before exporting each one in turn to SimpleXML.

After some tests I was able to successfully import XML files up to 5mb. Beyond this limit there were still server timeout issues, but the solution was good enough for the nightly updates, while the initial data dump could be split into manageable chunks.

Once the data was accessible, it was relatively straightforward to use the Processwire API to create/update pages for books as well as pages within a PageTable field for each edition.

The site now runs a nightly cron job via SSH to pick up new books/update editions. At the time of writing, the site has over 1100 books and 2100 editions.


### Speed

Making sure a website loads quickly is always a challenge with every project.

Processwire has some great in-built caching, but I highly recommend [ProCache](/blog/categories/procache/) — I’ve used it for nearly every single install since I started working with Processwire.

One big advantage of ProCache is in-built support for CDN delivery of resources. On this project, all images/CSS/JS files are delivered via Amazon CloudFront. Setting it up is [extremely easy](/api/modules/procache/cdn/#configuring-a-cdn-with-procache) too.

As well as serving cached pages, ProCache is also minifying the HTML, combining and minifying JS/CSS files to reduce DNS lookups, and adding all the rules to the .htaccess file for performance optimisation from expires headers to GZIP compression.

ProCache is great way to supercharge your site with very little work or advanced expertise.

Alongside ProCache, I also installed [Google’s PageSpeed](https://modpagespeed.com/) on the server and set it to “[Optimize for Bandwidth](https://modpagespeed.com/doc/optimize-for-bandwidth)”. This setting gives you the benefit of many of PageSpeed’s features with a lower risk of breaking anything on your site (I’ve done this on numerous occasions with PageSpeed). PageSpeed has a lot of advanced options, a lot of which are a bit over my head, but I’ve found over time that there is a law of diminishing returns the further you get into it.

Combining ProCache and PageSpeed made a massive increase in performance: page load times reduced from 3-4 seconds to often below 1 second.

Another performance challenge was to deal with print-quality book cover images delivered via the feed, some of which were > 5000px wide.

Initial tests showed the standard GD image library was really struggling with resizing the book covers. Initial page loads when creating image variations were > 30 seconds.

Thankfully [Processwire 3+ has support for ImageMagick](/blog/posts/processwire-3.0.10-expands-image-resize-options/), which is a core module but not installed by default. ImageMagick was able handle the large images without any fuss, resizing each one for multiple screen sizes/resolutions, and bringing down the initial load time when creating variations to a more manageable 5-6 seconds.

If you can, I highly recommend installing ImageMagick on your server and enabling it in Processwire. If you’re not sure about installing it, ask your hosting provider — it may already be installed.


### The Result

“.. our new website feels like it does justice to the range of brilliant writers we publish, the style with which we like to present their books to the world and the attitude that underpins this fiercely independent publishing house.” –Jamie Byng, CEO Canongate

The site was a major upgrade for the client, with the bold decision made early on to stop selling their books directly via the website and to instead focus on offering [“deeper, more immersive connections between reader, story and author”.](http://www.thebookseller.com/news/canongate-unveils-website-redesign-555106)

The use of Processwire as a CMS was a big part this upgrade, with the previous site using an unwieldy combination of Magento and Wordpress.

Much of my development work involved making sense of a lot of data — from dealing with the XML feed and optimising page load times to developing a front-end/back-end with Processwire that was simple and user-friendly for the client and end users. Again, working with Processwire made these goals much easier to achieve.

I offer my thanks to Ryan, and also to the Processwire community for all the times I couldn’t get things working as I wanted. Special thanks go to [Robin S](/talk/profile/2897-robin-s/) for so often pre-empting my code conundrums with [modules that solve them](http://modules.processwire.com/authors/robin-s/).
