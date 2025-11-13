import puz

#use puz.read() to load the file
p = puz.read('ZhouqinBurnikelWillShortz-NYTimesMondayNovember102025.puz')

#use clue_numbering() to get the clues and answers
#you get an object with two lists of dictionaries named across and down
#below is an example dictionary format for the fill at 1A
#{'num': 1, 'clue': 'Beginnings of days', 'clue_index': 0, 'cell': 0, 'row': 0, 'col': 0, 'len': 5, 'dir': 'across'}
numbering = p.clue_numbering()

#run puz.Grid to wrap a string into grid format, returns an object
#the inputs are the string, and you want the other two to be p.width and p.height
#the object has the methods get_string_for_clue(clue), get_cell(row, col), set_cell(row, col, char), is_black(row, col)
#here, since we are trying to get the solution grid, our first input is p.solution
solution = puz.Grid(p.solution, p.width, p.height)

print('Across')

for clue in numbering.across:
    #get_string_for_clue(clue) extracts the desired fill from the solution grid, the input is a dictionary
    answer = solution.get_string_for_clue(clue)

    print(clue['num'], clue['clue'], '-', answer)

print('Down')

for clue in numbering.down:
    answer = solution.get_string_for_clue(clue)

    print(clue['num'], clue['clue'], '-', answer)

#here, since we are trying to get the actual grid (the layout of the squares), our first input is p.fill
grid = puz.Grid(p.fill, p.width, p.height)
for row in range(p.height):
    #get_row(row) detects the row in the grid
    print(' '.join(grid.get_row(row)))

#unlock a scrambled solution, not sure if we have to use this later on but i'm keeping this here just in case
p.unlock_solution(7844)

for row in range(p.height):
    print(' '.join(solution.get_row(row)))