`docker build -t cron-i .`
`docker run --name cron-c -v ./cron.log:/var/log/cron.log cron-i`