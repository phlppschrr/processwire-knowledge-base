# CMS Critic Powered by ProcessWire (again) + Case Study

Source: https://processwire.com/blog/posts/cms-critic-powered-by-processwire-again-case-study/

## Sections


## CMS Critic Powered by ProcessWire (again) + Case Study

9 September 2016 by Ryan Cramer [ 8 Comments](/blog/posts/cms-critic-powered-by-processwire-again-case-study/#comments)

Hey there… I'm [Jonathan Lahijani](http://jonathanlahijani.com/), an independent ProcessWire developer based in Los Angeles. I work directly with design firms, agencies and medium-to-large business and provide white-glove development and maintenance services with an eye for precision. I've built all types of sites with ProcessWire, from [corporate sites](http://www.unitedag.org/) to ecommerce sites that sell [video editing workstations](https://zworkstations.com/). [Email me](mailto:jlahijani@gmail.com?subject=I'm%20interested%20in%20working%20with%20you,%20Jonathan!) to learn more about my services.

I recently had the opportunity to work with Mike Johnston of CMS Critic and Ryan asked if I could share my experience with you this week.


## A Brief History

[CMS Critic](https://www.cmscritic.com/) is a website that many in the ProcessWire community are familiar with as it is (or was rather) powered by ProcessWire and developed by Ryan Cramer, founder and lead developer of ProcessWire. It is a vital source for a large number of individuals and organizations when it comes to honest product and hosting reviews and may be more widely known for its [CMS Critic Awards](https://www.cmscritic.com/awards/) whereby products compete in a variety of categories based on a voting system.

The development history of the site is one that exemplifies a natural progression in technology and solutions. Way back in 2008, Mike Johnston, CMS Critic's creator, developed the website in WordPress and the approach served him well. Given that his business involves reviewing and having a strong understanding of the multitude of competing CMS solutions, it wasn't long before [he discovered and wrote about ProcessWire](https://www.cmscritic.com/critics-choice-for-best-free-cms-goes-to/), which further peaked his interest, particularly after [ProcessWire won the 2012 CMS Critic Best Free CMS Award](https://www.cmscritic.com/critics-choice-for-best-free-cms-goes-to/).

Faced with growing traffic, the wish for a better and more flexible front-end and a desire to reduce dependency on 30+ (!) various WordPress plugins, Mike decided to hire Ryan in mid-2013 to redevelop the site the ProcessWire way. Weeks later, the data was migrated, code was written and the site was [launched](https://www.cmscritic.com/cms-critic-is-now-powered-by-processwire/) with much excitement.

Fast-forward nearly three years later, and... well, [Mike ended up right back where he started](https://www.cmscritic.com/extreme-makeover-cms-critic-edition/). He had a desire to re-architect the website with a new home page, expanded product categories (such as document management systems, hosting, etc.), the ability for vendors to create richer product pages and a more streamlined navigation (with underlying page structure).

There's no question ProcessWire could have handled the new features CMS Critic needed, but given Mike's limited resources, he decided to give it his best shot.


## Plugin *All* the Things!

As a former WordPress developer, I know the excitement that can consume (and ultimately blind) you when you come across one exciting plugin after another. "I'll use plugin A for slideshows, plugin B for forms, plugin C for visual page building, plugin D for custom fields, and Theme E for my frontend" and so on.

**The painful reality is however unless you have an advanced skillset, making these dependencies work nicely and elegantly together, having it be user friendly and having a performant site is extremely difficult.** If any of these plugins output markup and/or styles on the frontend, that's one set of problems. If the plugins conflict with each other, that's another set of problems. If they are updated very rapidly, that's yet another set of problems. If a plugin is extremely popular but has questionable coding practices, the chances of being hacked rises dramatically. Throw in some misuse of pages vs. custom post types, a security plugin and more and more resources get eaten up, conflicts rise and you've entered what I like to call "Plugin Hell".

These were all issues that I had faced in my earlier WordPress years and as my skills and knowledge advanced, the types of plugins I came to depend on were mostly related to the admin side of things. Advanced Custom Fields for custom fields, Simple Page Ordering for re-arranging pages (it's not easy to re-arrange pages with a native WP installation) and perhaps an SEO plugin. I avoided anything that outputted styles as every site I developed was custom designed, so a good starter / barebones theme was the way to go.


## Back to ProcessWire

Back to our story… A couple months went by after the site was re-launched on WordPress and some chatter occurred here on the ProcessWire forums with Mike taking some heat; he got what I'll call "WordPress-shamed", which is defined as the act of being rightly (or wrongly, but usually rightly) ridiculed for using the wrong tool (WordPress in this case) for the job.

All jokes aside, after explaining his decision, he left an open-ended offer to anyone on the forum interested in re-developing his site on ProcessWire yet again, which is when I decided to take action. We worked out a deal and after several weeks of development, caffeine, regular phone calls and judicious use of various migration scripts, the site was re-launched last week.


## The Nitty Gritty Details

This project involved working with the existing installation and codebase that [Ryan had previously developed](/talk/topic/3987-cmscritic-development-case-study/). I must admit that I was a bit nervous in my attempt to fill Ryan's shoes, thinking that there would be all kinds of advanced techniques being utilized which would be difficult to wrap my head around. However after looking at the codebase, templates and fields for no more than 15 minutes, I felt right at home because the techniques and naming conventions that were in place were very similar to what I'm comfortable with. I suppose this is no surprise since I tend to frequent the ProcessWire forums like a hawk, and especially since [Ryan's 10,000+ posts](/talk/profile/2-ryan/) have provided so much direction (in addition to the excellent documentation and well documented source code).

Note: Oftentimes when I go to any online forum, there will usually be a person with an impressive amount of posts. This always catches my attention and speaks to the dedication and time commitment one has put in. This is one aspect that sealed the deal for me in making ProcessWire my go to CMS, which was a lengthy decision.


### Goals

The goals in the remodel included the following:

- work off of the previous ProcessWire site and codebase
- upgrade ProcessWire to 3.0 (was on 2.6)
- heavily modify the taxonomies and URL structure
- improve existing features and develop new features
- completely re-do the frontend of the site using UIkit and a Gulp-based workflow (which I made a video about [here](https://www.youtube.com/watch?v=056XtKAT7yg)).
- take advantage of any new modules ([ProDrafts](/api/modules/prodrafts/), [RepeaterMatrix](/api/modules/profields/repeater-matrix/))
- create user registration capability with a dashboard
- migrate data from the WordPress site
- obtain new hosting


### ProcessWire 3.0

I started off by making a local copy of the previous ProcessWire website (files and database). Once I got that going, I immediately upgraded to ProcessWire 3.0. I didn't hit any issues there other than perhaps 1-2 minor code edits.


### Frontend

It was easy to sell Mike on UIkit as the frontend CSS framework, which I have come to love and now prefer over Bootstrap and Foundation. It's updated more often, has a great selection of breakpoints, uses SASS as the default language which I prefer, and contains a vast amount of components which work seamlessly with each other and that can be selectively enabled/disabled. An added bonus is that Form Builder has an output framework for UIkit, so forms look great and feel cohesive.

I setup UIkit using a Gulp-based workflow which allows for minification and a host of other goodies. To complete the integration, I modified the necessary classes on all the various the HTML elements to match what UIkit expects in addition to modifying some HTML structures. In the process, we switched from a 12 column grid to a 10 column grid (since UIkit doesn't have a 12 column grid by default).

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-frontend.jpg)


### Data Manipulation

Next up was quite a bit of data wrangling with respect to taxonomies and the pages that rely upon them. Some taxonomy items were to be removed, some were to be renamed, some were to be split in two, some were to be put in another taxonomy. These were intricate modifications and data could not be lost. This took quite a few phone calls to perfect since we were thinking it up as we went, but ProcessWire handled it perfectly and data remained intact given the strong adherence to relational data within the CMS. Some changes were handled "by hand" and some were scripted using one-off scripts to make batch changes and save our wrists.


### Widgets

One major new feature was a dynamic widgets system. The previous ProcessWire site had hardcoded widgets but Mike expressed interest in being able to manage these dynamically. With WordPress, you get widgets automatically since it's a native feature, but creating a similar feature with ProcessWire is a snap. The approach I took is nearly the same as the one demonstrated in the [Blog Profile](http://modules.processwire.com/modules/blog-profile/). Simply create a 'widget' template with a Title and Body (and any other necessary fields), then create a page field called 'widgets', assign this page field to any templates that will output widgets, write some template code and logic and that's all there is to it.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-widgets.jpg)


### User Registration

The previous ProcessWire site didn't allow user registration. In an effort to expand the community aspects of the site with product reviews by general users, this was a highly sought after feature and one which we implemented. The registration form was built using the ProcessWire form API and registrations are validated with [Cleantalk](https://cleantalk.org/) [(PHP API)](https://github.com/CleanTalk/php-antispam) to prevent spam accounts (of which there were a myriad of being created post launch before deciding to implement). Lastly, upon successful registration, a user is added to two mailing lists managed by [Sendy](https://sendy.co/) [(PHP API)](https://github.com/JacobBennett/SendyPHP). These third party libraries are being brought in using Composer which ProcessWire works well with. Here's a screenshot of the registration form:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-register.jpg)


### Dashboard

Several different roles exist within the site: general, author and vendor. A regular user has the 'general' role, users who can submit posts have the 'author' role and companies with products have the 'vendor' role.

A convenient place to see one's content makes a great experience and the Dashboard was just the place to house this information. Here's what it looks like from a vendor's point of view:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-dashboard.jpg)


### Page Builder

If a vendor signs up for an advertising package, they should be afforded advanced features to dress up their product page and make their offering stand out among the rest. For example, being able to add accordions, tabs, slideshows and description lists are all advanced structures that a typical rich text editor cannot alone produce.

So how did we solve this problem? [Repeater Matrix](/api/modules/profields/repeater-matrix/) of course. Here it is in action:


### Other Features

The excellent [ProCache](/blog/categories/procache/) module is being used for caching and to handoff the static assets (images, stylesheets, JavaScript) to a CDN. I love that this module is so easy to get going. Here's a speed test result from Pingdom (it scored 94% which is high considering the site has a lot images):

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-pingdom.jpg)

ListerPro is also being used to provide rich listings in the admin interface for Posts and Products.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1073/pw-listerpro-posts.jpg)

[Hanna Code](http://modules.processwire.com/modules/process-hanna-code/) is also being used for inserting complex HTML within rich text editor fields.


## WordPress vs. ProcessWire

Now that we've covered how the site was built, I want to discuss my personal opinions regarding both content management systems and why I chose ProcessWire as my go-to CMS.

I think WordPress is a fine platform and I've worked with it daily (and across a variety of use cases) for over eight years. However, as a web developer who works with numerous talented designers and medium-to-large businesses, every project requires a unique touch, whether it be a completely custom design and/or set of features. Furthermore, the ability for end-clients to **easily** manage their website is a top priority.

With WordPress, I found this to be a difficult endeavor the more complex a site became. Much of this has to do with the opinionated nature of the system which always felt unrefined to me: [The Loop](https://codex.wordpress.org/The_Loop), [the Template Hierarchy](https://wphierarchy.com/), and the lack of a robust custom field system (which is why many advanced WordPress developers rely on [Advanced Custom Fields](https://www.advancedcustomfields.com/)). It didn't help when my sites got repeatedly hacked as well, despite using what I assumed to be safe plugins. It also made me feel uncomfortable when a plugin would insert an awkward menu in the admin.

After evaluating a plethora of CMSs, I came across ProcessWire by chance and was blown away with how trivial it made some complex tasks look, like [creating a set of repeating fields](https://www.youtube.com/watch?v=ynW4pLCgR0M) (which wasn't common in 2012). I then challenged myself to see if I could do everything in ProcessWire that I was comfortable with in WordPress. My comparison table looked like this:

|  |  |  |
| --- | --- | --- |
| **Required Feature** | **WordPress** | **ProcessWire** |
| `Language` | PHP | PHP |
| Rich Text Editor | TinyMCE (built-in) | CKEditor (built-in) |
| Custom Fields | Advanced Custom Fields | Everything is a 'custom field'! (tons benefits come out of this) |
| Page Types | Custom Post Types | Everything is a Page (even Users -- smart!) and pages can have different templates |
| Advanced Content in Rich Text Editor | Shortcodes | [Hanna Code](http://modules.processwire.com/modules/process-hanna-code/) |
| `Query` | query_posts function | `[Selectors](/blog/categories/selectors/)` |
| `Forms` | Gravity Forms | [Form Builder](/blog/categories/form-builder/) |
| Menu Creation | Menus | [Menu Builder](http://modules.processwire.com/modules/process-menu-builder/) (however it's easy to roll own system using fields/templates/pages) |
| `Caching` | WP Super Cache, W3 Total Cache, etc. | `[ProCache](/blog/categories/procache/)` |
| `Blogging` | Posts | Easy to roll own approach (like [Blog Profile](http://modules.processwire.com/modules/blog-profile/)) or the [Blog module](http://modules.processwire.com/modules/process-blog/) |
| `Widgets` | Widgets | Easy to roll own (like with CMS Critic) |
| `Builder` | (there are many 3rd party solutions like Beaver Builder, SiteOrigin Page Builder, etc.) | [Repeater Matrix](/api/modules/profields/repeater-matrix/) (released in 2016) |

ProcessWire passed with flying colors and the [weekly updates](https://github.com/ryancramerdesign/ProcessWire/commits/devns) and the [thriving community](/talk/) sealed the deal.


## The Right Tool for the Job

Much of what I spoke about is from a developer's point of view. Not everyone has this skillset which takes years and a multitude experiences to build up. Sometimes you just need to get a website up quickly and cheaply, or you simply need a blog, and I believe that is where WordPress has much of the appeal (in addition to name recognition). The ecosystem of themes, plugins and hosting solutions is vast, enticing and empowering to those who don't write code. In fact, I would agree with [Jeff Chandler's piece](https://wptavern.com/if-i-switched-publishing-systems-processwire-wouldnt-be-my-first-choice) on WP Tavern about ProcessWire not being a first choice when the person actually developing the site is not a coder.

However one must be cautious of the "Plugin All the Things" approach described above. If a site requires a custom design, high use of custom fields and relational data, speed, security and full control (no opinions on how things should be structured), ProcessWire wins hands down and there are [large](https://discourse.roots.io/) [number](https://github.com/Automattic/_s) of developers who I'd like to see give ProcessWire a shot. It is a blank slate... a white sheet of paper with which you can create exactly what you are looking for without any bloat and a [well thought-out API](../api-full/index.md).
