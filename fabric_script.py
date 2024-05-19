from fabric import Connection

with Connection(host='54.210.196.197',
		user='ubuntu',
		connect_kwargs={
			'key_filename':'/root/.ssh/id_rsa',
		},
		) as c:
			#print(c.run('hostname'))
#			c.put('versions/web_static_20240506061201.tgz', remote='/data/web_static/current')
			c.run('tar xf /data/web_static/current/web_static_20240506061201.tgz --directory=/data/web_static/current/')
			c.run('rm  /data/web_static/current/web_static_20240506061201.tgz')
