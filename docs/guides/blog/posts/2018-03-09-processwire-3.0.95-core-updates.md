# Owner Selectors and how to use them (added in ProcessWire 3.0.95)

Source: https://processwire.com/blog/posts/processwire-3.0.95-core-updates/

## Sections


## Owner selectors - ProcessWire 3.0.95 core updates

9 March 2018 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.95-core-updates/#comments)


## ProcessWire 3.0.95

Last week we didn't have a blog post, but there was a [short post](/talk/topic/18606-pw-3094-%E2%80%93-core-updates/) in the forum where I mentioned we might have our next master version ready this week. That post also talked about testing and issue reports in preparation for the next master version—thanks to everyone that's been helping us with that, you are doing great. I've been working on resolving issue reports on GitHub the entire week. We are down to mostly minor details at this stage and we've made a ton of progress, and are very close. But since issue reports are still coming in (even today) we're going to give it at another week here to make sure everything is resolved and that we haven't introduced any new issues in resolving other issues. If it seems like no significant issues are cropping up next week, 3.0.96 will be the next master.

If you want to take a closer look at what has changed in 3.0.95, please see our dev branch [commit log](https://github.com/processwire/processwire/commits/dev), which has seen a lot of activity this week. A couple highlights are numerous tweaks and fixes to AdminThemeUikit, as well as some really nice improvements to our new image Focus+Zoom feature, thanks to the awesome work of Horst (see the long thread of comments in [this commit](https://github.com/processwire/processwire/commit/8fe1eb13f4cbc85c6d5dad093fc559c438c92667) for more, which became kind of or forum for this feature).

This week we'll take a closer look at new feature in ProcessWire that's actually been there for a couple months, but I haven't told you about yet…


## Owner Selectors


### Introducing owner selectors

A few months ago, Antti ([@apeisa](/talk/profile/18-apeisa/)) came to me with a need they ([Avoine](https://www.avoine.fi/)) had for PageTable fields that managed memberships for thousands of members. As I understand it, each member can have multiple memberships to various clubs and associations, and those memberships are represented by PageTable pages (though it could just as well be regular Page fields or Repeater fields too). They often needed to perform find() operations on these membership pages, independently of the member page. But aspects of each member (the owners of the memberships) are part of the matching criteria.

Memberships were not setup as child pages of the member pages, so using "parent.field" selectors weren't an option. Prior to the new owner selectors, if they wanted to find all memberships to a particular golf club, where the membership type was GOLD, and where the members having those memberships were older than 50 years, they had to do something like this:

```php
$members = $pages->find("template=member, age>50");
foreach($members as $m) {
  $items = $m->memberships->find("club='Golf Club X', mtype=GOLD");
  foreach($items as $membership) {
     // add to excel or other export, etc.
  }
}
```

That works, and maybe that's okay at small scale, but the problem is they have hundreds of thousands of members and memberships. So the above example is problematic because it loads many pages they don't even need (the member pages) and it has to load the PageTable field on each of them, and run a find() on it. Basically, it's not efficient, it's slow, and may not even be possible at really large scale.

This is where owner selectors come into play. They let you match aspects of whatever Page reverse references another (whether from a Page field, Repeater field or PageTable field), and make it part of the find() criteria. The above example with finding memberships can now be done like this:

```php
$items = $pages->find("club='Golf Club X', mtype=GOLD, memberships.owner.age>50");
foreach($items as $membership) {
  // add to excel or other export, etc.
}
```

Notice the `memberships.owner.age>50` above. That `owner` part is the important keyword. It is referring to the member pages that have a memberships field that will match the rest of the selector. In this case, it's saying: only include memberships where the member page has an age greater than 50.

*Thanks to @apeisa for the above code examples, and to Avoine for envisioning and sponsoring this feature. The original examples from Antti actually used the lazy-loading version of find() called [findMany()](../../../full/wire/core/Pages/method-findmany.md), which is what they have to use for the scale they are working at (and owner selectors work equally well with them too). *


### Simpler examples with Skyscrapers

If the above example seems a bit difficult to grasp at first, lets look at a couple of simpler examples for using `owner` by going back to our trusty [Skyscrapers profile](http://demo.processwire.com). Each skyscraper page has an "architects" field that is a Page field referencing one or more architects that designed the skyscraper. (Basically, when you are [editing a Skyscraper](http://demo.processwire.com/admin/page/edit/?id=4184), you've got a field where you can select which architects designed it).

Lets say that we want to find all architects that have designed skyscrapers with a height taller than 1000 feet:

```php
$pages->find("template=architect, architects.owner.height>1000");
```

The result is a PageArray of 29 architects that have designed skyscrapers more than 1000 feet in the USA. But lets say instead that we want a list of architects that have designed skyscrapers in the city of Atlanta:

```php
$pages->find("template=architect, architects.owner.parent.name=atlanta");
```

Just in case you aren't familiar with the Skyscrapers profile, each skyscraper is a child page of a city page (i.e. [/cities/atlanta/bank-of-america-plaza/](http://demo.processwire.com/cities/atlanta/bank-of-america-plaza/)), which is why we were able to use `parent.name=atlanta`. If it were instead in a Page field called something like "city", then we would have used `architects.owner.city.name=atlanta`.

Lets say we want to combine the two above and find all architects that designed skyscrapers in atlanta greater than 1000 feet:

```php
$items = $pages->find(
  "template=architect, " .
  "architects.owner.parent.name=atlanta, " .
  "architects.owner.height>1000"
);
```

Here in Atlanta we have just 1 skyscraper more than 1000 feet (Bank of America Plaza), and that matches 1 architect for that building (Kevin Roche), so our $items contains the architect page for Kevin Roche. If we run the same search on a city like Chicago or New York (that have a lot of tall skyscrapers), then we get a lot more architects returned.

This is one of those features that some people really need a lot, and others might never use. Though even if you don't need it now, you might find it very handy at some point. When you find this useful, please let us know how you are using it. I'll be writing documentation for it on the site soon, and would like to include other real-world examples.


### Happy 200 to the ProcessWire Weekly

If I'm reading it correctly, tomorrow will be the 200th issue of the ProcessWire Weekly! That's really amazing. Congratulations to Teppo—thank you for all of your awesome writing, research and insights that you share with us every week in the ProcessWire Weekly, I am so grateful. Reading the [ProcessWire Weekly](http://weekly.pw) is the highlight of every week for me and the entire ProcessWire community.
