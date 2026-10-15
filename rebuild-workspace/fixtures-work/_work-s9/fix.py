p = 'verify.py'
s = open(p).read()
new = r'''if re.search(r'^(Consultant|Marisol|Warren|Ines|Speaker \d+|[A-Z][a-z]+ [A-Z][a-z]+)\s*(\(\d{2}:\d{2}:\d{2}\))?\s*:', transcript, re.M):
    err("transcript.txt appears to contain speaker labels; this fixture must have none.")'''
assert '// placeholder' in s, 'placeholder not found'
open(p, 'w').write(s.replace('// placeholder', new))
print('patched')
