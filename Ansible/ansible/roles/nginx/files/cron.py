from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/service_state')
job.minute.every(1)
cron.write()