"""Render the project's restricted Markdown subset to a standalone LaTeX document.

Supports simple headings/lists/tables, inline and display math, and local figures.
Not a general Markdown parser. Study and provenance documents use the same layout.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def inline(value):
    tokens=[]
    def hold(m):
        tokens.append(m.group(0))
        return f'ZZTOKEN{len(tokens)-1}ZZ'
    value=re.sub(r'\$[^$]+\$',hold,value)
    value=value.replace('\\',r'\textbackslash{}')
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]:value=value.replace(a,b)
    for a,b in [('—','---'),('–','--'),('“','"'),('”','"'),('’',"'"),('→',r'$\to$'),('≤',r'$\le$'),('≥',r'$\ge$'),('−','-'),('·',r'$\cdot$'),('…',r'\ldots{}')]:value=value.replace(a,b)
    value=re.sub(r'`([^`]+)`',lambda m: r'\path{'+m[1].replace(r'\_', '_')+'}',value)
    value=re.sub(r'\*\*([^*]+)\*\*',lambda m: r'\textbf{'+m[1]+'}',value)
    value=re.sub(r'\*([^*]+)\*',lambda m: r'\emph{'+m[1]+'}',value)
    for i,t in enumerate(tokens):value=value.replace(f'ZZTOKEN{i}ZZ',t)
    return value

def render(s, root=ROOT):
    lines=s.splitlines(); out=[]; i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip():out.append('');i+=1;continue
        if line=='$$':
            out.append(r'\[');i+=1
            while lines[i]!='$$':out.append(lines[i]);i+=1
            out.append(r'\]');i+=1;continue
        if line.startswith('### '):out.append(r'\subsection*{'+inline(line[4:])+'}');i+=1;continue
        if line.startswith('# '):out.append(r'\section*{'+inline(line[2:])+'}');i+=1;continue
        if line.startswith('## '):out.append(r'\section{'+inline(re.sub(r'^\d+\. ', '', line[3:]))+'}');i+=1;continue
        if line.startswith('!['):
            match=re.fullmatch(r'!\[(.*?)\]\((.*?)\)',line)
            if not match: raise ValueError('Invalid figure reference')
            path=Path(match[2]).name.replace('.png','.pdf')
            if not (root/'figures'/path).is_file(): raise FileNotFoundError(path)
            out.extend([r'\begin{figure}[htbp]', r'\centering',
                        r'\includegraphics[width=0.78\linewidth]{'+('figures/'+path)+'}',
                        r'\caption{'+inline(match[1])+'}',r'\end{figure}'])
            i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[x.strip() for x in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[-:]+',c) for c in cells):rows.append(cells)
                i+=1
            out += [r'\begin{center}',r'\small',r'\begin{tabular}{'+'l'*len(rows[0])+'}',r'\toprule']
            for j,row in enumerate(rows):
                out.append(' & '.join(inline(c) for c in row)+r' \\')
                if j==0:out.append(r'\midrule')
            out += [r'\bottomrule',r'\end{tabular}',r'\end{center}'];continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            numbered=not line.startswith('- ');env='enumerate' if numbered else 'itemize'
            out.append(r'\begin{'+env+'}')
            while i<len(lines) and (lines[i].startswith('- ') or re.match(r'^\d+\. ',lines[i])):
                item=re.sub(r'^(?:- |\d+\. )','',lines[i]);i+=1
                while i<len(lines) and lines[i].strip() and not lines[i].startswith('- ') and not re.match(r'^\d+\. ',lines[i]):item+=' '+lines[i];i+=1
                out.append(r'\item '+inline(item))
            out.append(r'\end{'+env+'}');continue
        para=[]
        while i<len(lines) and lines[i].strip() and lines[i]!='$$':para.append(lines[i]);i+=1
        value=' '.join(para)
        out.append(inline(value))
    return '\n'.join(out)+'\n'


def document(markdown, title, day, root=ROOT, layout=None, author=""):
    preamble = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{iftex}
\ifPDFTeX\usepackage[utf8]{inputenc}\fi
\usepackage[english]{babel}
\usepackage{amsmath,amssymb,booktabs,graphicx,enumitem}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{2em}
\setcounter{tocdepth}{1}
"""
    if layout == 'one_problem_per_page':
        body = render(markdown, root)
        body = body.replace(r'\section{', r'\clearpage\section*{', 1)
        body = body.replace(r'\section{', r'\clearpage\section*{')
        body = body.replace(r'\clearpage', '', 1)
        return (preamble + r'\setlength{\parindent}{0pt}'+'\n'+r'\setlength{\parskip}{5pt}'+'\n'+r'\begin{document}'+'\n'
                + r'\noindent\textbf{'+inline(title)+'}'+r'\\'+'\n'+inline(author)+r'\hfill '+inline(day)+'\n'
                + body + r'\end{document}'+'\n')
    return (preamble + '\\title{'+inline(title)+'}\n\\author{}\n\\date{'+day+'}\n'
            + r'\begin{document}'+'\n'+r'\maketitle'+'\n'+r'\tableofcontents'
            +'\n\\clearpage\n'+(r'\raggedright'+'\n' if 'Traceability' in title else '')+render(markdown, root)+r'\end{document}'+'\n')
