Smart Repo
----------


# How to use

## Add application

```
$ curl --header "Content-Type:application/json" -X POST http://127.0.0.1:8000/applications/  --data '{"ID":"tst" ,"name":"test application1"}'
```


## List all applications
```
$ curl http://127.0.0.1:8000/applications/
```

## List all builds for an application
```
$ curl http://127.0.0.1:8000/applications/tst/
```


## List all builds for an application with tag
```
$ curl http://127.0.0.1:8000/applications/tst/latest/
```

## Add builds to application
```
$ curl --header "Content-Type:application/json" -X POST http://127.0.0.1:8000/builds/ --data '{"application":"tst" , "branch":"master", "commitId":"abcde123456", "tag":"latest", "location":"sha256:7ae21864752174ddf1df5de6182bfef018699018e75a6342dd2f154a04bf829b"}'
```

## Get build details
```
$ curl http://127.0.0.1:8000/builds/1/
```

## Update build info
```
$ curl --header "Content-Type:application/json" -X PATCH http://127.0.0.1:8000/builds/1/ --data '{"tag":"latest,tested"}'
```

