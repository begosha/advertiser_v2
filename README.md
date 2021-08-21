# advertiser_v2

To install and run this project you need to install postgres, python >3.7, pip and virualenv

Clone the project to your local dir

The project is based on PostgreSQL. You will need to create new database for this project:

```
~$ sudo -u postgres psql

postgres=# CREATE DATABASE <your_db_name> WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8';

postgres=# ALTER DATABASE <your_db_name>  OWNER TO <your_desired_user>;

```

After you create database, you need to create new .env file in the directory where you cloned the project. Populate .env file with the following data:

```
DEBUG={your_value}
SECRET_KEY={your secret key}
DB_NAME={your db_name}
DB_USER={your db_user}
DB_PASSWORD={your db_user_password}
DB_HOST={your db_host}
DB_PORT={your db_port}
```

Create virtual env with following command: 

```
~$ virtualenv -p python3 venv
```

Activate your virtual env using command: 

```
~$ source venv/bin/activate
```

then change directory to source
```
~$ cd server
```

Install all dependencies by following command:

```
~$ pip install -r requirements.txt
```

Apply migrations:

 ```
~$ ./manage.py migrate
```

Now you can launch the project locally using the command

 ```
 ~$ ./manage.py runserver
 ```

