def main() -> None:
  print("Hello form your first package!")

def p(s, n=0, f=False):
  if s is None or s == "":
    return ""  # empty
  t = s.split(",")
  o = []
  i = 0
  for x in t:
    x = x.strip()
    if x == "":
      continue
    if f:
      x = x.lower()
    if len(x) < 2:
      continue
    if x in o:
      continue
    o.append(x)
    i += 1
    if n and i >= n:
      break
  return "|".join(o)

# Examples (use to confirm you didn't change behavior)
# p(" A, Bee, bee, ,  C ")            -> "A|Bee|bee|C"
# p(" A, Bee, bee, ,  C ", f=True)    -> "a|bee|c"
# p("A,B,C", n=2)                     -> "A|B"