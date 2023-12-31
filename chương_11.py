#11.1
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print(len(a))
print(len(b))
print(len(c))
print(len(d))

#11.2
teams=[['Steven','Neena','Lex','Alexander','Bruce'],['David','Jack','Bill','Tom','Mike','Daniel'],['Alexander','Adam','Payam','Kevin','Sigal','Mike']]
doi_te_nhat = teams[2]
doi_truong_doi_te_nhat = doi_te_nhat[1]
print('đội trưởng đội tệ nhất:', doi_truong_doi_te_nhat)

#11.3
list=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print('list of animals:',list)
print(len(list))
find = "bear" in list
print(find)

#11.6
chieu_cao_inch = [ 74,74,72,72,73,69,69,71,76,71 ]
chieu_cao_met = [ x * 0.0254 for x in chieu_cao_inch]
print('3 chiều cao đầu tiên:', chieu_cao_met[:3])
print('3 chiều cao cuối cùng:', chieu_cao_met[-3:])
print('in ra chiều cao trung bình:', sum(chieu_cao_met)/len(chieu_cao_met))
print('chiều cao lớn nhất:', max(chieu_cao_met))
print('chiều cao nhỏ nhất:', min(chieu_cao_met))
print('list theo giá trị tăng dần:', chieu_cao_inch.sort())
print('list theo giá trị giảm dần:', chieu_cao_inch.reverse())

#11.7
def elementwise_greater_than(L, thresh):
    return [ num > thresh for num in L]
L=[1,2,3,4]
thresh= 2
print(elementwise_greater_than(L, thresh))

#11.8
nums= [2,6,7,9]
def kiem_tra_so_may_man(nums):
    for so in nums:
        if so % 7 == 0:
            return True
    return False
if kiem_tra_so_may_man(nums):
    print('danh sách chứa số may mắn')
else:
    print('danh sách không chứa số may mắn')

#11.9
def ktra_khach_den_tre(arrivals,name):
    index= arrivals.index(name)
    if index == len(arrivals)-1:
        return False
    khach_toi_som=index +1
    if khach_toi_som >= len(arrivals)/2:
        return True
    else:
        return False
arrivals= ['adela','fleda','owen','may','mona','gilbert','ford']
print(ktra_khach_den_tre(arrivals,name='gilbert'))
print(ktra_khach_den_tre(arrivals,name='ford'))
print(ktra_khach_den_tre(arrivals,name='mona'))

#11.10
def menu_is_boring(meals):
    for i in range(len(meals_1)-1):
        if meals_1[i]==meals_2[i] and meals_1[i+1]==meals_2[i+1]:
            return True
    return False
meals_1=['redneck ribs','prawn star','san quentin squid','fist full of pizza','honky tonk chicken']
meals_2=['redneck ribs','prawn star','running bear salmon','running bear salmon','honky tonk chicken']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))

#11.11
tulpe = ('red','green','yellow','blue','black','white','pink','orange','red','blue')
print('tulpe', tulpe)
print(tulpe[2])
print(tulpe[-2])
s_find = 'blue'
print('blue xuất hiện trong tulpe ', tulpe.count('blue'))

#11.12
tuple_a = (3,1,2,4)
tuple_b = (5,7,6,8) 
tuple_c = tuple_a + tuple_b
print(tuple_c)     
tuple_d = sorted(tuple_c)
print(tuple_d)
print(tuple_d[3])
print('3 phần tử cuối cùng của tuple_d:',tuple_d[-3:])
