<img width="925" alt="image" src="https://user-images.githubusercontent.com/45871181/181697927-8e1a962a-fb87-4b69-97ed-da719d511016.png">


```
import sys
import os

absp = os.path.abspath((os.path.join(os.path.dirname(__file__), "../../../")))

sys.path.append(absp)

from e.f.g import server
server.callme()

#above will run from anywhere, os.path.dirname will return the directory name of file with respect to place from where file is getting executed and then it will add ../../../ and then apspath will give path till PTY
```
