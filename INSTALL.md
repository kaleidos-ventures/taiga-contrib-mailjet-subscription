Taiga Contrib MailJet Subscription
=====================================

![Kaleidos Project](http://kaleidos.net/static/img/badge.png "Kaleidos Project")
[![Managed with Taiga.io](https://tree.taiga.io/support/images/taiga-badge-gh.png)](https://taiga.io "Managed with Taiga.io")

Plugin to subscribe and unsubscribe users to the newsletter list in MailJet


Installation
------------

**NOTE:** *Remeber that you need to create a contact list in MailJet and create the contact properties `username` (string), `full_name` (string) and `is_taiga_user` (boolean).*

### Production env

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-mailjet-subscription` with:

```bash
  pip install -e "git+https://github.com/taigaio/taiga-contrib-mailjet-subscription.git@stable#egg=taiga-contrib-mailjet-subscription&subdirectory=back"
```

Then modify in `taiga-back` your `settings/local.py` and include this line:

```python
  MAILJET_API_KEY = "XXXXXXXXXXXXXXXXX"
  MAILJET_SECRET_KEY = "XXXXXXXXXXXXXXXXX"
  MAILJET_CONTACTLIST_ID = "my-contactlist-id"

  INSTALLED_APPS += ["taiga_contrib_mailjet_subscription"]
```


#### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-mailjet-subscription` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/taigaio/taiga-contrib-mailjet-subscription/branches/stable/front/dist" "mailjet-subscription"
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailjet-subscription/mailjet-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailjet-subscription/mailjet-subscription.json"
    ]
...
```


### Dev env

#### Taiga Back

Clone the repo and

```bash
  cd taiga-contrib-mailjet-subscription/back
  workon taiga
  pip install -e .
```

Then modify in `taiga-back` your `settings/local.py` and include this line:

```python
  MAILJET_API_KEY = "XXXXXXXXXXXXXXXXX"
  MAILJET_SECRET_KEY = "XXXXXXXXXXXXXXXXX"
  MAILJET_CONTACTLIST_ID = "my-contactlist-id"

  INSTALLED_APPS += ["taiga_contrib_mailjet_subscription"]
```


#### Taiga Front

After clone the repo link `dist` in `taiga-front` plugins directory:

```bash
  cd taiga-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../taiga-contrib-mailjet-subscription/front/dist mailjet-subscription
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailjet-subscription/mailjet-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailjet-subscription/mailjet-subscription.json"
    ]
...
```

In the plugin source dir `taiga-contrib-mailjet-subscription` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.
