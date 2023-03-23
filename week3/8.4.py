def simplifyPath(self, path: str) -> str:
    st = []
    dirs = path.split('/')
    for d in dirs:
        if d == "" or d == '.':
            continue
        elif d == '..':
            if len(st) != 0:
                st.pop()
        else:
            st.append(d)
    return '/' + '/'.join(st)
