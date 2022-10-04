import pdbdump
import copy

tp = pdbdump.return_tp()

def syn(p):
    params  = ', '.join([i['name'] for i in p['params']])
    returns = ', '.join([i['name'] for i in p['returns']])
    name = f'pdb.{p["name"].replace("-","_")}'
    if not returns == '':
        fstr = f'{returns} = {name}({params})'
    else:
        fstr = f'{name}({params})'
    return fstr

def make_row(prod):
    nl = '\n<br>'
    op = []
    for i in prod:
        tr = {}
        tr['name'] = i[0]
        tr['type'] = i[1]
        if '@' in i[2]:
            tr['desc'] = i[2].replace(', ',nl) 
            tr['desc'] = tr['desc'].replace('@','')
            tr['desc'] = tr['desc'].replace('{','{'+nl) 
            tr['desc'] = tr['desc'].replace('}',nl+'}')
        else:
            tr['desc'] = i[2]
        op.append(copy.deepcopy(tr))
    return op

def link_dep(prod):
    if "Deprecated: Use" in prod:
        start = prod.find("'")+1
        end   = prod.rfind("'")
        name = prod[start:end]
        prod = ''.join([prod[:start], f'<a href="#{name}">', name, '</a>',prod[end:]])
    return prod

def parsescm(tp):
    op = []
    for prod in tp:
        p = {}
        p['name']      = prod[0]
        p['blurb']     = link_dep(prod[1])
        p['help']      = link_dep(prod[2])
        p['author']    = prod[3]
        p['copyright'] = prod[4]
        p['date']      = prod[5]
        p['location']  = prod[6]
        p['params']    = make_row(prod[7])
        p['returns']   = make_row(prod[8])
        p['synopsis']  = syn(p)
        op.append(copy.deepcopy(p))
        if len(prod) > 9:
            print(f"{p['name']} is greater than 9!")
    return op

def loadfile(path):
    with open(path) as f:
        return f.read()

def construct_html(m):
    header  = loadfile('header.thtml')
    body    = loadfile('pdbtemplate.thtml')
    tr      = loadfile('tr.thtml') #r'<tr><td>{name}<td>{type}<td>{desc}<tr>'
    footer  = loadfile('footer.thtml')
    content = []
    for i in m:
        cur = body.format(**i)
        params = []
        for row in i['params']:
            params.append(tr.format(**row))
        cur = cur.replace('%params%','\n'.join(params))
        returns = []
        for row in i['returns']:
            returns.append(tr.format(**row))
        cur = cur.replace('%returns%','\n'.join(returns))
        content.append(cur)
    content = '\n\n'.join(content)
    content = '\n\n'.join((header, content, footer))
    with open('pdb.html','w') as f:
        f.write(content)

construct_html(parsescm(tp))
