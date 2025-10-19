class Grid {
  static WIDTH = 10;
  static HEIGHT = 20;

  constructor() {
    this.cells = [];

    // Initialize empty grid
    for (let y = 0; y < Grid.HEIGHT; y++) {
      this.cells[y] = [];
      for (let x = 0; x < Grid.WIDTH; x++) {
        this.cells[y][x] = 0;
      }
    }
  }

  get width() {
    return Grid.WIDTH;
  }

  get height() {
