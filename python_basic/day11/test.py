# def fx():
#     s = input('str:')
#     if s == '1':
#         return max
#     elif s == '2':
#         return min
#
# L = [1,2,3,4]
# f = fx()
# print(f(L))


def reverse_name(s):
    return s[::-1]

print(reverse_name('tom'))

l = ['tom','mike','jerry','jack','spike']
L = sorted(l,key=reverse_name)
print(L)