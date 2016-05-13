For this ToDoApp project I used Django for the backend and
AngularJS for the frontend.

I enjoyed Django a lot. I had used Flask for a school project
and it was definitely not a good experience because of not
having enough documentation and other issues. With Django the
documentation was superb, creating models, routes, having Class
based and API based views were really great options. Designing
the database didn't take that much time once I got the hang of
Django and understodd the basic concepts such as serializers.
The Django Rest Framework is also a great thing to do CRUD stuff.
Also the Rest Framework comes with a built in database viewer
which came in really handy to test out how my code was working
or not working.

In terms of Angular, when I started it, it looked really beautiful.
But as I went deeper into implementing thing it became harder and
harder, things looked way more complicated than it should be.
Understanding the difference between "factory" and "service" took
me a long time, turns out it's not only me but a lot of people have
a tough time with this. For me "ng-submit" didn't work properly,
so if I wanted to submit something without having a button it wouldn't
do so, hence I had to have a submit button with a link in it.
Also getting the Edit button to work, and when clicked the other
two buttons to show up was a challenge. Right now I have set a timeout
which makes a get request in a set time interval, so if you don't see
something getting created or deleted right away, give it a second or
two and it will work fine. Although the edit works right away.
I thought about using ngResource at one point but then I heard that
sometimes it doens't work the way you want it to, so I just went
with normal $http requests.