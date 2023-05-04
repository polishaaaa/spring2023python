import pathlib
import typing as tp
from random import *

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    return [values[i*n:(i+1)*n] for i in range(n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    #return grid[i] for i in range(0,3) if pos[0]==i
    return grid[pos[0]]



def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    ans=[]
    for i in range(9):
        ans.append(grid[i][pos[1]])
    return ans




def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    r , c = pos[0] // 3 , pos[1] // 3
    ans = [grid[3*r + i][3*c + j] for i in range(3) for j in range(3)]
    return ans


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    flag=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i,j)
                flag==1
    if flag==0: return 0


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции """
    d=set(get_block(grid,pos))
    ans=get_row(grid,pos)
    for i in range(len(grid)):
        if ans[i]!='.':
            d.add(ans[i])
    ans = get_col(grid, pos)
    for i in range(len(grid)):
        if ans[i] != '.':
            d.add(ans[i])
    d1=set('123456789')
    return d1-d



def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    ans = find_empty_positions(grid)
    if find_empty_positions(grid)==0:
        return grid
    for i in find_possible_values(grid, ans):
        grid[ans[0]][ans[1]] = i
        if solve(grid):
            return solve(grid)
        else:
            grid[ans[0]][ans[1]] = "."



def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    k1,k2,k3=False, False, False
    for i in range(len(solution)):
        if set(get_row(solution,(i,0))) == set('123456789'):
            k1=True
        else: k1=False
    for i in range(len(solution)):
        if set(get_row(solution,(0,i))) == set('123456789'):
            k2=True
        else: k2=False
    for i in range(len(solution)):
        for j in range(len(solution)):
            if set(get_block(solution,((i//3)*3 ,(j//3)*3))) == set('123456789'):
                k3=True
            else: k3=False
    if k1!=False and k2!=False and k3!=False:
        return True
    else:
        return False





def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    grid = solve([['.' for i in range(9)] for j in range(9)])
    k=0
    while k!=N:
        row=randint(0,8)
        col=randint(0,8)
        if grid[row][col]=='.':
            grid[row][col]=str(randint(1,9))
            k+=1
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
