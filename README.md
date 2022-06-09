# movlist
A set of tools to compute moving functions over an input stream.

### movlist.rotlist
##### (movlist.rot.rotlist)

A list of a set size that rotates elements in as add() is called.  Think of it as a queue which's size never changes, and always calls a pop() with a push() (or a dequeue() with an enqueue()).

### movlist.avglist
##### (movlist.avg.avglist)

A consumer of values streamed into its add() method, this list maintains a set of averages of different lengths.

```python
from movlist import avglist

al = avglist({
  'A':1,
  'B':5,
  'C':10,
  'D':20
})

for i in range(50):
  al.add(i)

print(al.avg())
```

This will output a dictionary containing the avg at the present moment, where each key associates with the moving average of the last that-many values added to the avglist.  This means a single object will manage moving averages of varying granularity.  Which is great!  It's the whole point of this module!
