'{1} {0}'.format('one', 'two')
# two one

''' ----------------------- Padding --------------------------- '''
'{:10}'.format('test')
# test      |

'{:>10}'.format('test')
#      test

'{:_<10}'.format('test')
# test______

'{:^10}'.format('test')
#   test   |

''' ----------------------- Truncating --------------------------- '''
'{:.5}'.format('xylophone')
# xylop

''' ----------------------- Number --------------------------- '''
'{:d}'.format(42)
# 42

'{:f}'.format(3.141592653589793)
# 3.141593

# Padding number
'{:4d}'.format(42)
#   42

'{:04d}'.format(42)
# 0042

'{:06.2f}'.format(3.141592653589793)
# 003.14

# 科学计数法
'{:.2e}'.format(2)