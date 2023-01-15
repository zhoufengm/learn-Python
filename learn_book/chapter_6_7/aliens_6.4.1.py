# 2023.1.10 6.4.1

# 创建一个用于存储外星人的空列表
aliens = []

# 创建20个绿色的外星人
for alien_number in range(20):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 修改第三个外星人颜色
aliens[2]['color'] = 'yellow'

# 显示创建了多少个外星人
print("Total number of aliens is " + str(len(aliens)))


# 修改前三个外星人颜色，速度
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')


