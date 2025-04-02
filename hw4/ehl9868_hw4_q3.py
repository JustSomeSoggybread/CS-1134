def print_triangle(n):
    if (n> 1):
        print_triangle(n-1)
    for i in range(n):
        print("*", end='')
    print()
def print_opposite_triangles(n):
    for i in range(n):
        print("*", end='')
    print()
    if (n> 1):
        print_opposite_triangles(n-1)
    for i in range(n):
        print("*", end='')
    print()

def print_ruler(n):
    if (n>1):
        print_ruler(n-1)
    for i in range(n):
        print("-", end='')
    print()
    if (n>1):
        print_ruler(n-1)
