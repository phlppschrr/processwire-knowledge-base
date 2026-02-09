# New API Syntax Options + 2015 Roadmap

Source: https://processwire.com/blog/posts/processwires-roadmap-in-2015/

## Sections


## New API Syntax Options + 2015 Roadmap

26 December 2014 by Ryan Cramer [ 1 Comment](/blog/posts/processwires-roadmap-in-2015/#comments)

Merry Christmas/Happy Holidays to everyone! With the holidays upon us, there haven't been a lot of core changes in the last week (though there were a few), and that's likely going to be the case until we get through the New Year holidays. But even when we're not in the code, we're always thinking and talking about ProcessWire and what we can do to make it better. This week we updated the roadmap to tell you about what's planned for the next version of ProcessWire (2.6). We're also starting to plan and do some work on the next generation of ProcessWire: 3.0, which will be a major focus of 2015.


### What's new in the core this week? New API syntax options!

This week some tweaks were made to ProcessWire's API syntax, which makes for even shorter and cleaner API calls in some cases. Now you can use most ProcessWire API variables as function calls. This is best communicated with examples. Below are examples of several API calls showing the current syntax you might use, followed by the new syntax you can optionally use, that does the same thing.

```php
// Get the 'title' field
$title = $fields->get('title');
$title = $fields('title'); // new

// Get a module
$rss = $modules->get('MarkupRSS');
$rss = $modules('MarkupRSS'); // new

// Get a single page by ID (123)
$p = $pages->get(123);
$p = $pages(123);

// Get a single page by path
$p = $pages->get('/about/contact/');
$p = $pages('/about/contact/'); // new

// Find 10 'product' pages sorted a-z
$a = $pages->find('template=product, limit=10, sort=name');
$a = $pages('template=product, limit=10, sort=name'); // new
```

The above are within the context of a template file. When in the context of an object or a function, API variables (like $pages) are of course not in scope to be accessed directly. But you can prepend `wire()` or `$this->wire()` to any of the above API calls to still use the new syntax. For example:

```
$title = wire()->fields('title'); // in a regular function outside of an object
$title = $this->wire()->fields('title'); // in a Wire-derived object
$title = $this->fields('title'); // in a Wire-derived object (alternate syntax)
```

The above are just examples. You can use any ProcessWire API variable in this manner. You can also use this syntax with any WireArray, which passes along the argument to the WireArray's get() method.

Admittedly, these are only a minor things, and perhaps not necessary at all. But a goal with ProcessWire has always been to offer and provide for the absolute simplest and shortest API syntax possible. So when we see an opportunity to do that (as we did here) we will. Usage is of course completely optional and the existing syntax will still be our primary documented syntax.


### ProcessWire Roadmap for 2.6

If you've been following past posts, you already know that the ProcessWire dev branch has been quite active. What's currently on the dev branch is targeted for ProcessWire 2.6. We're very close to a feature freeze for 2.6 so that we can get this new version out to you on the stable branch as soon as possible. Take a look at the [2.6 roadmap](/blog/categories/roadmap/#processwire-2.6-winter-spring-2015), which includes a list of features many of you may already be familiar with of using ProcessWire's dev branch. In fact, the roadmap is not unlike a changelog at this point.

The biggest additions not yet in place are inclusion of the *ProcessWireUpgrade* and *ProcessWireConfig* modules in the core. These are currently available as separate modules, but we think they belong in the core. However, I do feel that the *ProcessWireUpgrade* module needs FTP installation support before it's core-ready, so that's a major area of focus at present.

[See the ProcessWire 2.6 roadmap here](/blog/categories/roadmap/)


### ProcessWire Roadmap for 3.0

One goal for 2015 is to move forward with ProcessWire 3.0. This version will accommodate some underlying major changes and additions we've been wanting to make for awhile. While the changes and additions aren't visually exciting the way some others might be, they will help to strengthen ProcessWire's foundation for the future, and help us to gain the interest of a broader audience.

These changes/additions include (but are not limited to) support for PHP namespaces, support for multiple instances of ProcessWire in the same request, and support for compiled template files. There will no doubt be a lot more added to that list (and plenty of visually exciting ones too we promise!), but this small list of changes involves some fundamental changes to the core, so this is why they are targeted for a major version change (3.0).

[See the ProcessWire 3.0 roadmap here](/blog/categories/roadmap/#processwire-3.0-fall-winter-2015) (work in progress)


### PW 3.0 Changes: Namespaces

One of the major changes outlined in the ProcessWire 3.0 roadmap is the addition of PHP namespaces. While our current audience isn't particularly interested in this, we think it's an important change as ProcessWire grows. It's also an important change for attracting other developers that may look at the current lack of namespaces, without understanding the reason why, and think that's a reason to overlook ProcessWire. But there are very good reasons for leaving namespaces out…

**Why we haven't had namespaces**

Most users of ProcessWire are web developers creating self contained web sites. Among this audience there are a lot more front-end web developers than PHP coders. Namespaces provide little tangible benefit to this audience, and only in certain scenarios. Yet namespaces make themselves known in every PHP file in rather verbose ways. Working with namespaced PHP code requires a lot of thinking about and coding for namespaces. Now that's just fine for our us, and for module developers. But that's not something we want our primary audience to have to think about when they are developing a site in ProcessWire… unless it suits their need, or unless they want to. Keep in mind that ProcessWire doesn't prevent you from using namespaces at present, if that is your desire. It just doesn't force them upon you.

ProcessWire's template files are native PHP by design. If we use namespaces in our core, then site developers likewise have to use and consider namespaces in their template files. Our experience in PW's design is that most front-end dev's see namespaces as overhead, unnecessary complexity, and a reason to skip right over ProcessWire. Namespaces run counter to our goals with API simplicity, without delivering a tangible benefit to most of our audience.

Lastly, in 2010 PHP 5.2 was still relatively common in web hosting environments. Part of supporting namespaces meant not supporting PHP 5.2 (namespaces were introduced in PHP 5.3). For a new project, we thought there were more growth benefits to offering PHP 5.2 support. Of course, we dropped PHP 5.2 support awhile ago, so this matters little now.

It's worth mentioning that many (most?) other CMS projects don't necessarily have to contend with this issue, because their template files aren't native PHP. So they can happily use namespaces in their core and plugins, without the site-developers having to think about them. But we think the benefits of native PHP template files far outweigh the alternative. ProcessWire's native PHP templates (combined with the API) are one of our core distinctions, and we think it's an important one.

**Why we are migrating to namespaces**

Given the above, you might wonder why we'd even consider adding namespaces to ProcessWire? Well the truth is, our biggest audience is far more important than PHP namespaces, and we wouldn't consider it… unless we could find a way to do it without forcing it upon them. But we also don't want to pursue one audience at the expense of another if we don't have to. We recognize that having to use namespaces may turn off much of our current audience, but lack of them turns off another important part of our audience: PHP developers. We want to grow and support both audiences. This is where one of ProcessWire 3.0's other major additions comes into play: compiled template files.

By default, ProcessWire 3.0 template files will be compiled behind the scenes every time you make a change to them. Your template files will still be native PHP but they'll be updated automatically by ProcessWire to add-in the extra verbosity needed for namespaces. Compiled templates will also bring some nice API benefits beyond this, but we'll get into that later, when we tell you more about compiled templates in a future blog post. But for the sake of this post, the point we're trying to make is that you'll be able to have template files using namespaces without having to think about namespaces… unless you want to. If you declare a namespace in your template file, then ProcessWire will leave it alone. You can also disable the compiled template option on a per-template basis.

Beyond the fact that we can now do it without forcing it on anyone, there are plenty of other reasons to migrate to namespaces. You'll be able to use ProcessWire with other non-namespaced software that you might not previously have been able to. For instance, we've come across a few occasions where people were trying to bootstrap ProcessWire from WordPress because they had to use WordPress for one reason or another, but really wanted ProcessWire's API to manage the data. Yet they couldn't do it because of name conflicts between ProcessWire and WordPress... specifically, with our i18n function calls. When ProcessWire is namespaced, you'll have no problem doing this. Another good reason is Composer support, which will make it simpler for you to pull other projects into ProcessWire, as well as pull ProcessWire into other projects. There are [plenty of other good reasons](http://php.net/manual/en/language.namespaces.rationale.php) to use namespaces as well, but this post is just focused on ProcessWire.

Beyond all of this, I personally have wanted namespaces since the beginning. It was a tough decision to leave them out in the original code base, but it was the right decision. But now we can keep simplifying the API and adopt namespaces without making our users adopt them unless they want to. That leaves no good reason to not have them, and plenty of good reasons to have them. As a result, we look forward to bringing you namespaces in ProcessWire 3.0.
