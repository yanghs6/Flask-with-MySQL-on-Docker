# Flask with MySQL on Docker

---

- [Summary](#summary)
  - [Content](#content)
  - [Author's environment](#authors-environment)
- [How To Work](#how-to-work)
  - [Set up environment](#set-up-environment)
  - [Set MySQL](#set-mysql)
  - [Set Simple Flask App](#set-simple-flask-app)
  - [Make docker-compose.yml](#make-docker-composeyml)
  - [RUN!](#run)
- [Reference](#reference)

---

## Summary

### Content

This repository is test for Flask with MySQL on Docker.

Just Do It, and Enjoy!

### Author's environment
- MacOS: 13.0.1 
- Python: 3.10.6
- MySQL: 8.0.31
- Docker: 20.10.17

---

## How To Work

![img](img/markdown/Docker%20Flask%20with%20MySQL.drawio.png)

### Set up environment
1. Install Python and Flask Library
   - Python \[[download](https://www.python.org/downloads/)\]
   - Flask \[[download](https://docs.conda.io/en/latest/miniconda.html)\]

2. Install MySQL
   - \[[download](https://dev.mysql.com/downloads/installer/)\]

3. Install Docker
   - Window \[[download](https://docs.docker.com/desktop/install/windows-install/)\]
   - MacOS \[[download](https://docs.docker.com/desktop/install/mac-install/)\]
   - Linux \[[download](https://docs.docker.com/desktop/install/linux-install/)\]

### Set MySQL
1. Make init sql
    - example (./02_db/init.d/01_init_db_table.sql)
        ```sql
        -- Use flask DB
        USE flask;

        -- Create Table
        CREATE TABLE emp (
            empno CHAR(20) NOT NULL,
            name CHAR(20) NULL,
            department CHAR(40) NULL,
            phone CHAR(14) NULL,
            PRIMARY KEY (empno)
        );
        ```

### Set Simple Flask App
1. Make app.py

2. Make template html

3. Add sql configuration

### Make docker-compose.yml
1. Set Flask container named "app"

2. Set MySQL container named "db"

3. Set links, depends_on, deploy option on db app container

### RUN!
1. Move root directory and run command: ```docker compose up```

2. Access Flask app: http://127.0.0.1:5005/

3. Stop command: ```docker compose down```

---

## Reference
1. Try Docker Compose, https://docs.docker.com/compose/gettingstarted/
2. Differenct between docker compose and docker-compose, https://stackoverflow.com/questions/66514436/difference-between-docker-compose-and-docker-compose
3. Docker Compose vs Docker-Compose, https://www.reddit.com/r/docker/comments/mmfr5p/docker_compose_vs_dockercompose/
4. [Docker Compose] Build Docker Compose in Go, https://github.com/docker/roadmap/issues/15
5. MySQL 8.0 Reference Manual CREATE USER Statement, https://dev.mysql.com/doc/refman/8.0/en/create-user.html#create-user-overview
