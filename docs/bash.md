#### subprocess for special commands
```python
import subprocess

def run_bash_cmd(cmd):
  process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  return output

run_bash_cmd("fswebcam -r 640x426 image.jpg")
```

#### sh
```python
import sh

print sh.pwd()
print sh.cd('/path/to/Development')
print sh.ifconfig("wlan0")
run = sh.Command("/home/amoffat/run.sh") # Absolute path
run()
sh.tar("cvf /tmp/test.tar /my/home/directory")
```

#### os
```python
import os
# Get working directory
print os.getcwd()
# Check whether file exists
print os.path.isfile(filepath)
```

#### example
```python
```

#### example
```python
```

#### example
```python
```
