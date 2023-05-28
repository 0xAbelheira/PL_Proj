def p_tagline(p):
    """
    tagline : tag content INDENT lines DEDENT 
            | tag INDENT lines DEDENT 
            | tag content
            | tag BAR
            | tag DOT NEWLINE block_text
            | tag
    """
    if len(p) == 6: # tag content INDENT lines DEDENT
        p[0] = Tree(type='tagline1', trees=[p[1], p[2], Tree(type='INDENT', value=p[3]), p[4]])
    elif len(p) == 5: # tag INDENT lines DEDENT
        if p[2] == '.': # tag DOT NEWLINE text
            p[0] = Tree(type='tagline5', trees=[p[1], p[4]])
        else: # tag INDENT lines DEDENT
            p[0] = Tree(type='tagline2', trees=[p[1], Tree(type='INDENT', value=p[2]), p[3]])
    elif len(p) == 3:
        if p[2] == '/': # tag BAR
            p[0] = Tree(type='tagline4', trees=[p[1], Tree(type='BAR', value=p[2])])
        else: # tag content
            p[0] = Tree(type='tagline3', trees=[p[1], p[2]])
    else: # tag
        p[0] = Tree(type='tagline6', trees=[p[1]])