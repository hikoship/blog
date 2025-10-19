+++
categories = "Tech"
date = "2016-01-29T11:53:01+08:00"
title = "Hugo, GitHub, VPS (2): Write a Hook Listener and Protect It Using Supervisor"
summary = "The article will talk about the first part mentioned in Hugo, GitHub, VPS (1): A Work Flow for static sites."
+++

The article will talk about the first part mentioned in *[Hugo, GitHub, VPS (1): A Work Flow for static sites](/post/hugo-github-vps-1/)*.

## Create GitHub webhooks

GitHub has an [official tutorial](https://developer.github.com/webhooks/) for webhooks, you can follow it and create one easily. The tutorial sets the payload URL to `http://localhost:4567/payload`, but since my hook is deployed on the VPS, I just fill in `http://my.domain:18001`. The port `:4567` and the subfolder `payload` doesn't matter. That's where the *POST* request is sent, and you just need to match it with the port and location of your hook. I preserve the whole `:18001` port for the hook, so I let the request sent to the root path directly.

The content type is `application/json`, and we only trigger the hook for push events.

## Write a hook listener

The tutorial offers a sample listener app written in [Sinatra](http://www.sinatrarb.com), which is a Ruby micro-framework. Unfortunately, I know little about Ruby as well as Sinatra, so I choose to use [Tornado](http://www.tornadoweb.org), a Python framework.

There is a ["Hello, world" example](http://www.tornadoweb.org/en/stable/#hello-world) in Tornado's documents. It has a `get` method in `MainHandler`, and what we want is a `post` method. So delete `get` and write a `post`:

{{< highlight python "linenos=inline">}}
import sys, subprocess

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        # do something
        print('New POST Received.')
        subprocess.call([sys.path[0] + "/generate.sh"])


{{< / highlight >}}

Now, you can run the app and push something to your blog for which a hook has been set, and the terminal will show `New POST Received.`. Then, it executes a shell script called `generate.sh`, which is located in the same folder as the tornado python file. Since we want our VPS to pull down the new source codes immediately and regenerate the static site, so we embed these operations in the script file and make it look like this:

```
#! /bin/sh

cd path/to/blog-repo
git pull
rm -rf public # remove previous output files
hugo # generate the site in public/
```

Then change its authority:

```
chmod +x generate.sh
```

Next, we judge whether the *POST* request is from our GitHub repository. Perhaps the hook is listening to several updates from different users, branches and repos, so let's parse the *json* file and read its information.

{{< highlight python "linenos=inline">}}
import json
import sys, subprocess

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        try:
            repo = data['repository']['full_name']
        except KeyError:
            print('Not a GitHub webhook post')
        else:
            if repo == 'yourusername/yourreponame':
                print('POST from my blog')
                subprocess.call([sys.path[0] + "/generate.sh"])
            elif repo == 'user2/repo2':
                # do something...
            elif repo == 'user3/repo3':
                # do something...
            elif repo == 'user4/repo4':
                # do something

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    // Your configuration
}
{{< / highlight >}}

Finally, we add logging module and filter IP addresses outside GitHub to prevent potentially harmful pseudo *POST* requests. Luckily, GitHub has [a whitelist](https://help.github.com/articles/what-ip-addresses-does-github-use-that-i-should-whitelist/), so we only allow addresses from `192.30.252/22`. Now we've got the whole program:

{{< highlight python "linenos=inline">}}
import tornado.ioloop, tornado.web
import json
import os, sys, logging, subprocess

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        ip = self.request.remote_ip.split('.')
        if ip[:2] == ['192', '30'] and int(ip[2]) >= 252:
            ## GitHub IP range
            try:
                repo = data['repository']['full_name']
            except KeyError:
                logging.warning('Not a GitHub webhook post')
            else:
                if repo == 'yourusername/yourreponame':
                    print('POST from my blog')
                    subprocess.call([sys.path[0] + "/generate.sh"])
                else:
                    logging.info('Unknown repo: %s', repo)
        else:
            logging.warning('Not from GitHub. IP [%s]: %s', ip, data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), # match your payload URL
    ])

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y, %a, %H:%M:%S', filename=sys.path[0] + '/post.log',level=logging.INFO)
    app = make_app()
    app.listen(18001) # match your payload URL
    tornado.ioloop.IOLoop.current().start()

{{< / highlight >}}

## Protect the listener process

In order to let our listener process run consistently in background and reboot after crash, we use [Supervisor](http://supervisord.org/) as a daemon program. Besides, it can manage multiple subprocesses of a tornado app and balance the load with the help of [nginx](http://nginx.org/), but it's unnecessary for a simple hook.

Follow [this direction](http://supervisord.org/configuration.html) to put your `supervisord.conf` file in proper path, and add codes like the following:

```
[program:mylistener]
command=python /path/to/mylistener.py
redirect_stderr=true
stdout_logfile=/path/to/log.log
```

Then, run `supervisorctl reload` to check if `mylistener` has been started.

## Host the blog

Almost all static site generators have their internal server, but you can also use more dedicated web servers such as Apache or nginx for advanced performance and stability, just setting the host path to your output folder in the configuration file.

We are done! Now try pushing something on GitHub, and you should see changes on your VPS.
