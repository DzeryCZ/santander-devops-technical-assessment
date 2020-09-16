# Santander DevOps Technical Assessment

## Renamer

### Usage
```bash
USAGE: renamer.py [OPTIONS] DIRECTORY
Renaming all files with configured extension to "<prefix>_<datestamp>_<counter>.<extension>" format
Options:
        -p, --prefix    Prefix of renamed file                  Default: "audiofile"
        -e, --extension Extension of files to be renamed        Default: "wav"

```

## Webserver

### Usage

- Run `docker-compose up -d`
- [Visit Webserver](http://localhost:8080/)
- [Visit Haproxy stats](http://localhost:8080/stats)
- [Visit Kibana](http://localhost:5601/)


## Ubuntu Server

### Usage

- Setup ansible host in `/etc/ansible/hosts`
  ```
  dbinstance ansible_host=<ec2-instance-ip> ansible_user=ubuntu ansible_ssh_private_key_file=<path-to-private-key>
  ```
