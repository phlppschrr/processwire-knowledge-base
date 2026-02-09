# ProcessWire 3.0.12 adds support for extended page names

Source: https://processwire.com/blog/posts/page-name-charset-utf8/

## Sections


## ProcessWire 3.0.12 adds support for extended page names

18 March 2016 by Ryan Cramer [ 6 Comments](/blog/posts/page-name-charset-utf8/#comments)


## ProcessWire 3.0.12


### Extended Page Names

[ Download](https://github.com/ryancramerdesign/ProcessWire/tree/devns)

**ProcessWire now supports the ability to use extended (UTF-8) page names, meaning your URLs can now have just about any characters that you want! (look at your address bar, for example)**

One of ProcessWire's key points is its multi-language capability. I've recently heard from several people (including two this week) that have been wanting URLs that aren't limited to the world of ASCII. So I thought it was time to move forward with this capability. After all, there's nothing particularly multi-language about ASCII, as its foundations are in English, and ProcessWire is for any language.

ProcessWire 3.0.12 adds support for extended page names. And by that I mean page names and URLs that can have characters outside of the traditional a-z 0-9 ASCII set.

One of the main reasons we've stuck with ASCII-only URLs up until this point is not as a matter of language, but as a matter of security and limiting the scope of input. Though UTF8 URLs and internationalized domain names still aren't all that common on the web, at least not as far as I can tell. But because our primary interest is in securing the inputs, our approach to supporting these URLs is not about supporting the entirety of UTF8, but rather about supporting UTF8 characters that are both in a configurable whitelist, and supported by the [IDN standard](https://en.wikipedia.org/wiki/Internationalized_domain_name).

Page names and paths aren't domain names of course (IDN implies domain name), but we are using the same IDN standard to validate them and best ensure our URLs using UTF8 remain as secure and portable as possible. Basically, we're taking kind of a cautious approach, which I think is always a good thing to do when venturing into something new like this.


## How to use extended page names

Extended page names aren't enabled by default and currently we consider them experimental in ProcessWire. But for those interested, here's how to get up and running with them. You'll need ProcessWire 3.0.12 or newer to utilize extended page names.

If you are using ProCache: *We are testing an update for ProCache that supports extended page names (and it's being used on this page). We'll have this available for download in the ProCache board early next week.*


### 1. Add the following to your /site/config.php file.

This is your way of telling ProcessWire that you intend to use UTF8 for your page names, rather than ASCII.

```
$config->pageNameCharset = 'UTF8';
```


### 2. Add the following whitelist to your /site/config.php file.

This is the "whitelist" of UTF8 characters that you want to allow in URLs. You may want to update this whitelist specific to the language you intend to support, though the one below should support many of the languages that PW is already used in.

```
$config->pageNameWhitelist = '-_.abcdefghijklmnopqrstuvwxyz
0123456789æåäßöüđжхцчшщюяàáâèéëêěìíïîõòóôøùúûůñçčćďĺľńňŕřšť
ýžабвгдеёзийклмнопрстуфыэęąśłżź';
```

The above MUST be placed all on one line, and is on multiple lines here only for readability.

Note: the above is the default whitelist value. If you don't need to make any changes to it, you can simply leave it out of your /site/config.php file.


### 3. Get the newest PW .htaccess file and modify it.

The [.htaccess file](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt) in 3.0.12 contains a couple of updates that you'll need. *If you want to update your existing .htaccess file rather than replace it, see the bottom of this post for instructions. *

Locate [directive 16a](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L172) (near the bottom of the file) and comment it out by placing a `#` at the beginning of the line. What we are doing here is disabling the .htaccess limit on only allowing ASCII URLs to pass through to ProcessWire.

```
# RewriteCond %{REQUEST_URI} "^/~?[-_.a-zA-Z0-9/]*$"
```


### 4. Also make this update to your .htaccess file.

Below the above directive (16a), you'll see [directive 16b](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L179), which contains the alternative to the one you just commented out. Un-comment that directive by removing the `#` from the beginning of the line that it is on. This is what it looks like (minus the line wrapping):

```
RewriteCond %{REQUEST_URI} "^/~?[-_./a-zA-Z
0-9æåäßöüđжхцчшщюяàáâèéëêěìíïîõòóôøùúûůñçčć
ďĺľńňŕřšťýžабвгдеёзийклмнопрстуфыэęąśłżź]*$"
```

The above MUST be all on one line, and is on multiple lines here only for readability.

Note: if you added any characters in step 2, go ahead and add them to the above line too, after the "ź" character at the end, but before the "]".


### 5. You are ready to use extended page names and URLs!

Simply edit any page or create a new one, and you now have a much broader character set available for your page URLs.


### For those that want to update an existing .htaccess file

Step 3 above mentions grabbing the latest .htaccess file from PW 3.0.12. But that's sometimes easier said that done, because you may have a customized .htaccess file at this point. If that's the case, substitute the following for steps 3 and 4 above.

Update the [two version lines](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L3) at the top to reflect ProcessWire 3.x:

```
# @version 3.0
# @indexVersion 300
```

Comment out [these lines](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L130) you see below by placing a "#" at the beginning of each line (like you see in the [link](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L130)).

```
# Comment out these lines 
RewriteCond %{REQUEST_URI} "[^-_.a-zA-Z0-9/~]"
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php?it=/http404/ [L,QSA]
```

You will have one or two lines in your .htaccess file that look like [the following](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L177):

```
RewriteCond %{REQUEST_URI} "^/~?[-_.a-zA-Z0-9/]*$"
```

Replace that line (or lines, if more than one) with [the directive](https://github.com/ryancramerdesign/ProcessWire/blob/devns/htaccess.txt#L185) you see below, but make sure it all stays on one line (unlike below). Feel free to update the list of whitelisted characters consistent with your own needs.

```
RewriteCond %{REQUEST_URI} "^/~?[-_./a-zA-Z
0-9æåäßöüđжхцчшщюяàáâèéëêěìíïîõòóôøùúûůñçčć
ďĺľńňŕřšťýžабвгдеёзийклмнопрстуфыэęąśłżź]*$"
```

Thats it! Have a great weekend, read the [PW Weekly](http://weekly.pw), and be on the lookout for more PW updates plus a FormBuilder update next week.
