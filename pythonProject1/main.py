from queue import Queueue
from stack import Stackk


q1 = Queueue(6)
s1 = Stackk(3)

q1.add_new("Brno")
q1.add_new("Praha")

print(q1.queue)
print(q1.read_remove())


s1.add_item("Brno")
s1.add_item("Praha")
s1.add_item("Hranice")
print(s1.stack)
s1.add_item("Olšovec")
print(s1.stack)
print(s1.pull())
print(s1.stack)
q1.add_new(s1)
print(q1.queue)