# Optimizing 404s in ProcessWire

Source: https://processwire.com/blog/posts/optimizing-404s-in-processwire/

## Sections


## Optimizing 404s in ProcessWire

3 February 2017 by Ryan Cramer [ 7 Comments](/blog/posts/optimizing-404s-in-processwire/#comments)


### ProcessWire 3.0.52

This week our featured topic is on how to optimize 404 requests in ProcessWire. This is a topic that may sound insignificant at first, but is actually quite significant, and offers a lot of benefits when given proper attention, which we'll outline in this post. Like most weeks, we also have a new core dev version ready, 3.0.52. This version doesn't have any new features, but does resolve numerous issue reports from GitHub. As a result, it's definitely worth grabbing. Our focus right now is on getting the dev branch merged to the master, so hopefully 3.0.53 or 3.0.54 will end up as the next master version within the next week or two (which will also include a new 2.8 master). Hope that you enjoy reading this and likewise remember to read the [ProcessWire Weekly](http://weekly.pw) this weekend as well.


## Why optimize 404 requests?

If you've ever looked through your Apache access logs, you probably see a lot of 404s for things that have nothing to do with your site. Often they are from bots that are sniffing for a vulnerability, while consuming your valuable server resources.


### Respecting server resources

You aren't running WordPress, and these 404s are generally harmless in small quantities. But the combined effect of all those thousands of 404s is that they can consume a lot of resources. That's because ProcessWire must render the 404 page for each of them. Meaning, that 404 can take up as much resources as rendering any other page on your site. Further, 404 requests typically can't be cached with tools like ProCache (since they are for URLs that don't exist), so 404s can sometimes be a heavier drain on server resources than legitimate page requests.

It's much better to dedicate your server resources away from irrelevant 404s and towards serving legitimate people and legitimate content. You can do this by creating a static 404 file and making some optimizations to your .htaccess file.


## Getting started


### Creating a static 404.html file

The first step in optimizing 404s is to create a static 404.html file that you can use to power the irrelevant 404s. It's quicker for a server to deliver a static html file than to load up PHP, MySQL and ProcessWire. So our intention is to let irrelevant 404s be handled by a static 404 file, rather than ProcessWire.

To do this, view a bogus URL on your site that will generate a 404, like domain.com/blah/. Then do a "view source" in your browser, copy the HTML, and paste it into a 404.html file on your server in the document root (or root of your ProcessWire installation, if running off a subdirectory).

When ready to set this in place permanently, be sure to see our section on [optimizing your static 404 file](#optimizing-your-static-404-file) at the bottom of this article too.


### Updating your .htaccess file

Now edit your .htaccess file. Near the top you'll see a line that says:

```
ErrorDocument 404 /index.php
```

Change that to to the static 404.html file that you just created:

```
ErrorDocument 404 /404.html
```

After this change, any URLs that ProcessWire doesn't handle will go to the static 404.html file you just created, rather than the more expensive ProcessWire 404 page render. But it would have to be a URL that is considered invalid to ProcessWire, like one with characters that aren't used for ProcessWire page names.

For example, the domain.com/blah/ that we mentioned earlier is a valid URL to ProcessWire, and would still get sent to it. But domain.com/foo bar/ (with the space in it) would get served by the 404.html file instead. That's because ProcessWire doesn't consider a space in a URL to be valid. So the change we made above will filter requests containing characters that aren't consistent with PW page names. But most 404s will still end up getting served by ProcessWire. Given that, we'll want to optimize our .htaccess file further to increase the situations where the static 404.html file is used…


## Filtering out irrelevant 404 requests

Now we're going to get serious about 404s by filtering out URLs that may be valid to ProcessWire, but we know it's never going to need to serve. In doing this, we can really reduce the irrelevant URLs that ProcessWire currently has to render 404 pages for.

Back in your .htaccess file, take a look near the bottom at the last RewriteRule line:

```
RewriteRule ^(.*)$ index.php?it=$1 [L,QSA]
```

Before that line above, we're going to add some more lines to filter out various things. Remember this spot for the following sections, as you'll be placing new lines *above* it.


### Filtering out missing image files

If you aren't using ProcessWire's [$config->pagefileSecure](../../../full/wire/core/Config/index.md) setting (and most sites aren't) then you might want to prevent ProcessWire from serving 404s for non-existent image files. This can cover a large number of 404s, since ProcessWire is not typically used to output image file data.

If you'd like to block these missing images from getting served by ProcessWire's 404 page, place the following *above* the RewriteRule line mentioned earlier:

```
RewriteCond %{REQUEST_URI} !\.(jpg|jpeg|gif|png|svg|ico)$ [NC]
```

What the rule above says is essentially this: “Allow ProcessWire to process this URL only if it DOES NOT END with one of these file extensions.” The “[NC]” at the end just means “Not Case-sensitive”, so it'll work equally well with .jpg, .JPG or .Jpg.


### Filtering out common WordPress files

A common source of potentially malicious 404s is from crawlers looking for vulnerable WordPress installations. They aren't malicious to ProcessWire, but the crawlers looking for them can consume a lot of resources from your server, so it's good to filter them out.

As you probably know, most WordPress files start with "wp-" and end with ".php" (like wp-login.php, wp-admin.php, and so on), so we can filter those out quite easily. Place this line right before or after the previous one that filters out images:

```
RewriteCond %{REQUEST_URI} !wp-.*\.php$ [NC]
```

Or if you prefer, put in a fun placeholder to waste the time of people looking for vulnerable WordPress installations, like this [http://processwire.com/wp-login.php](/wp-login.php).


### Determining what else to filter

The above examples filtering out missing image files and WordPress files are are just that–examples. Now lets get more serious and figure out what's really significant when it comes to 404s in your environment. To do this, we'll need to either look at the server access logs, or log 404s on our own. We'll cover that in more detail further down in this article. But for now, lets look at the problem areas we found.

Below are 404s that were accessed several times as I was writing this post. They all look like they are scanning for vulnerabilities.

```
GET /modules.php?name=Your_Account 404
GET /home.php 404
GET /guestbook.php 404
GET /bbs.cgi 404
GET /gastenboek.php 404
GET /light.cgi 404
GET /Guestbook.php 404
GET /seo-joy.cgi 404
GET /yybbs.cgi 404
GET /aska.cgi 404
GET /jax_guestbook.php 404
GET /default.asp 404
GET /album.cgi 404
GET /processwire.com.rar 404
GET /processwire.com.zip 404
```

ProcessWire has had to waste time serving thousands of requests like these, and I'd like to have Apache filter them out…


### Filtering out irrelevant file extensions

I've decided that any requests that end with the file extensions mentioned above should not be getting served by ProcessWire. I don't use page URLs that end with ".php" or any of the others above when creating my ProcessWire pages, so I feel comfortable excluding them. I've added this line below the other RewriteCond lines we added earlier:

```
RewriteCond %{REQUEST_URI} !\.(php|cgi|pl|asp|rar|zip)$ [NC]
```

If there actually is a .php (or .cgi, .pl, .asp, .zip, .rar) file on the server that we want to allow, then it should still work just fine. The rules we are inserting here don't get visited unless the file requested doesn't actually exist on the server. Our focus is on optimizing 404s after all.

If you've followed along this far and everything is working, congratulations! You've just removed a lot of irrelevant traffic (and thus load) from being served by ProcessWire. Use these same strategies to filter out any other irrelevant file extensions and requests.

*Something to note is that this RewriteRule above effectively cancels the need for the WordPress ("wp-*.php") one we mentioned earlier. So if you are following along with making changes to your .htaccess file, then you can remove that WordPress-specific one, as it's no longer needed. That's assuming you added the one above that filters out .php file (and other) requests.*


## Analyzing 404 requests

An important part of filtering out irrelevant requests is being able to see what 404s are currently consuming your server's resources. The quickest path to this information exists in your server access logs.


### Access logs

Depending on your server environment, the access logs will be in different locations. On my server, they are in /var/log/httpd/. On cPanel-based servers they might be in /usr/local/apache/domlogs/. If not running your own server, they are likely accessible for download from your control panel with your web host. The access log files typically contain "access_log" or "ssl_access_log" in the filename, perhaps accompanied by the hostname.

Once you've located your access logs, search for “ 404 ” and see what you find. I like to use the unix “grep” utility to do this, but you can use whatever text editor or text searching tool you'd like. For the sake of having an example, here's how I do it with grep:

```
grep " 404 " /var/log/httpd/access_log
```

The returned lines would be all of the 404 requests from that log file, which should give you hundreds or thousands of lines to look at.

I like to search with the leading and trailing space like " 404 " because there are usually other lines present in the log files that have 404 as part of some other unrelated number, like 1240412.

After isolating the 404 lines, I'll typically bring them into a text editor or spreadsheet, then filter out everything but the URLs. Then I sort them so that duplicate 404s appear together as a block, and recurring 404s become apparent.


## Building your own 404 logger

Building your own 404 logger in ProcessWire is a useful thing to do because it gives you a picture of what 404 requests ProcessWire is actually serving. Meaning, it can be helpful in analysis both before and after implementing the solutions outlined in this article.


### Recording 404s with ProfilerPro

It's particularly handy to log 404s with [ProfilerPro](/store/pro-dev-tools/profiler-pro/) because it groups and counts them for you, plus it keeps track of how long it took to render each 404, and the combined effect of those times on server resources. To log 404s with ProfilerPro, place the following in your /site/ready.php file:

```
if($page->id == $config->http404PageID && !empty($profiler)) {
  $url404 = $sanitizer->text($_SERVER['REQUEST_URI']);
  $event404 = $profiler->start("404: $url404");
  $wire->addHookBefore('ProcessWire::finished',
    function($e) use($profiler, $event404) {
      $profiler->stop($event404);
    }
  );
}
```

In ProfilerPro you should see your 404 events appear on the "MyPHP" tab, whenever you've got ProfilerPro enabled. Let it run for a day or two and it should give you an excellent picture of any problem areas when it comes to 404s.


### Logging 404s with ProcessWire logs

If you don't have ProfilerPro, the best alternative is to log those 404s using ProcessWire's [$log](/docs/start/variables/log/) API variable. Place the following in your /site/ready.php file:

```
if($page->id == $config->http404PageID) {
  $url404 = $sanitizer->text($_SERVER['REQUEST_URI']);
  $log->save('http404', $url404);
}
```

This will save the URLs of 404 requests to Setup > Logs > http404. Note that this will record a new log entry for every single 404. For this reason, it's best to download the log file and analyze it offline yourself. I like to load them into my text editor or spreadsheet, remove everything except for the 404 URLs, and then sort the file, so that duplicate URLs appear together. While a little more difficult to analyze than with ProfilerPro, this still gives you a decent picture of where the problem areas might be.


## Optimizing your static 404 file


### Make it easy to identify (for yourself)

Lets go back to that 404.html file you just created in the beginning of this article. I recommend making a minor change to that file so that you can differentiate it from your ProcessWire powered 404 page, at least during testing. Otherwise, you probably won't be able to tell if your new 404 rules are working or not.

In my case, I removed a “continue to homepage” link that appears in the bodycopy of the 404 page. That way I know that when I see the “continue to homepage” link, it's the [ProcessWire powered 404](http://processwire.com/blah/), and when I don't see it, it's the [Apache powered 404](http://processwire.com/bl,ah/) (that's using my 404.html file).


### Limit other asset links

It's also worthwhile to limit what other assets your 404 file serves along with itself. For instance, consider limiting or completely omitting linked images, javascript files and any unnecessary css files. Inline any necessary scripts or styles if possible. In most cases, there's little need for a 404 request to launch a bunch of other requests to assets on the server, unless for specific branding or functionality reasons. Though it's worth noting that most crawlers/bots don't bother loading those assets either way.

If using something that merges CSS and JS files into a single file (like AIOM or ProCache), the filename likely changes every time an update is made to the source files. This can be problematic when referenced from a static 404 file, because the originally sourced CSS and JS files may disappear at some point. This is yet another reason to inline the necessary scripts and styles into the 404 document. If that's not possible, you may want to have the 404.html file reference the non-merged/minified versions of these files, so that you don't accidentally end up with a unstyled 404 page.


### Keep it up-to-date

Since many of your 404s will now be served by a static file, it's important to remember that when major site changes take place. You may update or re-create this static 404 file when major navigation or branding changes are made to your website, ensuring that it is up-to-date with your current navigation and branding. It's easy to forget about this static 404 file after getting things setup, so make a note to consider it when major site updates are launched.
