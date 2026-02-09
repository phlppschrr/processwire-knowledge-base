# How to use multi-instance in PW 3.x

Source: https://processwire.com/blog/posts/multi-instance-pw3/

## Sections


## How to use multi-instance in PW 3.x

12 August 2016 by Ryan Cramer [ 13 Comments](/blog/posts/multi-instance-pw3/#comments)


## ProcessWire 3.0.30 and 2.8.30

This week work continued on preparing 3.x (and 2.8.x) for release. One of the features of 3.x that we'd not yet covered in much detail was the multi-instance support. So the primary focus this week was in making sure we clarified and simplified some things in that respect. This post covers all the details. In addition we've also got some $session updates that we think you'll like!


## Using multi-instance in PW3

One of the things new to ProcessWire 3.x is multi-instance support. What this means is that you can create multiple instances of ProcessWire from the same code. You can pull or manipulate data from one instance into another and vice versa. This is particularly useful when you've got multiple ProcessWire installations in the same environment and you want them to be able to share data. It's a simpler, more efficient and powerful alternative to using feeds and web services (though obviously less portable).


### Usage environment

When using multi-instance in a web environment, typically you'll have a master instance that is serving a page, and the template file [used by that page] that creates another instance of ProcessWire (pulling from another local installation). For instance, on our server we have the main site (you are here), and we've got 4 other ProcessWire installations for the [modules site](http://modules.processwire.com), [directory site](http://directory.processwire.com), [cheatsheet site](http://cheatsheet.processwire.com), and [demo site](http://demo.processwire.com).

Prior to multi-instance support, the only way these sites could share data was by pulling from feeds (like RSS feeds), and indeed we've done quite a bit of that. But with multi-instance support, any one of these installations can boot up another and have access to the entire ProcessWire API of that installation (where file permissions permit).

Another environment for multi-instance is from a PHP script (or shell script) running on its own. It can create and connect to as many ProcessWire installations as are visible to it. The same goes for instantiating ProcessWire from another software (like another CMS). In this post, we'll primarily focus on the environment described by the previous paragraph. However, note that everything mentioned here applies to either environment. The primary difference is that if your environment isn't already within ProcessWire, then you would need to include/require ProcessWire's core file first, like this:

```
require('/path/to/wire/core/ProcessWire.php');
```

You also have the option of letting the Composer autoloader handle it instead. PW3 isn't yet up on Packagist, but will be after it's in master release.


### How to create a new instance

To connect to and create a new instance of ProcessWire, you need to know where it is located on the file system. The directory you provide can either be to the root of the installation (where PW's index.php file resides) or to the /site/ directory of the installation (where the config.php file resides). That's all you need to instantiate that site:

```
$site = new ProcessWire('/path/to/www/');
```

While optional, we also recommend providing the URL to the installation as the second argument (preferably including the scheme and hostname). That way if you make any [$page->url()](../../../full/wire/core/Page/method-url.md) or [$page->httpUrl()](../../../full/wire/core/Page/method-httpurl.md) calls, it will know where to point them to:

```
$site = new ProcessWire('/path/to/www/', 'http://domain.com/');
```

Once you've got your ProcessWire instance ($site), you can access the entire API of that ProcessWire installation. For example:

```
$newestPages = $site->pages->find("sort=-created, limit=3");
```

That's a simple example above (finding the 3 newest pages), but that's just to communicate that "you have access to the API". Meaning, you have access to the *entire* API of that installation. But rather than accessing an API variable such as [$pages](../../../full/wire/core/Pages/index.md) via `$pages` or `wire('pages')`, you access it through `$site->pages`, where $site can be whatever variable name you've assigned the instance to.

A couple of things to note if you are booting a ProcessWire installation from a non-ProcessWire installation. First would be that you'll need to include/require the core ProcessWire.php file (as described in the previous section). Next would be that, assuming you aren't already in the ProcessWire namespace, you'd need to identify that namespace when creating the new instance, i.e.

```
$site = new \ProcessWire\ProcessWire('/path/to/site/');
```


### Live example

The following data is being pulled directly from [modules.processwire.com](http://modules.processwire.com) (a separate ProcessWire installation) using multi-instance, every time this page is rendered. This examples lists the 5 newest modules added to the directory. Following this example, you'll see the actual code used to deliver it.

newest-modules


### Code used in the live example

Below is the exact code used to create the new ProcessWire instance (to modules.processwire.com) and produce the output shown above. This code appears in the blog-post template that is rendering this page you are reading now.

```
// Server path to the PW installation
$path = '/home/modules/www/';

// The root URL for the PW installation
$url = 'http://modules.processwire.com/';

// Create a new ProcessWire instance
$site = new ProcessWire($path, $url);

// Find the 5 newest items in modules directory
$items = $site->pages->find("parent=/modules/, limit=5, sort=-created");

// output list
foreach($items as $item) {
  echo "
    <p>
      <a href='$item->httpUrl'>$item->title</a><br />
      $item->version <em>by $item->author</em><br />
      $item->summary
    </p>
    ";
}
```


### Pitfalls and considerations

Multi-instance support has not seen much broad use yet, so we'll be keeping this particular feature in beta even after 3.x is officially released. If you opt to use multi-instance support, please keep the following in mind:

As you can see, there are a lot of potential pitfalls, so use care with multi-instance. However, we suspect many will be using multi-instance simply as a way to pull data in a read-only manner, and in that context you shouldn't have to worry about much.


### Future multi-instance goals

Currently multi-instance requires that the PW installation are local and accessible on the file system. In the future, we'd like to extend this so that multi-instance can work over http in some respect. Meaning, you could make two completely independent PW installations on different servers talk with each other via the ProcessWire API. For instance, imagine if I could do this from here on processwire.com:

```
$tripsite = new ProcessWire("https://www.tripsite.com"); 
$tours = $tripsite->find("template=tour, country=Austria");
```

Currently to do stuff like this, I usually setup JSON web services and feeds. While it's not hard to do, it can be time consuming. If I could just make two PW installations talk to each other via the API instead, it would be a game changer. We're a long way off from this still, but it's fun to dream about.


## More session control

Something small (or large, depending on your point of view) that was added this week is the ability to disable sessions. ProcessWire has always maintained sessions when delivering pages, which makes life simple for us. If we want to get or set some session data, we just use the [$session](../../../full/wire/core/Session/index.md) API var and everything is ready to go.

But there are cases where maybe you don't want sessions to be active. For instance, sessions require a cookie on the client side, and maybe you don't want to set a cookie because of some law that says you have to have user consent. Or maybe your site is simple and you have absolutely no use for sessions. Or maybe some other reason. Whatever the reason, it's now supported in ProcessWire 3.0.30 via the `$config->sessionAllow` configuration property.

This configuration property may be set to a callable function that returns boolean (true or false) as to whether or not to allow sessions for the current request. Initializing the session is one of the first things that ProcessWire does, before determining the current page or user. So the callback function has to rely on what can be determined without the ProcessWire API, in order to determine whether a session is allowed or not.


### Usage and example

Below is an example of using the `$config->sessionAllow` property. This example would go in your /site/config.php file. In this example, we allow sessions if a session cookie is already present, or if the requested URL looks like an admin URL. Otherwise we disallow sessions. This would have the effect of disabling sessions for an entire site, except for admin URLs, or for users that are already logged in. This callback function is provided a single argument, which is the [$session](../../../full/wire/core/Session/index.md) API variable.

```
$config->sessionAllow = function($session) {

  // if there is a session cookie, chances are user is logged in
  if($session->hasCookie()) {
    return true;
  }

  // if requested URL is an admin URL, allow session
  if(strpos($_SERVER['REQUEST_URI'], '/processwire/') === 0) {
    return true;
  }

  // otherwise disallow session
  return false;
};
```

Hope that you all have a great weekend. See you at [ProcessWire Weekly](http://weekly.pw) tomorrow!
