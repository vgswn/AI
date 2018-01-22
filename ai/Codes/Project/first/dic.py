class FileOwners:

    @staticmethod
    def group_by_owners(files):
        dic={}
        for a,b in files.items():
            if dic.__contains__(b):
                dic[b].append(a)
            else:
                at=[]
                at.append(a)
                dic[b]=at
        return dic

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
l=input()
l=l.split(sep=' ')
print(l[1])
