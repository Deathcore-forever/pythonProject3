x='*'
print(f'.{x:^4}.')
print(f'.{x:<1}.''.*')
print(f'.{x:>1}.''.*')
print(f'.{x:^2}.''*')
print(f'.{x:^4}.')
print()
товары=['ring','earring','wathc','glasses','pony']
итог=[6,7,8,9,4]
цена=[7000.00,3000.00,15000.00,500.00,1000000.00]
for i in range (5):
    print(f"t\t {товары[i]}\t {итог[i]}\t {цена[i]}\t {итог[i]*цена[i]}")

