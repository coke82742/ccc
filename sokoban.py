WALL = '#'
FLOOR = ' '
PLAYER = '@'
BOX = '\$'
GOAL = '.'
BOX_ON_GOAL = '*'
PLAYER_ON_GOAL = '+'

GAME_MAP = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '\$', ' ', '.', ' ', ' ', '#'],
    ['#', ' ', ' ', '@', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', '\$', ' ', ' ', '#'],
    ['#', ' ', '.', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

DIRECTIONS = {
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1),
    '上': (-1, 0),
    '下': (1, 0),
    '左': (0, -1),
    '右': (0, 1),
}

def get_player_position(game_map):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell in (PLAYER, PLAYER_ON_GOAL):
                return (y, x)
    return None

def count_total_boxes(game_map):
    count = 0
    for row in game_map:
        for cell in row:
            if cell in (BOX, BOX_ON_GOAL):
                count += 1
    return count

def count_boxes_on_goal(game_map):
    count = 0
    for row in game_map:
        for cell in row:
            if cell == BOX_ON_GOAL:
                count += 1
    return count

def is_wall(game_map, y, x):
    return game_map[y][x] == WALL

def is_box(game_map, y, x):
    return game_map[y][x] in (BOX, BOX_ON_GOAL)

def is_floor_or_goal(game_map, y, x):
    return game_map[y][x] in (FLOOR, GOAL)

def render(game_map):
    print('\n' + '=' * 30)
    for row in game_map:
        print(''.join(row))
    print('=' * 30)
    print('操作说明: w=上 s=下 a=左 d=右')
    print('或使用: 上/下/左/右 方向指令')

def move(game_map, direction):
    player_y, player_x = get_player_position(game_map)
    dy, dx = DIRECTIONS[direction]
    new_y, new_x = player_y + dy, player_x + dx
    
    if is_wall(game_map, new_y, new_x):
        return False
    
    if is_box(game_map, new_y, new_x):
        box_new_y, box_new_x = new_y + dy, new_x + dx
        if not is_floor_or_goal(game_map, box_new_y, box_new_x):
            return False
        
        if game_map[box_new_y][box_new_x] == GOAL:
            game_map[box_new_y][box_new_x] = BOX_ON_GOAL
        else:
            game_map[box_new_y][box_new_x] = BOX
        
        if game_map[new_y][new_x] == BOX_ON_GOAL:
            game_map[new_y][new_x] = PLAYER_ON_GOAL
        else:
            game_map[new_y][new_x] = PLAYER
        
        if game_map[player_y][player_x] == PLAYER_ON_GOAL:
            game_map[player_y][player_x] = GOAL
        else:
            game_map[player_y][player_x] = FLOOR
        
        return True
    
    if is_floor_or_goal(game_map, new_y, new_x):
        if game_map[new_y][new_x] == GOAL:
            game_map[new_y][new_x] = PLAYER_ON_GOAL
        else:
            game_map[new_y][new_x] = PLAYER
        
        if game_map[player_y][player_x] == PLAYER_ON_GOAL:
            game_map[player_y][player_x] = GOAL
        else:
            game_map[player_y][player_x] = FLOOR
        
        return True
    
    return False

def check_win(game_map):
    total_boxes = count_total_boxes(game_map)
    boxes_on_goal = count_boxes_on_goal(game_map)
    return boxes_on_goal == total_boxes

def main():
    import copy
    game_map = copy.deepcopy(GAME_MAP)
    total_boxes = count_total_boxes(game_map)
    print('=== 推箱子小游戏 ===')
    print(f'总箱子数: {total_boxes}')
    
    while True:
        render(game_map)
        
        if check_win(game_map):
            print('\n🎉 恭喜你！游戏胜利！ 🎉')
            print('所有箱子都已推到终点位置！')
            break
        
        user_input = input('请输入移动指令: ').strip().lower()
        
        if user_input in ('quit', 'exit', 'q', '退出'):
            print('游戏已退出')
            break
        
        if user_input not in DIRECTIONS:
            print('无效指令！请使用 w/s/a/d 或 上/下/左/右')
            continue
        
        move(game_map, user_input)

if __name__ == '__main__':
    main()
