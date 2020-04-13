
def create_permutation(perm, l):
    for i in range(len(l)):
        if len(l) == 1:
            print(perm + l)
        new_l = l[0:i]+l[i+1:]
        create_permutation(perm + [l[i]], new_l)

if __name__ == '__main__':
    create_permutation([],[1,2,3])