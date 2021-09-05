''' Game of Life '''
class Game:
    def __init__(self):
        self.states = list()

    def new(self, seed):
        self.irange = len(seed) # convas i
        self.jrange = len(seed[0]) # convas j
        self.states.append(seed) # first step is the seed itself

    ''' Run only one step forward '''
    def run_one_step(self):
        state = self.states[-1]
        new_state = list()
        for i in range(self.irange):
            row = list()
            for j in range(self.jrange):
                new_cell_state = self.cell_next_state(state, i, j)
                row.append(new_cell_state)
            new_state.append(row)
        self.states.append(new_state)
        #print(new_state)

    ''' Run the game '''
    def run(self, steps=1):
        #current_steps = len(self.states)
        for step in range(steps):
            self.run_one_step() 

    ''' Count live neighbouring cells '''
    def count_live_neighbours(self, state, i, j):
        neighbours = list()
        try:
            neighbours.append(state[i-1][j-1])
        except:
            pass
        try:
            neighbours.append(state[i][j-1])
        except:
            pass
        try:
            neighbours.append(state[i+1][j-1])
        except:
            pass
        try:    
            neighbours.append(state[i-1][j])
        except:
            pass
        try:    
            neighbours.append(state[i+1][j])
        except:
            pass
        try:    
            neighbours.append(state[i-1][j+1])
        except:
            pass
        try:    
            neighbours.append(state[i][j+1])
        except:
            pass      
        try:    
            neighbours.append(state[i+1][j+1])
        except:
            pass
        result = 0
        for neighbour in neighbours:
            if neighbour == 1: # Alive
                result += 1
        #print("i:", i)
        #print("j:", j)
        #print("neighbours:", result)
        return result

    ''' Next cell state '''
    def cell_next_state(self, state, i, j):
        next_cell_state = state[i][j] # default state
        count = self.count_live_neighbours(state, i, j)
        if state[i][j] == 1: # Alive
            if count < 2:
                next_cell_state = 0
            elif count == 2 or count == 3:
                next_cell_state = 1
            elif count > 3:
                next_cell_state = 0
        elif state[i][j] == 0: # Dead
            if count == 3:
                next_cell_state = 1
        return next_cell_state

    ''' Print states '''
    def print(self, step='all'):
        import numpy as np
        if step == 'all':
            for matrix in self.states:
                print(np.matrix(matrix))
                print('\n')
        else:
            for step_number in range(step):
                print(np.matrix(self.states[step_number]))
                print('\n')

    ''' Show as plot '''
    def show(self, step=0):
        from GoL.graphics import show
        show(self.states[step], name="step:"+str(step))

    ''' Save states to file '''
    def save(self, file_name='sample'):
        file_name += '.txt'
        with open(file_name, 'w') as f:
            for step in range(len(self.states)):
                f.writelines('step:'+str(step)+'\n')
                for i in range(self.irange):
                    line = ''
                    for j in range(self.jrange):
                        line += str(self.states[step][i][j])
                        line += ','
                    line += '\n'
                    f.writelines(line)

    ''' Load states from file '''
    def load(self, file_name='sample'):
        file_name += '.txt'
        with open(file_name, 'r') as f:
            content = f.read()
            #print(content)
            states = list()
            content_splits = content.split('step:')
            content_splits = content_splits[1:]
            #print(content_splits)
            for step_content in content_splits:
                step_content_split = step_content.split('\n')
                #step = step_content_split[0]
                step_content_split = step_content_split[1:-1]
                #print(step_content_split)
                state = list()
                for row_content in step_content_split:
                    row_content_split = row_content.split(',')
                    row_content_split = row_content_split[:-1]
                    #print(row_content_split)
                    row = list()
                    for item in row_content_split:
                        row.append(int(item))
                    state.append(row)
                states.append(state)
            #print(states)
            self.states = states
            seed = self.states[0]
            self.irange = len(seed) # convas i
            self.jrange = len(seed[0]) # convas j

    
    def animate(self, name='sample'):
        from GoL.graphics import animate
        animate(self.states, name)



if __name__ == "__main__":
    from GoL import seeds
    #seed = seeds.library['blinker']
    seed = seeds.random(50, 50)

    G = Game()
    G.load()
    #G.new(seed)
    G.run(50)
    #G.run()
    #G.print(2)
    #G.show(2)
    #G.show(-1)
    G.save()
    G.animate()
    