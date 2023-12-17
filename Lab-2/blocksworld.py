class BlocksWorld:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.blocks = {str(i): i for i in range(1, num_blocks + 1)}
        self.table = []

    def move_onto(self, a, b):
        self.return_blocks(a)
        self.return_blocks(b)
        self.move_to_top(a, b)
        self.stack_blocks(a, b)

    def move_over(self, a, b):
        self.return_blocks(a)
        self.move_to_top(a, b)
        self.stack_blocks(a, b)

    def pile_onto(self, a, b):
        self.return_blocks(b)
        self.move_to_top(a, b)
        self.stack_blocks(a, b)

    def pile_over(self, a, b):
        self.move_to_top(a, b)
        self.stack_blocks(a, b)

    def move_to_top(self, a, b):
        if a in self.table:
            self.table.remove(a)
        if b in self.table:
            index = self.table.index(b)
            self.table = self.table[:index + 1]

    def return_blocks(self, block):
        if block in self.table:
            index = self.table.index(block)
            for b in self.table[index + 1:]:
                self.blocks[b] = int(b)
                self.blocks[block] = int(block)
            self.table = self.table[:index + 1]

    def stack_blocks(self, a, b):
        self.blocks[a] = int(b)
        if a in self.table:
            self.table.remove(a)
        self.table.append(a)

    def print_state(self):
        for block, position in self.blocks.items():
            print(f"Block {block} is on Block {position}")


blocks_world = BlocksWorld(5)
blocks_world.print_state()
blocks_world.move_onto('1', '2')
blocks_world.move_over('3', '4')
blocks_world.pile_onto('2', '4')
blocks_world.print_state()
