
** ⚠️⚠️⚠️ Alert ⚠️⚠️⚠️**

I created a similar project [visitor-badge](https://github.com/jwenjian/visitor-badge) and hosted on the [glitch.com](https://glitch.com) to avoid the free hours limitation in heroku.

So I will archive this project and migrate the current data to new project one by one.

Please switch to new project and **use the same repo_id value as page_id parameter**, I will migrate the current data one by one. After that, I may stop deploy this project to heroku.

Sorry for the inconvience and hope you have a better experience with the new project.

Any question please [open a new issue](https://github.com/jwenjian/visitor-badge/issues/new) on new project.

---

**[Note] Since the app is deployed in heroku free plan, 500 hours is not enough for everyone's use, fork and deploy under your own account is recommended!**

---

# visitor-count-badge

A badge generator for count visitor of your README, it support 2 endpoints now:

1. total.svg
> count total visitors to your README or Issue

2. today.svg
> count visitors only in current day(server timezone), and be noted: this will **NOT** increase the total count

## Demo
See below badge, try to refresh current page then see again :tada:


## Website
Click [here](https://visitor-count-badge.herokuapp.com) to visit index page which will shows you:

- repos with top 10 total visitors
- repos with top 10 visitors within each day
 
## Install dependencies

1. `pip install -r requirements.txt`

## IDE run
`FLASK_APP=main.py flask run`

## How to use

Add a image to your README file:

```markdown
![Total visitor](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=)
![Visitors in today](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=)
```

in which:

`repo_id`:

An unique string represent your current README, recommend as following pattern

- For README:

{your.github.login}.{your.repo.id}, for example: repo_id=`jwenjian.ghiblog`
