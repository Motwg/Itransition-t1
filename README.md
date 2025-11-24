## How to use
- cd to project catalog and put your file with data in.
- Use `docker compose start -d` to start mysql or use your own instance by changing connection config in insert.py.
- Use install.sh to install python requirements if you need `./install.sh`, remember to add x privilage `chmod +x install.sh`.
- Run `./main.sh <input filename>`, also remember to use `chmod +x main.sh`.

Conversion of json file may take a while, because it was done using bash script to **challenge myself**. 
In case it is some kind of difficulty just let me know - I can include full python implementation.
