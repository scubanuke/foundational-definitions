"""Render pages/glossary.md from glossary.json. Run from the repo root: python3 tools/build_glossary.py"""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = json.load(open(os.path.join(ROOT, 'glossary.json'), encoding='utf-8'))
TITLES = {'fd-bl': 'The Bright Line', 'fd-ld': 'Layer Decomposition and Determinism', 'fd-br': 'The Broker', 'fd-ev': 'The Envelope',
          'fd-bl-d1': 'Mode of Discharge', 'fd-bl-d2': 'Indication Integrity', 'fd-ls': 'Local Sovereignty', 'fd-dbl': 'Design Basis Layers'}
def md(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
out = ['# Glossary', '',
       '<p class="lede">One glossary for every Eclectic Technologies site. The course, the CIKR examples and the SMR licensing site point here rather than defining these terms again.</p>', '',
       'Each entry is a plain-language reading. Where an entry names an instrument, the instrument governs, as issued in *%s*. Terms used on only one site stay in that site’s own glossary.' % G['edition'], '',
       '<dl class="terms">']
for x in sorted(G['terms'], key=lambda x: x['term'].lower().replace('the ', '', 1)):
    see = (' See <a href="#/%s"><em>%s</em></a>.' % (x['see'], TITLES[x['see']])) if x['see'] else ''
    out.append('<dt id="%s">%s</dt>' % (x['id'], x['term']))
    out.append('<dd>%s%s</dd>' % (md(x['def']), see))
out += ['</dl>', '']
open(os.path.join(ROOT, 'pages', 'glossary.md'), 'w', encoding='utf-8', newline='').write('\n'.join(out))
print('wrote pages/glossary.md,', len(G['terms']), 'terms')
