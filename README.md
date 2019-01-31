1) **Install python requirements**
    ```
   pip install -r requirements.txt
   ```

2) **Install linux requirements**
    
    To obtain a password, the script uses the **pass** utility. Please, install [pass](https://passwordstore.org).

3)  **Fill config file**

    Configure the configuration file `config.ini`
    - `username` - it is your SFTP username.
    - `password_path` - it is path to your SFTP password in **pass** storage.

4)  **Install flameshot**

    Information about installation you can found in [official github repository](https://github.com/lupoDharkael/flameshot#installation)



### Usage
```
flameshot gui -r | python main.py
```


### Tips

To use this script to run the hotkey, just create a bash file:

```
#!/bin/bash
flameshot gui -r | /path/to/python /path/to/sctipt/main.py
```

And set the call of this file to the desired key